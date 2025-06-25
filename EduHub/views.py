from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ApiRoot(APIView):
    permission_classes = []
    def get(self, request, format=None):
        return Response({            
            'students': reverse('students-list', request=request),
            'courses': reverse('courses-list', request=request),
            'enrollments': reverse('enrollment-list', request=request),

        })
