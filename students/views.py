from rest_framework import viewsets
from .models import StudentModel
from .serializers import StudentSerializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers