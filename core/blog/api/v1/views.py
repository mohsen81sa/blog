from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly , IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .sreializers import PostSerializer
from rest_framework.views import APIView
from ...models import Post
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
class PostList(APIView):
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