from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


Gender_Choices = (
    ('male', '男'),
    ('female', '女')
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='呢称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=Gender_Choices)
    address = models.CharField(max_length=100, verbose_name="地址", default='')
    mobile = models.CharField(max_length=11,  verbose_name='手机号码')
    image = models.ImageField(upload_to='head_image/%Y/%m', default='head_image/default.jpg',verbose_name='用户头像')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class BaseModel(models.Model):#建立基础模型
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:#不生成表
        abstract=True