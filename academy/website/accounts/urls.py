from django.urls import path, include, re_path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign-up/', views.sign_up, name='sign_up'),
    re_path(r'^activate/(?P<uidb36>[0-9A-Za-z]+)/(?P<token>.+)/$',
            views.active_account, name='active_account'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    re_path(r'^reset-password/(?P<uidb36>[0-9A-Za-z]+)/(?P<token>.+)/$',
            views.reset_password, name='reset_password'),
    path('trainings/', include('academy.website.accounts.trainings.urls', namespace='trainings')),
    path('survey/', views.survey, name='survey'),
    path('survey/edit/', views.edit_survey, name='edit_survey'),
    re_path(r'^auth-user/(?P<uidb36>[0-9A-Za-z]+)/(?P<token>.+)/$',
            views.auth_user, name='auth_user'),
]
