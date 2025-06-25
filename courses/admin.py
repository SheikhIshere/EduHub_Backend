from django.contrib import admin
from .models import CourseModel
# Register your models here.
@admin.register(CourseModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'fee']