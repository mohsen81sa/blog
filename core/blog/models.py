from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

#get-user-model
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نشر دهنده')
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

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name    