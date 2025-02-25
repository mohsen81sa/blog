from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


app_name = "api-v1"


router = DefaultRouter()
router.register('post',views.PostListViewSet, basename='post')
router.register('category',views.CategoryViewSet, basename='category')
urlpatterns = router.urls


# urlpatterns = [
#     # path("post/",views.post_list,name="post_list"),
#     # path("post/<int:id>/",views.post_detaile,name="post_detaile"),
#     path("post/",views.PostList.as_view(),name="post-list"),
#     path("post/<int:pk>/",views.PostDetail.as_view(),name="post-detaile"),

# ]