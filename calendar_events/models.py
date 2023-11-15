from django.db import models

class UserDate(models.Model):
    selected_date = models.DateField()