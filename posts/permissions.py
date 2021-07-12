"""Post permissions class"""

from rest_framework.permissions import BasePermission

from posts.models import Author, Post

class IsAuthor(BasePermission):

    def has_object_permission(self,request,view,obj):
        
        try:
            Author.objects.get(
                author=request.user, 
                post= Post.objects.get(pk=obj.pk)
            )
        except Author.DoesNotExist:
            return False

        return True