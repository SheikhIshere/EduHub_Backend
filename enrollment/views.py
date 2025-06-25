from rest_framework import viewsets
from .models import EnrollmentModel
from .serializers import Enrollmenterializers


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = EnrollmentModel.objects.all()
    serializer_class = Enrollmenterializers