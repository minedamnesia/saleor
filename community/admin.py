from django.contrib import admin

from .models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ['description', 'is_featured', 'created_at']
    ordering = ['-created_at']
    list_filter = ['is_featured']


admin.site.register(Story, StoryAdmin)
