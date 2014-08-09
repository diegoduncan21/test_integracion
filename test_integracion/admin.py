from django.contrib import admin

from .models import Person, Info

class PersonModelAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'dni')

admin.site.register(Person, PersonModelAdmin)
admin.site.register(Info)
