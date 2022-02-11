from django.urls import path, include
# from .views import MovieAPIView, ActorAPIView
from .views import MovieViewSet, ActorViewSet
from rest_framework.routers import DefaultRouter
from .views import MovieActorAPIView, CommentViewSet
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view()),

    # path('comments/', CommentAPIView.as_view()),
    # path('movies/', MovieAPIView.as_view()),
    # path('actors/', ActorAPIView.as_view()),
    path("auth", views.obtain_auth_token),
]
