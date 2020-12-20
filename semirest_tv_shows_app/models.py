from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def show_validator(self, postdata):
        errors={}
        if len(postdata['title'])<2:
            errors['title']="The title must be at least 2 characters"
        if len(postdata['network'])<3:
            errors['network']="The network must be at least 3 characters"
        if len(postdata['desc'])>0:
            if len(postdata['desc'])<10:
                errors['desc']="If a description is provided, it must be at least 10 characters"
        if datetime.strptime(postdata['release_date'], '%Y-%m-%d')>datetime.now():
            errors['release_date'] = 'Release date must be in the past'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.CharField(max_length=750)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()