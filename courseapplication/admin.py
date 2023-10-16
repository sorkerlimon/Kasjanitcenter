from django.contrib import admin
from .models import Course, CourseRegistration

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'national_id', 'registration_date')
    list_filter = ('courses', 'registration_date')

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseRegistration, CourseRegistrationAdmin)
