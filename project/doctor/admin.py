from django.contrib import admin
from .models import Contact,Doctor,City,Country,State,Specialization
# Register your models here.

admin.site.register(Contact)
admin.site.register(Doctor)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Specialization)
