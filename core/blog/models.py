from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    num = models.CharField(max_length=250)

    def __str__(self):
        return self.num
class Post(models.Model):
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=250)
    content=  models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=timezone.now)  # یا هر تاریخ دلخواه به عنوان مقدار پیش‌فرض


    def __str__(self):
        return self.title
