from django.urls import path
from register.views import register as register_view_function

urlpatterns = [
    path("", register_view_function, name="register"),
]