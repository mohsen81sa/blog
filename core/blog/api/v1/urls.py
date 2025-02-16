from django.urls import path,include
from . import views
app_name = "blog"

urlpatterns = [
    # path("post/",views.post_list,name="post_list"),
    # path("post/<int:id>/",views.post_detaile,name="post_detaile"),
    path("post/",views.PostList.as_view(),name="post-list"),
    path("post/<int:id>/",views.PostDetail.as_view(),name="post-detaile"),

]