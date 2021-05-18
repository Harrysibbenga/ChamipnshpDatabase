from django.contrib import admin
from .models import Driver, Team, Track, Championship, Result, Year, Session, RoadCondition, DriverClass

# Register your models here.


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['driver', 'team',
                    'round_number', 'track', 'year', 'position', 'position_in_class', 'mph', 'session', 'championship']
    list_filter = ['year', 'track', 'driver', 'championship']


admin.site.register(Driver)
admin.site.register(Team)
admin.site.register(Track)
admin.site.register(Championship)
admin.site.register(Year)
admin.site.register(DriverClass)
admin.site.register(Session)
admin.site.register(RoadCondition)

