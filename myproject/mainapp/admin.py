from django.contrib import admin
from .models import *
from .models import Contact

# Register your models here.
admin.site.register(Company)
admin.site.register(Shoes)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message')

admin.site.register(Contact, ContactAdmin)