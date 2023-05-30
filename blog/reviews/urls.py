from rest_framework import routers

from .views import CommentViewSet, FavoriteViewSet


router = routers.DefaultRouter()
router.register('comment', CommentViewSet, 'comment')
router.register('favorite', FavoriteViewSet, 'favorite')

urlpatterns = router.urls
