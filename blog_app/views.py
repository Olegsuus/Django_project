from rest_framework import generics, mixins
from .models import Post, Author, Comment
from .serializers import PostSerializer, AuthorSerializer, CommentSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CommentDetails(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        queryset = Comment.objects.filter(post_id=post_id)
        return queryset


class CommentList(
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin
                  ):

    serializer_class = CommentSerializer



# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

    # @action(methods=['get'], detail=False)
    # def author(self, request):
    #     auth = Author.objects.all()
    #     return Response({'author': [c.name for c in auth]})


# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
