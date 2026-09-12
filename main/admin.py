from django.contrib import admin
from main import models
admin.site.register([
    models.Article,
    models.Author,
])
# Register your models here.
