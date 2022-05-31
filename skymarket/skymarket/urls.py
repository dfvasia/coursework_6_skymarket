from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# TODO здесь необходимо подклюючит нужные нам urls к проекту
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers


urlpatterns = [

    path("admin/", admin.site.urls),
    # path("api/redoc-tasks/", include("redoc.urls")),
    # # path("api-auth/", include("rest_framework.urls")),
    # # path("auth/", include("djoser.urls")),
    path("api/token/", include("djoser.urls.jwt")),
    #
    #
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('users/', include('users.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
