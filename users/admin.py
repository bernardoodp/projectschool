from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')


admin.site.register(CustomUser, UserAdmin)
# Register your models here.
