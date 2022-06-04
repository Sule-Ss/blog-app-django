from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    (None, 'Choose...'),
    ('Technology','Technology'),
    ('Software','Software'),
    ('Business','Business'),
    ('Fashion','Fashion'),
    ('Lifestyle','Lifestyle'),
    ('Travel','Travel'),
    ('Food','Food'),
)

STATUS =(
    (None,'status'),
    ('published','published'),
    ('draft','draft'),
)

class Blog(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    image= models.URLField( default= "default.jpg")
    category= models.CharField(choices=CATEGORY, blank=True, max_length=200)
    status= models.CharField(choices=STATUS, max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    publish_date=models.DateTimeField(auto_now_add=True)
    last_update=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def get_comment_count(self):
        comments = Comment.objects.all()
        return comments.count()

    def get_view_count(self):
        return BlogView.objects.filter(blog=self).count()

    def get_like_count(self):
        return Favorite.objects.filter(blog=self).count()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_added']


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites' , on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='favorites' , on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

class BlogView(models.Model):
    time_stamp = models.DateTimeField(auto_now=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.user