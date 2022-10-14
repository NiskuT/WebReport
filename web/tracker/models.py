from email.policy import default
from turtle import title
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class Job(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)

class Period(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    isOpen = models.BooleanField(default=True)
    allotedTime = models.IntegerField()

class User(AbstractUser):
    job = models.ForeignKey("Job", blank=True, null=True, on_delete=models.CASCADE, related_name="users")

class Project(models.Model):
    key = models.CharField(max_length=4)    # PPPP
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_manager_of")

class Group(models.Model):
    key = models.CharField(max_length=2)    # GG
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="groups")
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="group_manager_of")

class Task(models.Model):
    key = models.CharField(max_length=4)    # TTTT
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="tasks")
    assignees = models.ManyToManyField(User, related_name="tasks")
    description = models.TextField()

class Sample(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # every sample is unique and identified by UUID v4

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="samples")
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name="samples")

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="samples")

    hours = models.IntegerField()
    amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)

    updated = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="edited_samples")