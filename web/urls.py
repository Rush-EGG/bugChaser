from django.conf.urls import url

from web.views import account

urlpatterns = [
    url(r'^register/$', account.register, name='register'),  # 直接通过register来反向解析
]
