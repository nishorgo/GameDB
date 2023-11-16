from django.contrib import admin
from .models import Publisher, Developer, Game, GamePlatform, Platform, Audience, Review, Wishlist

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Developer)
admin.site.register(Platform)
admin.site.register(Game)
admin.site.register(Audience)
admin.site.register(Review)
admin.site.register(Wishlist)