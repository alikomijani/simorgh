from django.conf.urls import url
from . import views

urlpatterns = [  # ex: /polls/5/
    url(r'^(?P<class_id>[0-9]+)/$', views.get_class_students, name='get_class_students'),
]
