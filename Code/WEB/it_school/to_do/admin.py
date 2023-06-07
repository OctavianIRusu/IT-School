from django.contrib import admin
from to_do.models import Todo

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, AuthorAdmin)