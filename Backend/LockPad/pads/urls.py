from django.urls import path
from .views import OpenPadView, SavePadView

urlpatterns = [
    path("open/", OpenPadView.as_view()),
    path("save/", SavePadView.as_view()),
]
