from django.db import models
from core import models as core_models


class FileManager(models.Manager):

    def check_if_exists(self, name, track, session, champ, year, file, round_number):
        try:
            return self.create(
                round_number=round_number,
                file=file,
                year=year,
                championship=champ,
                session=session,
                track=track,
                name=name
            )
        except:
            return None


# Create your models here.
class File(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    round_number = models.IntegerField()
    file = models.FileField(unique=True)
    session = models.ForeignKey(core_models.Session, on_delete=models.CASCADE)
    track = models.ForeignKey(core_models.Track, on_delete=models.CASCADE)
    championship = models.ForeignKey(
        core_models.Championship, on_delete=models.CASCADE)
    year = models.ForeignKey(core_models.Year, on_delete=models.CASCADE)

    objects = FileManager()

    class Meta:
        unique_together = (('name', 'year', 'session', 'round_number', 'championship', 'track'),)
        index_together = (('name', 'year', 'session', 'round_number', 'championship', 'track'),)

    def __str__(self):
        return self.name + '(' + self.track.name + '-' + self.year.name + ')'
