from rest_framework.routers import SimpleRouter
from .views import DailyListApiView, TaskApiView

router = SimpleRouter()
router.register('daily', DailyListApiView)
router.register('task', TaskApiView)

urlpatterns = router.urls