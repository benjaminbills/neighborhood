from customer.models import Business, Neighborhood, Post, Profile
from django.contrib import admin

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)

