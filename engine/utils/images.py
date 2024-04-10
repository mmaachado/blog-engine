from pathlib import Path

from django.conf import settings
from PIL import Image


def resize_image(
    image_django: str,
    new_width: int = 800,
    optimize: bool = True,
    quality: int = 60,
):
    """
    resize images uploaded from user.

    Arguments:
        image_django -- the image uploaded by the user.

    Keyword Arguments:
        new_width -- new width of the image. (default: {800})
        optimize -- optimize image uploaded (default: {True})
        quality -- defines the image quality (default: {60})

    Returns:
        new image resized.
    """

    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_heigth = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow

    new_heigth = round(new_width * original_heigth / original_width)

    new_image = image_pillow.resize((new_width, new_heigth), Image.LANCZOS)
    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image
