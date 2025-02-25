from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

#get-user-model
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,verbose_name = 'عکس')
    title = models.CharField(max_length=255,verbose_name ="موضوع")
    content = models.TextField(max_length=255,verbose_name ='کانتنت')
    status = models.BooleanField(verbose_name = "در حال پست ")
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,verbose_name = 'بخش')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = 'ساخت انتشار')
    update_date = models.DateTimeField(auto_now=True,verbose_name = 'آپدیت انتشار')
    published_date = models.DateTimeField(verbose_name = 'تاریخ انتشار')

    class Meta:
        verbose_name = "پست ها"
        verbose_name_plural = "افزودن پست"
        
    def __str__(self):
        return self.title 
    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})
    
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name    