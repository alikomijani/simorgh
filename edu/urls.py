from django.conf.urls import url
from . import views

urlpatterns = [  # ex: /polls/5/
    url(r'^(?P<class_id>[0-9]+)/$', views.get_class_students, name='get_class_students'),
    url(r'^register/$', views.FormRegisterStudent.as_view(), name='registerstudent'),
    url(r'^student/list/$', views.StudentListView.as_view(), name='StudentListView'),
    url(r'^student/detail/(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='StudentDetail'),
    url(r'^student/edit/(?P<pk>[0-9]+)/$', views.StudentUpdateView.as_view(), name='StudentEdit')
]
