from django.urls import path
from .views import PostListView, PostDetailView, RepuPostListView, RepuPostDetailView

app_name='posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('republicas', RepuPostListView.as_view(), name='repuList'),
    path('republicas/<slug:slug>/', RepuPostDetailView.as_view(), name='repuDetail'),
]