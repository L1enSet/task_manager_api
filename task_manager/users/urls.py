from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import GetUserApi

router = SimpleRouter()
router.register(r'user', GetUserApi)


urlpatterns = router.urls