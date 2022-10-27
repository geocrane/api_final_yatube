from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post(),
        )

    def get_queryset(self):
        return self.get_post().comments

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get("post_id"))


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        if self.request.user == User.objects.get(
            username=self.request.data["following"]
        ):
            raise serializers.ValidationError("Подписка на самого себя")
        serializer.save(user=self.request.user)

    def get_queryset(self):
        followers = get_object_or_404(User, id=self.request.user.id).follower
        search_name = self.request.query_params.get("search")
        if search_name is not None:
            return followers.filter(following__username=search_name)
        return followers
