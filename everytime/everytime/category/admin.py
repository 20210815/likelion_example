from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('content', )

    prepopulated_fields = {'slug': ('title', )}
# Register your models here.
admin.site.register(Category, CategoryAdmin)


