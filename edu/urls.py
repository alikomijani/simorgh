from . import views
from django.conf.urls import url, include, handler404
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    url(r'^register/$', auth_views.LoginView.as_view(template_name='register/login.html'), name='register'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^password_reset/$',
        auth_views.PasswordResetView.as_view(template_name='register/password_reset_form.html'),
        name='password_reset'),
    url(r'^password_reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^$', views.index, name="dashboard"),

]
# student_course
urlpatterns += [
    url(r'^student_course/list/(?P<pk>[0-9]+)$', views.StudentCourseListView.as_view(), name='StudentCourseListView'),
]
# student
urlpatterns += [
    url(r'^student/create/$', views.StudentCreateView.as_view(), name='StudentCreateView'),
    url(r'^student/list/$', views.StudentListView.as_view(), name='StudentListView'),
    url(r'^student/detail/(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='StudentDetail'),
    url(r'^student/edit/(?P<pk>[0-9]+)/$', views.StudentUpdateView.as_view(), name='StudentEdit'),
]
# User url
urlpatterns += [
    url(r'^user/list/$', views.UserListView.as_view(), name='UserListView'),
    url(r'^user/edit/(?P<pk>[0-9]+)/$', views.UserEditView.as_view(), name='UserEditView'),
    url(r'^user/detail/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='UserDetailView'),
    url(r'^user/create/$', views.UserCreateView.as_view(), name='UserCreateView'),
]
# Teacher urls
urlpatterns += [
    url(r'^teacher/create/$', views.TeacherCreateView.as_view(), name='TeacherCreateView'),
    url(r'^teacher/list/$', views.TeacherListView.as_view(), name='TeacherListView'),
    url(r'^teacher/detail/(?P<pk>[0-9]+)/$', views.TeacherDetailView.as_view(), name='TeacherDetail'),
    url(r'^teacher/edit/(?P<pk>[0-9]+)/$', views.TeacherUpdateView.as_view(), name='TeacherEdit'),
]
# TeacherCourseClass urls
urlpatterns += [
    url(r'^class/List/$', views.TeacherClassCourseListView.as_view(), name='TeacherClassCourseList'),
    url(r'^class/details/(?P<pk>[0-9]+)/$', views.TeacherClassCourseDetailView.as_view(),
        name='TeacherClassCourseDetails'),
    url(r'^class/create/$', views.TeacherClassCourseCreateView.as_view(), name='TeacherClassCourseCreate'),
    url(r'^class/edit/(?P<pk>[0-9]+)/$', views.TeacherClassCourseUpdateView.as_view(), name='TeacherClassCourseEdit'),
]

# Course
urlpatterns += [
    url(r'^course/List/$', views.CourseList.as_view(), name='CourseList'),
    url(r'^course/details/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view(), name='CourseDetail'),
    url(r'^course/create/$', views.CourseCreate.as_view(), name='CourseCreate'),
    url(r'^course/edit/(?P<pk>[0-9]+)/$', views.CourseUpdate.as_view(), name='CourseUpdate'),
]
# Classrooms
urlpatterns += [
    url(r'^classroom/List/$', views.ClassroomList.as_view(), name='ClassroomList'),
    url(r'^classroom/student/details/(?P<pk>[0-9]+)/$', views.ClassroomStudentDetail.as_view(),
        name='ClassroomStudentDetail'),
    url(r'^classroom/course/details/(?P<pk>[0-9]+)/$', views.ClassroomCourseDetail.as_view(),
        name='ClassroomCourseDetail'),
    url(r'^classroom/create/$', views.ClassroomCreate.as_view(), name='ClassroomCreate'),
    url(r'^classroom/edit/(?P<pk>[0-9]+)/$', views.ClassroomUpdate.as_view(), name='ClassroomUpdate'),
]

# Register
urlpatterns += [
    url(r'^register/List/$', views.RegisterList.as_view(), name='RegisterList'),
    url(r'^register/details/(?P<pk>[0-9]+)/$', views.RegisterDetail.as_view(), name='RegisterDetail'),
    url(r'^register/create/$', views.RegisterCreate.as_view(), name='RegisterCreate'),
    url(r'^register/edit/(?P<pk>[0-9]+)/$', views.RegisterUpdate.as_view(), name='RegisterUpdate'),
]
# class time
urlpatterns += [
    url(r'^first_setup/$', views.first_setup, name='first_setup'),
]
