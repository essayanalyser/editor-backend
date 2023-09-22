from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers                 
from editor_users import views                            

# router = routers.DefaultRouter()                   
# router.register(r'users', views.EditorUsersView.as_view(), 'editor_users')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.EditorUsersView.as_view()),             
    # path('api/users/', views.EditorUsersView.as_view()),             
    path('api/users/<str:title>/', views.EditorUsersView.as_view())             
]