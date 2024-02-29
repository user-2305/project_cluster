from django.db import models

# Create your models here.
class Post(models.Model): #старый проект
    title = models.CharField(max_length=450)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

class Edu(models.Model):
    region = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    indicator = models.CharField(max_length=255)
    amount = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.region

class Empl(models.Model):
    region = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    indicator = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=4, decimal_places=1)
    year = models.IntegerField()

    def __str__(self):
        return self.region

class Agr(models.Model):
    region = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    indicator = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=1)
    year = models.IntegerField()

    def __str__(self):
        return self.region