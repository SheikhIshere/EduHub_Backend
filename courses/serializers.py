from rest_framework import serializers
from . import models

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CourseModel
        fields = '__all__'