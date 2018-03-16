from django.urls import path

from .views import QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', QuestionViewSet, base_name='questions')
urlpatterns = router.urls