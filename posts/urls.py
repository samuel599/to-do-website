from django.urls import path,include
from .views import PostCreateView,create,PostUpdateView,PostDeleteView,PostDetailView

urlpatterns = [
    path('create/', create, name='create-post'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/',PostUpdateView.as_view(),name='update-post'),
    path('delete/<int:pk>/',PostDeleteView.as_view(template_name='posts/post_delete.html'),name='delete-post'),

]
