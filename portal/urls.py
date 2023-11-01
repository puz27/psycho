from django.urls import path
from portal.views import MainView


app_name = "portal"

urlpatterns = [
    path("", MainView.as_view(), name="Main_page"),
]
