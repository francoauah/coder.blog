from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='details'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='delete'),
]