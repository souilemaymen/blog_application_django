from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path("", views.PostList, name="post_list"),
    #path("<int:id>/", views.detailList, name="post_detail")
    path("<slug:slug>/", views.detailList, name="post_detail"),
    ]