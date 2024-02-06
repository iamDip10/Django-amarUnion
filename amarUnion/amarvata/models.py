from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20, null=True)
    per_add = models.CharField(max_length=60, null=True)
    press_add = models.CharField(max_length=60, null=True)
    mobile = models.CharField(max_length=14, null=True)
    nid_number = models.CharField(max_length=14, primary_key=True)
    password = models.CharField(max_length=18, null=True)

    class Meta:
        db_table = "user"

