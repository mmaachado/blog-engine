import string
from random import SystemRandom

from django.utils.text import slugify


def random_letters(size: int = 5):
    return ''.join(
        SystemRandom().choices(
            string.ascii_lowercase + string.digits,
            k=size,
        )
    )


def new_slug(text: str):
    return slugify(text) + '-' + random_letters()
