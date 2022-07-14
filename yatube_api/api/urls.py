from django.urls import include, path
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [path('api-token-auth/', views.obtain_auth_token),
               path('admin/', admin.site.urls),
               path('', include(router.urls))]
