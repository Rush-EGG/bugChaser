from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32)
    # EmailField会有正则表达式进行判断，看用户输入的是否是邮箱格式
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    # 但是对手机号的格式验证必须要自己来添加，添加在ModelForm中
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    # 虽然一般的注册页面会要求重复输入密码以来确保，但为了防止数据库数据冗余，所以可以在ModelForm中添加一个字段，这个字段是不会加入到数据库中的
    password = models.CharField(verbose_name='密码', max_length=32)
