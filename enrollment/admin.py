# enrollment/admin.py
from django.contrib import admin
from .models import EnrollmentModel

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'student', 
        'total_fee', 
        'enrolled_on', 
        'grade', 
        'is_canceled'
    )
    
admin.site.register(EnrollmentModel, EnrollmentAdmin)