from django.contrib import admin

from travel_anywhere.models import (Airport, City, Continent, Country, Hotel,
                                    Trip)

admin.site.register(Continent)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Airport)
admin.site.register(Hotel)
admin.site.register(Trip)
