from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register("products-v2", ProductViewSet, basename="products")

urlpatterns = router.urls
