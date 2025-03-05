from django.db import models


# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=50)

    def __str__(self):
        return self.room_name
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    sender = models.CharField(max_length= 50)
    message = models.TextField()

    def __str__(self):
        return f"{str(self.room)} - {self.sender}"


class UploadDp(models.Model):
    user = models.CharField(max_length=50, null=True)
    dp = models.ImageField(upload_to="images")
    

class Recents(models.Model):
    chats = models.CharField(max_length=50, null=True)
    user_name = models.CharField(max_length=50, null=True)
    join_name = models.CharField(max_length=50, null=True)
    room_name = models.CharField(max_length=50, null=True)
    time = models.TimeField(auto_now=True)