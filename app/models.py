from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(blank=True, null=False)
    user_name = models.CharField(blank=True, null=False, max_length=25)
    user_pass = models.CharField(blank=True, null=False, max_length=100)
    join_date = models.DateTimeField(blank=True, null=False)

