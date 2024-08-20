from rest_framework import routers
from .api import personaViewSet

router = routers.DefaultRouter()

router.register('api/personas', personaViewSet,'personas')

urlpatterns = router.urls