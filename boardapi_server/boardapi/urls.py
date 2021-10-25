from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'board', views.BoardViewSet, basename="board")

urlpatterns = [
    # path('', include(router.urls)),
    # path('board', views.BoardViewSetAsView, name='Board'),


    # path('', views.BoardListView.as_view(), name='Board'),
    path('boardapi/', views.BoardListView.as_view(), name='BoardListView'),
    path('boardapi/<int:pk>/', views.BoardDetailView.as_view(), name='BoardDetailView'),
    path('boardapi/create/', views.BoardCreateView.as_view(), name='BoardCreateView'),
    path('boardapi/<int:pk>/update/', views.BoardUpdateView.as_view(), name='BoardUpdateView'),
    path('boardapi/<int:pk>/delete/', views.BoardDeleteView.as_view(), name='BoardDeleteView'),

    ######### comment  ##########

    # path('boardapi/<int:board_pk>/comment/', views.CommentListView.as_view(), name='CommentListView'),
    # path('boardapi/<int:board_pk>/comment/create/', views.CommentCreateView.as_view(), name='CommentCreateView'),
    # path('boardapi/<int:board_pk>/comment/', views.comment_list_create, name='CommentListView'),
    path('boardapi/<int:board_pk>/comment/<int:pk>/delete/', views.CommentUpdateDeleteView.as_view(), name='CommentDeleteView'),
    path('boardapi/<int:board_pk>/comment/<int:pk>/update/', views.CommentUpdateDeleteView.as_view(), name='CommentUpdateView'),

    path('boardapi/<int:board_pk>/comment/', views.CommentListCreateView.as_view(), name='CommentListCreateView'),
    # path('boardapi/<int:board_pk>/comment/create/', views.CommentListCreateView.as_view(), name='CommentCreateView'),


    ###### account ########
    # path('account/login/', views.signup, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)