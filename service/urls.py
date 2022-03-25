from django.urls import path, include
from service import author_views, post_views, inbox_views, followrequest_views, comment_views, imagepost_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Social Distribution API",
        default_version='v1',
        description="API documentation for our social distribution API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('auth/signup/', author_views.signup, name='signup'),
    path('service/', include([
        # API Docs
        path('docs', schema_view.with_ui('swagger', cache_timeout=0)),

        # Author Endpoints
        path('authors/', author_views.author_list, name='author_list'),
        path('authors/<str:pk>', author_views.author_detail, name='author_detail'),

        # Post Endpoints
        path('authors/<str:author_pk>/posts/<str:post_pk>',
             post_views.post_detail, name='post_detail'),
        path('authors/<str:author_pk>/posts/',
             post_views.posts, name='post_list'),

        #Inbox Endpoint
        path('authors/<str:pk>/inbox', inbox_views.inbox_list, name="inbox_list"),

        # Send Request Endpoints
        path('<str:author_pk>/sendfollowrequest/', followrequest_views.send_request, name='follow_request'),

        # Comment Endpoints
        path('authors/<str:author_pk>/posts/<str:post_pk>/comments',
             comment_views.comments, name='comments'),

        # Image Endpoints
        path('authors/<str:author_pk>/posts/<str:post_pk>/image',
             imagepost_views.imagepost, name='imagepost'),


    ]))
]
