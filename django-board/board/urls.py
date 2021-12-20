from . import views
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('', views.home, name="home"),
    path('board/', views.board.as_view(), name="board"),
    path('board/<int:pk>/', views.board_detail.as_view(), name="board_detail"),
    path('board_write/', views.board_write, name="board_write"),
    path('board_insert', views.board_insert.as_view(), name="board_insert"),
    path('board_edit/', views.board_edit, name="board_edit"),
    path('board_update/', views.board_update, name="board_update"),
    path('board_delete/', views.board_delete, name="board_delete"),

    ####### comment #########
    path('board/comment/<int:pk>/update/', views.comment_update.as_view(), name="comment_update"),
    path('board/comment/<int:pk>/delete/', views.comment_delete.as_view(), name="comment_delete"),
    # path('board/<int:pk>/comment/<int:id>/delete/', views.comment_delete.as_view(), name="comment_delete"),
    # path('board/<int:Board_id>/comment/<int:id>/delete/', views.comment_delete.as_view(), name="comment_delete"),
    # path('board/<int:pk>/comment/<int:id>/update/', views.comment_update, name="comment_update"),
    # path('board/comment/delete/', views.comment_delete, name="comment_delete"),
]
