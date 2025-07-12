from django.contrib import admin

from phones.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_phone = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists']
# Register your models here.
