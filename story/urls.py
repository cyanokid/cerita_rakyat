from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('show_story/<story_id>', views.show_story, name="show_story"),
    path('add_story', views.add_story, name="add_story"),
    path('my_story', views.my_story, name="my_story"),
    path('delete_story/<story_id>', views.delete_story, name="delete_story"),
    path('show_profile/<int:pk>', views.show_profile, name="show_profile"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('profile_list/', views.profile_list, name="profile_list"),
    path('story_like/<int:pk>', views.story_like, name="story_like"),
    path('story_sad/<int:pk>', views.story_sad, name="story_sad"),
    path('story_laugh/<int:pk>', views.story_laugh, name="story_laugh"),
    path('story_angry/<int:pk>', views.story_angry, name="story_angry"),
    path('story_shock/<int:pk>', views.story_shock, name="story_shock"),
    path('admin_approval', views.admin_approval, name="admin_approval"),
    path('search', views.search, name="search"),
]
