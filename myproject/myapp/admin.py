from django.contrib import admin
from .models import Menu, Person, Logger

# Register your models here.
admin.site.register(Person)
admin.site.register(Menu)
admin.site.register(Logger)