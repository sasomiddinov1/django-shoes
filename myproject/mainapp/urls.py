from django.urls import path
from .views import shopPage, mycontact


urlpatterns = [
    path("", shopPage, name="shop_page"),
    path('contact', mycontact, name="contact"),
]