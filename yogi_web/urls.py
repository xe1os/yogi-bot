from django.urls import path

from . import views


app_name = "yogi_web"

urlpatterns = [path("", views.return_one, name="one")]
