from django.contrib import admin
from home.models import Contact
from home.models import posts
from home.models import Home
# Register your models here.

admin.site.register(Contact)
admin.site.register(posts)
admin.site.register(Home)