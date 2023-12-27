from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.TextField()


class Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projectinterests = ArrayField(models.TextField(), blank=True, default=list)
    toolsknown = ArrayField(models.TextField(), blank=True, default=list)
    toolsdesiredtolearn = ArrayField(models.TextField(), blank=True, default=list)
    topicinterests = ArrayField(models.TextField(), blank=True, default=list)


class Generation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    tools = ArrayField(models.TextField(), blank=True, default=list)
    difficulty = models.TextField()
    time = models.TextField()


class SavedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Generation, on_delete=models.CASCADE)

