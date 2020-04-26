from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('newpost/', views.new_post, name='new-post'),
    path('postdetail/<str:pk>/', views.post_detail, name='post-detail'),
    path('update/<str:pk>/', views.update_post, name='post-update'),
    path('delete/<str:pk>/', views.delete_post, name='post-delete'),
    path('myposts', views.my_post, name='post-my'),

    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update')
]

