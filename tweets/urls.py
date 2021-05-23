from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path("", views.create_tweet, name="create_tweet"),
    path('<int:pk>', views.detail_tweet, name="detail_tweet"),
    path("/update/<int:pk>", views.update_tweet, name="update_tweet"),
    path("<int:pk>/delete", views.delete_tweet, name="delete_tweet")
]
