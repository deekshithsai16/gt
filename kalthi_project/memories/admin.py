from django.contrib import admin
from .models import MediaMemory, Track

@admin.register(MediaMemory)
class MediaMemoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'media_type', 'date', 'is_special', 'created_at')
    list_filter = ('media_type', 'is_special', 'date')
    search_fields = ('caption',)

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'caption', 'audio_file', 'uploaded_at')
    search_fields = ('title', 'caption')
