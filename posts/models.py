from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

"""
=> models.Cascade 

When the referenced object is deleted, also delete the objects that have references to it 
(when you remove a blog post for instance, you might want to delete comments as well).


=> auto_now 

fields are updated to the current timestamp every time an object is saved 
and are therefore perfect for tracking when an object was last modified, 

=> auto_now_add 

field is saved as the current timestamp when a row is first added to the database, 
and is therefore perfect for tracking when it was created.
"""