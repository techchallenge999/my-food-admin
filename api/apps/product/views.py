from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from api.apps.product.models import Product
from api.apps.product.serializers import ProductSerializer


class CreateProduct(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ListProduct(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UpdateProduct(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'uuid'
