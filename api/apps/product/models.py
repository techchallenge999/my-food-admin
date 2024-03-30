from enum import Enum
import uuid

from django.db import models

from api.shared.mixins import TimestampMixin


def image_file_path(instance, filename):
    return '/'.join((
        'media',
        'products',
        str(instance.uuid),
    ))


class ProductCategory(Enum):
    SANDWICH = "lanche"
    SIDE_DISH = "acompanhamento"
    BEVERAGE = "bebida"
    DESSERT = "sobremesa"


class Product(TimestampMixin):
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[(category.value, category.value) for category in ProductCategory],
    )
    price = price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    image = models.ImageField(
        null=True,
        upload_to=image_file_path,
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=False)
