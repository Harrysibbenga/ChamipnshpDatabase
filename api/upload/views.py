from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FileSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import File
from core.models import Team, Driver, Championship, Year, DriverClass, Track, Result, Session, RoadCondition

# helper code
from helpers.base import check_item
from helpers.driver import check_driver

# Python libraries
import tabula
import pandas as pd
import numpy as np


# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):

        # check if file is uploaded
        if 'file' in request.FILES:

            # get the request variables
            file = request.FILES['file']
            year = request.data['year']
            champ = request.data['champ']
            track = request.data['track']
            session = request.data['session']
            round_number = request.data['round_number']
            road = request.data['road']

            # convert pdf to data frame
            df = tabula.read_pdf(file)[0]

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

            # try to upload the file and check if same upload has been performed prior
            try:
                File.objects.create(
                    round_number=round_number,
                    file=file,
                    year=year,
                    championship=champ,
                    session=session,
                    track=track,
                    name=file.name
                )

                # loop through each variable after zipping them together.
                for (name, nat, pos, cls, pis, entry, bt, btol, lap, mph) in zip(names, nationality, positions, classes,
                                                                                 position_in_class, teams, best_times,
                                                                                 best_times_on_lap, laps, speeds):
                    # get driver names
                    names = name.split(' ')
                    first_name = names[0]
                    last_name = names[1]

                    # check to see if variables exist already in db, and upload if not, then set
                    driver = check_driver(first_name, last_name, nat, Driver)
                    team = check_item(entry, Team)
                    driver_class = check_item(cls, DriverClass)
                    year = check_item(year, Year)
                    session = check_item(session, Session)
                    champ = check_item(champ, Championship)
                    track = check_item(track, Track)
                    road_condition = check_item(road, RoadCondition)

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
                        round_number=round_number,
                        laps=lap,

                    )

                response = {
                    'message': 'Uploaded to database',
                }

                return Response(response, status=status.HTTP_200_OK)

            except:
                response = {'message': 'Cannot upload file that has been previously uploaded'}

                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = {
                'message': 'Need to provide a file'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
