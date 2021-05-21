from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Team, Driver, Championship, Year, DriverClass, \
    Track, Result, Session, RoadCondition, Weather

from .models import File

# helper code
from helpers.base import check_item, check_conversion, check_variable
from helpers.driver import check_driver


# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        if 'file' in request.FILES:
            # check if file is present
            file = request.FILES['file']

            # was upload conversion successful ?
            df = check_conversion(file)
            if df is None:
                response = {
                    'message': "Check file type it wasn't able to be converted to a data frame",
                }

                return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

            # get request variables and store in dictionary
            variables = {"year": request.data['year'],
                         'champ': request.data['champ'],
                         'track': request.data['track'],
                         'session': request.data['session'],
                         'round_number': request.data['round_number'],
                         'road': request.data['road'],
                         'weather': request.data['weather'],
                         'date': request.data['date'],
                         'time': request.data['time']
                         }

            # loop through variables.items() which is a list of tuples and check them
            for v in variables.items():
                if not check_variable(v):
                    response = {
                        'message': "Check variable " + v[0] + " shouldn't be empty",
                    }

                    return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)

            # get modal instances for request data or create it and return it if not present
            year = check_item(variables['year'], Year)
            session = check_item(variables['session'], Session)
            champ = check_item(variables['champ'], Championship)
            track = check_item(variables['track'], Track)
            road_condition = check_item(variables['road'], RoadCondition)
            weather = check_item(variables['weather'], Weather)

            # upload file and return none if the file has been uploaded before
            file = File.objects.check_if_exists(
                round_number=variables['round_number'],
                file=file,
                year=year,
                champ=champ,
                session=session,
                track=track,
                name=file.name
            )

            if file is not None:
                # try to upload the file and check if same upload has been performed prior
                try:
                    # create separate series for each variable
                    names = df['NAME']
                    nationality = df['NAT']
                    positions = df['POS']
                    classes = df['CL']
                    position_in_class = df['PIC']
                    teams = df['ENTRY']
                    best_times = df['TIME']
                    best_times_on_lap = df['ON']
                    laps = df['LAPS']
                    speeds = df['MPH']

                    # loop through each variable after zipping them together.
                    for (name, nat, pos, cls, pis, entry, bt, btol, lap, mph) in zip(names, nationality, positions, classes,
                                                                                     position_in_class, teams, best_times,
                                                                                     best_times_on_lap, laps, speeds):
                        # get driver names
                        names = name.split(' ')
                        first_name = names[0]
                        last_name = names[1]

                        # check to see if variables from data frame still exist already in db, and upload if not,
                        # then set
                        driver = check_driver(first_name, last_name, nat, Driver)
                        team = check_item(entry, Team)
                        driver_class = check_item(cls, DriverClass)

                        Result.objects.create(

                            driver=driver,
                            team=team,
                            driver_class=driver_class,
                            year=year,
                            session=session,
                            championship=champ,
                            track=track,
                            mph=mph,
                            position=pos,
                            road_condition=road_condition,
                            position_in_class=pis,
                            best_time=bt,
                            best_time_on_lap=btol,
                            round_number=variables['round_number'],
                            laps=lap,
                            weather=weather,
                            date_of_event=variables['date'],
                            time_of_event=variables['time'],

                        )

                        print(name, nat, pos, cls, pis, entry, bt, btol, lap, mph)

                    response = {
                        'message': 'Uploaded to database',
                    }

                    return Response(response, status=status.HTTP_200_OK)

                except:
                    response = {'message': 'Cannot upload file that has been previously uploaded'}

                    return Response(response, status=status.HTTP_400_BAD_REQUEST)

            else:
                response = {
                    'message': "File has already been uploaded",
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = {
                'message': 'Need to provide a file'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
