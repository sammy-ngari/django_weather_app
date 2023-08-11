from django.db import models


# Create your models here.
# A model that represent the continents (will require a predifened list of continents and countries in the database)
class Continent(models.Model):
    name= models.CharField(max_length=50)

    def str(self):
        return self.name
    
 # Model representing the country, the country is associated with the Continent using a foreign key 
class Country(models.Model):
    name = models.CharField(max_length=100)
    continet = models.ForeignKey(Continent, on_delete=models.CASCADE)

    def str(self):
        return self.name    
    
# Model represents the specific location in a country
class Location(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE) #If using user authentication

    def str(self):
        return self.name
    
class WeatherEntry(models.model):
    Location= models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    weather_condition = models.CharField(max_length=50)

    def str(self):
        return f"Weather at {self.location.name} - {self.timestamp}"