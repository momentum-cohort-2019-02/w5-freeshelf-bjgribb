from django.contrib import admin
from core.models import Book, Topic

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Topic)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_topics')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
