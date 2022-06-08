from django.urls import path

from . import views

# urls for diferent purposes
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_index_list, name='list'),  # show tos stories index list.
    path('index/', views.get_story_by_index, name='index'), # show 'title' and 'id' and save them in cache indexes by id
    path('redis_health/', views.redis_healthcheck, name='redis_health'),  #check status of redis server, show data keys in memory
]