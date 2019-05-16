from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login,{'template_name':'edu/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name':'edu/login.html'}, name='logout'),
    url(r'^register/$',auth_views.login,{'template_name':'edu/login.html'}, name='register'),
    url(r'^password_reset/$', auth_views.login,{'template_name':'edu/login.html'}, name='password_reset'),
    url(r'^(?P<class_id>[0-9]+)/$', views.get_class_students, name='get_class_students'),
    url(r'^student/create/$', views.StudentCreateView.as_view(), name='StudentCreateView'),
    url(r'^student/list/$', views.StudentListView.as_view(), name='StudentListView'),
    url(r'^user/list/$', views.UserListView.as_view(), name='UserListView'),
    url(r'^student/detail/(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='StudentDetail'),
    url(r'^student/edit/(?P<pk>[0-9]+)/$', views.StudentUpdateView.as_view(), name='StudentEdit'),
    url(r'^teacher/create/$', views.TeacherCreateView.as_view(), name='TeacherCreateView'),
    url(r'^teacher/list/$', views.TeacherListView.as_view(), name='TeacherListView'),
    url(r'^teacher/detail/(?P<pk>[0-9]+)/$', views.TeacherDetailView.as_view(), name='TeacherDetail'),
    url(r'^teacher/edit/(?P<pk>[0-9]+)/$', views.TeacherUpdateView.as_view(), name='TeacherEdit'),
    url(r'^student/api/detail/(?P<pk>[0-9]+)/$', views.get_student_rest_api),
    url(r'^student/api/detail/all/$', views.get_all_student_rest_api),
    url(r'^$', views.index,name="dashboard"),

]
