from rest_framework import generics
from blog_app.models import User, Blog, Comment
from .serializers import BlogSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

# class UserListView(generics.ListAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
    
class UserBlogListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        user = self.kwargs['pk']
        try:
            user_object = User.objects.get(username=user)
        except User.DoesNotExist:
            raise ValidationError({'status':"No User with specified name found"})
        return Blog.objects.filter(user=user_object)
    
class BlogsCreateView(generics.CreateAPIView):
    serializer_class = BlogSerializer
    
    def perform_create(self,serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            pass
        
class BlogsListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
# class UserCreateView(generics.CreateAPIView):
#     serializer_class = UserSerializer
    
        
    
    