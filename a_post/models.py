from django.contrib.auth.models import User
from django.db import models
import uuid

class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True , related_name='posts')
    image = models.URLField(max_length=500)
    body = models.TextField(max_length=500)
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(blank=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    


    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created']


class LikedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} : {self.post.title}'



class Tag(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField( null=True, blank=True)
    slug = models.SlugField(max_length=20, unique=True)


    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    likes =models.ManyToManyField(User,related_name='likescomments', through='LikedComments')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'

    class Meta:
        ordering = ['-created']


class LikedComments(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.comment.body[:20]}'

        #test3@gmail.com
        #ilovepython.

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="replies")
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key = True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[:30]}'

    class Meta:
        ordering = ['created']


class Routes(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=400)

class Image(models.Model):
    image = models.ImageField(upload_to='pic/')


