from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
    	return self.first_name + " " + self.last_name

class Memory(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
    	return self.location