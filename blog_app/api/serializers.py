from blog_app.models import Blog, Comment
from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = '__all__'
        
#     def create(self, validated_data):

#         user = User.objects.create(
#             username=validated_data['username'],
#             password=validated_data['password'],
#             name=validated_data['name'],
#             age=validated_data['age'],
#             address=validated_data['address']
#         )

        # return user
        
class BlogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'