from django.urls import include, path

# TODO настройка роутов для модели
from rest_framework import routers

from ads.views import AdViewSet, AdMeViewSet

router = routers.SimpleRouter()
router.register('', AdViewSet)


urlpatterns = [
    path('create/', AdViewSet.as_view({'post': 'create'})),
    path('me/', AdMeViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),

    # path('<int:pk>/upload_image/', AdsImageUpdateView.as_view()),
    ]