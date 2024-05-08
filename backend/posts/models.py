from django.db import models
from accounts.models import User



class Posts(models.Model):
    content=models.TextField(max_length=1000,blank=False,null=False)
    author=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    dateCreated=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.id



class Comments(models.Model):
    content=models.CharField(max_length=255,blank=False,null=False)
    postId=models.ForeignKey(Posts, on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    dateTimeCreated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
    


class Likes(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    postId=models.ForeignKey(Posts, on_delete=models.CASCADE,related_name='likes')


    def __str__(self):
        return self.id
    
