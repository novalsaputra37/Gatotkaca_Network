from django.db import models

class projectDoneModel(models.Model):
    Counties = models.CharField(max_length=255)
    Project_success = models.IntegerField()
    Happy_client = models.IntegerField()
    Project_done = models.IntegerField()

def __str__(self):
        return "{}".format(self.id)