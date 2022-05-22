from django.db import models

class projectDoneModel(models.Model):
    Counties = models.CharField(max_length=255)
    Project_success = models.IntegerField()
    Happy_client = models.IntegerField()
    Project_done = models.IntegerField()

    def __str__(self):
            return "{}".format(self.id)

class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__ (self):
        return "{}. {}".format(self.id, self.name)