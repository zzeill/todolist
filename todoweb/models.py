from django.conf import settings
from django.db import models
from django.utils import timezone

class List(models.Model):
    idUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def activities_done(self):
        return self.activities.filter(done=True)

    def activities_notdone(self):
        return self.activities.filter(done=False)

    def activities_todo(self):
        return self.activities.filter(done=False).first()

    def __str__(self):
        return self.name


class Activity(models.Model):
    idList = models.ForeignKey('todoweb.List', related_name='activities', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)


    def complete(self):
        self.done = True
        self.save()

    def __str__(self):
        return self.title