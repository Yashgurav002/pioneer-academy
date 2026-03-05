from rest_framework.routers import DefaultRouter
from .views import CoachProfileViewSet

router = DefaultRouter()
router.register(r'coaches', CoachProfileViewSet, basename='coaches')

urlpatterns = router.urls