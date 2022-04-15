from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render
from APP01 import models

# Create your views here.

from django.shortcuts import render, HttpResponse
import random
from utils.tencent.sms import send_sms_single
from django.conf import settings


def send_sms(request):
    """ 发送短信
        ?tpl == login
        ?tpl == register
    """
    template = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(template)
    if not template_id:
        return HttpResponse('模板不存在')

    code = random.randrange(1000, 9999)

    res = send_sms_single('15957278805', template_id, [code, ])
    print(res)

    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        return HttpResponse(res['errmsg'])


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


def register(request):
    form = RegisterModelForm()
    return render(request, 'APP01/register.html', {'form': form})
