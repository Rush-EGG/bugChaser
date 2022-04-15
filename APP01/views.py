from django.shortcuts import render

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
