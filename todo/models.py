from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255)

class Assignee(models.Model):
    name = models.CharField(max_length=255)

class TaskExecution(models.Model):
    TASK_CHOICES = [
        ("I", "Initialized"),
        ("S", "Succeeded")
    ]
    status = models.CharField(max_length=11, choices=TASK_CHOICES)
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    assignee = models.ForeignKey("Assignee", on_delete=models.CASCADE)

class Achievement(models.Model):
    name = models.CharField(max_length=255)
    count = models.PositiveSmallIntegerField()
    assignees = models.ManyToManyField("Assignee")
