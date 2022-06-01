from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    re_path(r"^api/token/", views.TokenObtainPairView.as_view(), name="jwt-create"),
    re_path(r"^jwt/refresh/?", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path(r"^jwt/verify/?", views.TokenVerifyView.as_view(), name="jwt-verify"),
    path('api/ads/', include('ads.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
