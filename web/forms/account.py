
from django import forms
from django.core.validators import RegexValidator
from web import models


class RegisterModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入%s' % field.label

    class Meta:
        model = models.UserInfo
        fields = ['username', 'email', 'mobile_phone', 'code', 'password', 'confrim_password']

    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])

    password = forms.CharField(widget=forms.PasswordInput(), label='密码')
    confrim_password = forms.CharField(widget=forms.PasswordInput(), label='重复密码')

    code = forms.CharField(label='验证码')

