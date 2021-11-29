from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'board', views.BoardViewSet, basename="board")

urlpatterns = [
    ######### board #########
    # path('', include(router.urls)),
    # path('board', views.BoardViewSetAsView, name='Board'),
    path('boardapi/', views.BoardListCreateAPIView.as_view(), name='BoardListCreateView'),
    path('boardapi/<int:pk>/', views.BoardView.as_view(), name='BoardView'),

    ######### comment  ##########
    path('boardapi/<int:board_pk>/comment/<int:pk>/', views.CommentUpdateDeleteView.as_view(), name='CommentUpdateDeleteView'),
    path('boardapi/<int:board_pk>/comment/', views.CommentListCreateView.as_view(), name='CommentListCreateView'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)