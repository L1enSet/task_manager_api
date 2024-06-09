from rest_framework.routers import SimpleRouter
from .views import TaskApiView

router = SimpleRouter()
router.register('task', TaskApiView, basename='task')

urlpatterns = router.urls