from django.db import models
from django.contrib.auth.models import User

# class declarations for each of our models 
# p.s. Django will auto-generate FKs for us by subclassing models.Model

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE) # FK from Topic to Board (board will now have topics prop)
    creator = models.ForeignKey(User, related_name='topics', on_delete=models.DO_NOTHING) # FK from Topic to User

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE) # FK from Post to Topic
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING) # FK from Post to User
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.DO_NOTHING) # + as name instructs Django to NOT create a prop on User for this
    updated_at = models.DateTimeField(null=True)    
 