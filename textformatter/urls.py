from django.urls import path

from . import views

app_name = "textformatter"
urlpatterns = [
    path("", views.IndexView, name="index"),
    path("newsong", views.NewSongView, name="newsong"),
    # path("newalbum", views.NewSongView, name="newsong"),
]