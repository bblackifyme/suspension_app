from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Setting(models.Model):
    SpringRate = models.IntegerField()
    FrontCompression = models.IntegerField()
    FrontRebound = models.IntegerField()
    RearHighSpeedCompression = models.IntegerField()
    RearLowSpeedCompression = models.IntegerField()
    RearRebound = models.IntegerField()
    Sag = models.IntegerField()
    Notes = models.TextField()
    # Define Relationships
    Bike = models.ForeignKey('Bike', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return """\n
        Front Suspension
        ----------------\n
        Spring Rate: %s,
        Front Compression: %s,
        Front Rebound: %s,

        Rear Suspension
        ---------------
        Rear High Speed Compression: %s,
        Rear Low Speed Compression: %s,
        Rear Rebound %s,
        Sag: %s

        Notes:
        ------
        %s
        """ % (
            self.SpringRate,
            self.FrontCompression,
            self.FrontRebound,
            self.RearHighSpeedCompression,
            self.RearLowSpeedCompression,
            self.RearRebound,
            self.Sag,
            self.Notes
        )
    
    def get_absolute_url(self):
        return "/settings/%s" % self.Bike.id

class Bike(models.Model):
    "Class reperesenting a Dirt Bike & its meta data"
    Make = models.CharField(max_length=10)
    Model = models.CharField(max_length=10)
    Year = models.IntegerField()
    Fork = models.CharField(max_length=20)
    Shock = models.CharField(max_length=20)
    LastMaintence = models.DateField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % ( self.Year, self.Make, self.Model)

    def get_absolute_url(self):
        return "/settings"
        