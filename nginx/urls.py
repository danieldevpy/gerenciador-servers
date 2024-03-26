from django.urls import path
from nginx import views

urlpatterns = [
    path('', views.get_text),
    path('rewrite', views.re_write, name="rewrite")
]
