from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',)

# The ability to include/exclude fields in our API this easily is a remarkable feature.
# More often than not, an underlying database model will have far more fields than
# what needs to be exposed