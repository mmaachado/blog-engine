from django.core.exceptions import ValidationError


def validate_png(image):
    """
    validate if image uploaded by user is png.

    Arguments:
        image -- the image uploaded by user.

    Raises:
        ValidationError: display to user `favicon must be .png` error.
    """
    if not image.name.lower().endswith('.png'):
        raise ValidationError('favicon must be .png')
