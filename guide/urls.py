from django.urls import path
from guide import views
from django.conf.urls import url, include


app_name = 'guide'
urlpatterns = [
    path('titles/', views.titles),
    path('add_title.html', views.add_title),
    path('edit_title.html', views.edit_title),
    path('del_title.html', views.del_title),
    path('urls/', views.urls),
    path('add_url.html', views.add_url),
    path('edit_url.html', views.edit_url),
    path('del_url.html', views.del_url),
]