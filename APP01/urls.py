from django.conf.urls import url
from APP01 import views

urlpatterns = [
    url(r'^send/sms/', views.send_sms),
    url(r'^register/', views.register, name='register'),  # 反向解析时写成"APP01: register"
]
