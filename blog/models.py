from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='user_post_fk')
    title = models.CharField(max_length=50, verbose_name='Tile')
    content = models.TextField(verbose_name='Description', null=True, blank=True)
    tech_used = models.CharField(verbose_name='Technology used', max_length=40, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    date_posted = models.DateTimeField(auto_now_add=True)
    repo = models.CharField(max_length=85, verbose_name='Repository', null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} - {self.title.title()}'

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'


class Album(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_albums_fk')
    photos = models.ImageField(upload_to='images/albums')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title} - Album'

    class Meta:
        verbose_name = 'Albums'
        verbose_name_plural = 'Albums'
