from django.db import models

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
    ('status','status'),
)

class Blog(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    image= models.ImageField(upload_to = "blogImg/", default= "default.jpg")
    category= models.CharField(choices=CATEGORY, blank=True, max_length=200)
    status= models.CharField(choices=STATUS, max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
