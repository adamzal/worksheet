from django.db import models

# Create your models here.

class IndirectWeeklyWorksheets(models.Model):

    user = models.ForeignKey(NextUser, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    number_sheets_submitted = models.PositiveIntegerField()
    absent_full_week = models.BooleanField(default=False)

    week_total = models.PositiveIntegerField(default=0)
    sunday = models.PositiveIntegerField(default=0)
    monday = models.PositiveIntegerField(default=0)
    tuesday = models.PositiveIntegerField(default=0)
    wednesday = models.PositiveIntegerField(default=0)
    thursday = models.PositiveIntegerField(default=0)
    friday = models.PositiveIntegerField(default=0)
    saturday = models.PositiveIntegerField(default=0)
    

class DirectWeeklyWorksheets(models.Model):

    user = models.ForeignKey(NextUser, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    number_sheets_submitted = models.PositiveIntegerField()
    absent_full_week = models.BooleanField(default=False)

    week_total = models.PositiveIntegerField(default=0)
    sunday = models.PositiveIntegerField(default=0)
    monday = models.PositiveIntegerField(default=0)
    tuesday = models.PositiveIntegerField(default=0)
    wednesday = models.PositiveIntegerField(default=0)
    thursday = models.PositiveIntegerField(default=0)
    friday = models.PositiveIntegerField(default=0)
    saturday = models.PositiveIntegerField(default=0)
