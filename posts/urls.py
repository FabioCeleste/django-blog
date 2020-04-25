from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('newpost/', views.new_post, name='new-post'),
    path('postdetail/<str:pk>/', views.post_detail, name='post-detail'),

    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update')
]

