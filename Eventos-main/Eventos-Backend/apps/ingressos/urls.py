from rest_framework.routers import DefaultRouter
from .views import IngressoViewSet

router = DefaultRouter()
router.register(r'ingressos', IngressoViewSet, basename='ingresso')

urlpatterns = router.urls
