from django.contrib import admin
from .models import User, Profile, Company
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Company)
