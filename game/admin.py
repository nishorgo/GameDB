from django.contrib import admin
from .models import Publisher, Developer, Game, GamePlatform, Platform

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Developer)
admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(GamePlatform)