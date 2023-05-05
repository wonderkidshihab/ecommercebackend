from django.urls import include, path
from .views import ProductList, ProductDetail
urlpatterns = [
    path('<int:pk>', ProductDetail.as_view()),
    path('/', ProductList.as_view()),
]
