from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid


class User(AbstractUser):
    pass


class Period(models.Model):
    isActive = models.BooleanField(default=True)
    startDate = models.DateField()
    endDate = models.DateField()
    allottedHours = models.IntegerField()


class Project(models.Model):
    key = models.CharField(max_length=4)    # PPPP
    

class Group(models.Model):
    key = models.CharField(max_length=2)    # GG
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="groups")


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
    