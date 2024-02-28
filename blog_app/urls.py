from django.urls import path
from blog_app.views import *


urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-details'),
    path('author/', AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetails.as_view(), name='author-details'),
    path('comment/<int:post_id>', CommentDetails.as_view(), name='comment-details'),
]
# path('comment/', CommentList.as_view(), name='comment-list'),
