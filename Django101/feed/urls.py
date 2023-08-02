from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView
app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    # pk = primary key (it's an ID)
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='post'),
]

