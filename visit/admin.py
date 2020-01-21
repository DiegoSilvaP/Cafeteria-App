from django.contrib import admin
from .models import Cover, TimeTable, Visit

# Register your models here.
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('get_days', 'get_hours',)

    def get_days(self, obj):
        if obj.get_FromDay_display() != obj.get_ToDay_display():
            return obj.get_FromDay_display() + " - " + obj.get_ToDay_display()
        else:
            return obj.get_FromDay_display()

    get_days.short_description = 'Days'

    def get_hours(self, obj):
        return obj.get_FromHour_display() + " - " + obj.get_ToHour_display()

    get_hours.short_description = 'Hours'

admin.site.register(Visit)
admin.site.register(Cover)
admin.site.register(TimeTable,TimeTableAdmin)
