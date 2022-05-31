from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework import routers
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

users_router = routers.SimpleRouter()
users_router.register("", UserViewSet, basename="users")

urlpatterns = [

]
urlpatterns += users_router.urls
