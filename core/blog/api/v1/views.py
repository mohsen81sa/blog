from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly , IsAdminUser
from rest_framework.response import Response
from rest_framework import status,viewsets
from .sreializers import PostSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from ...models import Post,Category
from blog.api.v1.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

""" fbv api """
# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_list(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# @api_view(["GET","PUT","DELETE"])
# @permission_classes([IsAuthenticated])
# def post_detaile(request,id):
#     post = get_object_or_404(Post,pk=id,status=True)
#     if request.method == "GET":
#         serializer = PostSerializer(post)    
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)


# cbv api
"""class PostList(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self,request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""
# cbv detail
"""
class PostDetail(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def get(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)    
        return Response(serializer.data)
    def put(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""

# list api mixin
"""class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=1)
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=1)"""

class PostListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=1)
    
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  