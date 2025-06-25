# enrollment/models.py
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from students.models import StudentModel
from courses.models import CourseModel

class EnrollmentModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    courses = models.ManyToManyField(CourseModel)
    total_fee = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    is_canceled = models.BooleanField(default=False)  # Fixed spelling

    # Removed save override

# Signal handler to update fees on course changes
@receiver(m2m_changed, sender=EnrollmentModel.courses.through)
def update_total_fee(sender, instance, action, **kwargs):
    if action in ("post_add", "post_remove", "post_clear"):
        total = sum(course.fee for course in instance.courses.all())
        instance.total_fee = total
        instance.save(update_fields=['total_fee'])