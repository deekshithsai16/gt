import json
from django.shortcuts import render
from .models import MediaMemory, Track

def home_view(request):
    media_qs = MediaMemory.objects.all().order_by('-created_at')
    media_list = []
    for item in media_qs:
        media_list.append({
            'src': item.file.url,
            'type': item.media_type,
            'caption': item.caption,
            'date': str(item.date) if item.date else '',
            'special': item.is_special,
        })

    track_qs = Track.objects.all().order_by('uploaded_at')
    tracks_list = []
    for t in track_qs:
        tracks_list.append({
            'id': f'backend_track_{t.id}',
            'title': t.title,
            'caption': t.caption,
            'url': t.audio_file.url,
        })

    context = {
        'db_media_json': json.dumps(media_list),
        'db_tracks_json': json.dumps(tracks_list),
    }
    return render(request, 'index.html', context)
