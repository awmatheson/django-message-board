from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.message_board, name='message_board'),
]