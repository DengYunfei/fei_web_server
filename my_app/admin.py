from django.contrib import admin

# Register your models here.
from my_app.models import Topic
from my_app.models import Entry

admin.site.register(Topic)
admin.site.register(Entry)
