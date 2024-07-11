from django.db import models

# Create your models here.

class Regist(models.Model):
    dEmailId=models.EmailField()
    dbasePassword=models.CharField(max_length=25)

    def __str__(self):
        return self.dEmailId
 
class Breakfast(models.Model):
    breakfastfood=models.CharField(max_length=25)
    breakfastcalories=models.IntegerField()
    breakfastprotein=models.FloatField()
    breakfastcarbohydrate=models.FloatField()
    breakfastfat=models.FloatField()

    def __str__(s):
        return s.breakfastfood

class Lunch(models.Model):
    lunchfood=models.CharField(max_length=25)
    lunchcalories=models.IntegerField()
    lunchprotein=models.FloatField()
    lunchcarbohydrate=models.FloatField()
    lunchfat=models.FloatField()

    def __str__(s):
        return s.lunchfood
    
class Dinner(models.Model):
    dinnerfood=models.CharField(max_length=25)
    dinnercalories=models.IntegerField()
    dinnerprotein=models.FloatField()
    dinnercarbohydrate=models.FloatField()
    dinnerfat=models.FloatField()

    def __str__(s):
        return s.dinnerfood
    
class totalcalories(models.Model):
    Emailid=models.CharField(max_length=25)
    date=models.DateField()
    eatenfoods=models.CharField(max_length=25)
    totalcalories=models.IntegerField()
    totalprotein=models.IntegerField()
    totalcarbohydrate=models.IntegerField()
    totalfat=models.IntegerField()

    def __str__(s):
        return s.eatenfoods
    
class caloriestarget(models.Model):
    Emailid=models.CharField(max_length=25)
    Age=models.IntegerField()
    Weight=models.IntegerField()
    Height=models.IntegerField()
    Target=models.IntegerField()

    def __str__(s):
        return s.Emailid

