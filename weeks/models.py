from django.db import models

# Create your models here.

class Week(models.Model):

    user = models.ForeignKey(NextUser, on_delete=models.CASCADE)
    year = models.ForeignKey(YearOfWork, on_delete=models.CASCADE)
    number_of_week = models.PositiveIntegerField()    
    start_of_week = models.DateField()
    end_of_week = models.DateField()
    
    
class YearOfWork(models.Model):

    year = models.CharField(max_length=4)
    user = models.ForeignKey(NextUser, on_delete = models.CASCADE)
