from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class PostType(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Post(models.Model):
    #标题
    title = models.CharField(max_length = 100)
    def __str__(self):
        return self.title
    #正文
    body = models.TextField()
    #创建时间和修改时间
    created_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    #文章类型
    post_type = models.ForeignKey(PostType)
    type_src = models.CharField(max_length = 100, blank = True)
    #文章摘要
    excerpt = models.CharField(max_length = 200, blank = True)
    #分类和标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank = True)
    #作者
    author = models.ForeignKey(User)
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs = {'category' : self.category.name,
                                                'title' : self.title
                                                })
