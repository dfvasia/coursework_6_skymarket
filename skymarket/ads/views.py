from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer
from users.models import User


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'retrieve': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'perform_update': [IsAuthenticated],
                                    'destroy': [IsAuthenticated],
                                    }

    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):

        adv_title = request.GET.get('title', None)
        adv_comment = request.GET.get('comment', None)

        if adv_title:
            self.queryset = self.queryset.filter(
                title__icontains=adv_title
            )
        if adv_comment:
            self.queryset = self.queryset.filter(
                author__comment__ad_id__in=User.objects.filter(name__icontains=adv_comment).get().pk
            )
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class AdMeViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'retrieve': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'perform_update': [IsAuthenticated],
                                    'destroy': [IsAuthenticated],
                                    }

    def list(self, request, *args, **kwargs):
        adv_user = request.user.pk
        self.queryset = self.queryset.filter(
            author_id=adv_user)

        return super().list(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

