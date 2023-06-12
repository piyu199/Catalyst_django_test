from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('file_upload',views.file_upload,name='file_upload'),
    path('logout',views.logout,name='logout'),
    path('display_user',views.display_user,name='display_user'),
    path('query_builder',views.query_builder,name='query_builder'),
]