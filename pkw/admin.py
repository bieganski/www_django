from django.contrib import admin

from .models import Wybory, Kandydat, Okregi

# Register your models here.

admin.site.register(Wybory)
admin.site.register(Kandydat)
admin.site.register(Okregi)