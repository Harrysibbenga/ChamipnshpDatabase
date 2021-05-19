from django.db import models


# Create your models here.

# Modal Managers
class DriverManager(models.Manager):

    def create_driver(self, first_name, last_name, nat):
        driver = self.create(first_name=first_name, last_name=last_name, nat=nat)
        return driver


class CreateByNameManager(models.Manager):

    def create_item(self, name):
        item = self.create(name=name)
        return item


class CreateYearManager(models.Manager):

    def create_item(self, year):
        year = self.create(year=year)
        return year


# Models
class Driver(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    dob = models.DateField(blank=True, null=True)
    nat = models.CharField(max_length=150)
    image = models.ImageField()

    objects = DriverManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def podiums(self):
        podiums = Result.objects.filter(driver=self, position__lte=3)
        return len(podiums)


class Track(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False)
    length = models.CharField(max_length=150)
    corners = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=20)

    objects = CreateByNameManager()

    def __str__(self):
        return self.name


class Team(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, unique=True)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    image = models.ImageField()

    objects = CreateByNameManager()

    def __str__(self):
        return self.name


class DriverClass(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, unique=True)

    objects = CreateByNameManager()

    def __str__(self):
        return self.name


class Session(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, unique=True)

    objects = CreateByNameManager()

    def __str__(self):
        return self.name


class Championship(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, unique=True)

    objects = CreateByNameManager()

    def __str__(self):
        return self.name


class RoadCondition(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, unique=True)

    objects = CreateByNameManager()

    def __str__(self):
        return self.name


class Year(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)

    objects = CreateByNameManager()

    def __str__(self):
        return self.name


class Result(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    track = models.ForeignKey('Track', on_delete=models.CASCADE)
    championship = models.ForeignKey(
        'Championship', on_delete=models.CASCADE)
    driver_class = models.ForeignKey(
        'DriverClass', on_delete=models.CASCADE)
    year = models.ForeignKey('Year', on_delete=models.CASCADE)
    team = models.ForeignKey(
        'Team', on_delete=models.CASCADE)
    road_condition = models.ForeignKey(
        'RoadCondition', on_delete=models.CASCADE)
    round_number = models.IntegerField()
    position = models.IntegerField()
    position_in_class = models.IntegerField()
    best_time = models.TimeField()
    total_time = models.TimeField(blank=True, null=True)
    laps = models.IntegerField()
    best_time_on_lap = models.IntegerField()
    mph = models.DecimalField(max_digits=5, decimal_places=2)
    date_of_event = models.DateField()
    time_of_event = models.TimeField()
