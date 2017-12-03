from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User object: {}>".format(self.name)
    
class Book(models.Model):
    bname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploader = models.ForeignKey(User, related_name="uploaded_books") #one to many
    liked_users = models.ManyToManyField(User, related_name="liked_books") #many to many
    def __repr__(self):
        return "<Book object: {}>".format(self.bname)

    