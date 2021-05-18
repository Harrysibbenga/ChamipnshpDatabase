from django.db import models


# Create your models here.
class File(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    session = models.CharField(max_length=150)
    championship = models.CharField(max_length=200)
    track = models.CharField(max_length=200)
    round_number = models.IntegerField()
    file = models.FileField(unique=True)

    class Meta:
        unique_together = (('name', 'year', 'session', 'round_number', 'championship', 'track'),)
        index_together = (('name', 'year', 'session', 'round_number', 'championship', 'track'),)

    def __str__(self):
        return self.name + '(' + self.track + '-' + self.year + ')'
