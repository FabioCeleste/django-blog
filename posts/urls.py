from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('newpost/', views.new_post, name='new-post'),
    path('postdetail/<str:pk>/', views.post_detail, name='post-detail'),
    path('update/<str:pk>/', views.update_post, name='post-update'),
    path('delete/<str:pk>/', views.delete_post, name='post-delete'),
    path('myposts', views.my_post, name='post-my'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update')
]

