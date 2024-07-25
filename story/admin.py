from django.contrib import admin
from django.contrib.auth.models import User
from .models import Story, Profile


# Mix Profile info into user info (Macam stackkan profile skli dgn user)
class ProfileInline(admin.StackedInline):
    model = Profile

#extend user to display on admin
class UserAdmin(admin.ModelAdmin):
    model = User
    #username dari User
    fields = ["username"]
    inlines = [ProfileInline]


# Register your models here.
admin.site.register(Story)
admin.site.register(Profile)
