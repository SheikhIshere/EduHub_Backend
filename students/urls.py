from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('students', views.StudentViewSet, basename='students')
# Add other registrations as needed

urlpatterns = router.urls