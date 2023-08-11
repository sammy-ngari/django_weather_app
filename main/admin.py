from django.contrib import admin
from .models import Continent, Country, Location, WeatherEntry

# Register your models here.

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(WeatherEntry)