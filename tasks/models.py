from django.db import models
from users.models import Profile

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ("WAITING", "Waiting for executor"),
        ("IN_PROCESS", "In process"),
        ("FINISHED", "Finished"),
    )

    orderer = models.ForeignKey(Profile, related_name="created_tasks", on_delete=models.CASCADE)
    executor = models.ForeignKey(Profile, related_name="taken_tasks", blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    status = models.CharField(max_length=20,
        choices=STATUS_CHOICES,
        default="Waiting for executor")
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    finished_date = models.DateTimeField(blank=True, null=True)
    report = models.TextField(blank=True)
