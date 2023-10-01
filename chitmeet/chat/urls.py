from django.urls import re_path, path

from .views import home

urlpatterns = [
    re_path(r"(?P<username>[\w.@+-]+)/$", home),
]
