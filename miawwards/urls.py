from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('profile/<username>/', views.profile, name='profile'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('project/<post>', views.project, name='project'),
    path('search/', views.search_project, name='search')
]