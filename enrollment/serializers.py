from rest_framework import serializers
from . import models

class Enrollmenterializers(serializers.ModelSerializer):
    class Meta:
        model = models.EnrollmentModel
        fields = '__all__'
        read_only_fields = ['total_fee']