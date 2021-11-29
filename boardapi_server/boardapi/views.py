from .models import Board, Comment
from .serializers import CommentSerializer, BoardSerializer, CommentListSerializer
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# from rest_framework import viewsets
from rest_framework.decorators import api_view


############################### Board ###################################

# class BoardViewSet(viewsets.ModelViewSet):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer

# BoardViewSetAsView = BoardViewSet.as_view({
#     "get": "list",
#     # "post": "create",
# })


# @csrf_exempt
class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.all().order_by('-b_no')
    serializer_class = BoardSerializer


class BoardView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        Board.objects.filter(pk=pk).update(b_count=F('b_count') + 1)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

############################### Comment ##################################


class CommentListCreateView(generics.ListCreateAPIView):
    model = Comment
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer

    def get(self, request, board_pk):
        board = get_object_or_404(Board, pk=board_pk)
        comments = board.comments.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, board_pk):
        queryset = Comment.objects.all()
        board = get_object_or_404(Board, pk=board_pk)
        serializer = CommentSerializer(data=request.data) 
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(Board=board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer