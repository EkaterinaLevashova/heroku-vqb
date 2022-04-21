from django.urls import path
from blog.views import *

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('about/', AboutView.as_view(), name='about'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', DraftListView.as_view(template_name='blog/post_draft_list.html'), name='post_draft_list'),
    path('post/<int:pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),
]

