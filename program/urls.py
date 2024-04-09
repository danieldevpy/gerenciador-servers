from django.urls import path
from program import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reload', views.reload, name='reload'),
    path('stopall', views.stop_all, name="stop_all"),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('start/<int:pk>', views.start, name='start'),
    path('stop/<int:pk>', views.stop, name='stop'),
    path('install/<int:pk>', views.install, name='install'),
    path('uninstall/<int:pk>', views.uninstall, name='uninstall'),
    path('git/<str:command>/<int:pk>', views.git, name='git'),
    path('notification/delete/<int:pk>', views.remove_notification, name='remove_notification')
]
 