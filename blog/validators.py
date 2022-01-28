from django.core.exceptions import ValidationError
import magic


def validate_file_type(f):
    """Validates that a file is either an image or a video"""
    accepted_media = (
        'image/jpeg', 'image/png', 'image/webp',
        'image/gif', 'video/mp4', 'video/quicktime', 
        'video/webm'
    )

    file_type = magic.from_buffer(f.read(1024), mime=True)
    f.seek(0)

    if file_type not in accepted_media:
        raise ValidationError("Please upload images or videos")
    else:
        return f
