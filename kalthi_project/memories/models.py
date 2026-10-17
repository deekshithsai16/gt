from django.db import models

class MediaMemory(models.Model):
    MEDIA_TYPES = (
        ('photo', 'Photo'),
        ('video', 'Video'),
    )
    caption = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='memories/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='photo')
    date = models.DateField(null=True, blank=True)
    is_special = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Media Memory'
        verbose_name_plural = 'Media Memories'

    def __str__(self):
        return self.caption or f"Media {self.id}"


class Track(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200, blank=True)
    audio_file = models.FileField(upload_to='tracks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    def __str__(self):
        return self.title
