from django.db import models

class Manage(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)
    def __str__(self):
        return self.ename