from django.urls import path

from api.apps.product.views import CreateProduct, ListProduct, UpdateProduct


urlpatterns = [
    path("create/", CreateProduct.as_view(), name="create"),
    path("list/", ListProduct.as_view(), name="list"),
    path("update/<uuid:uuid>", UpdateProduct.as_view(), name="update"),
]
