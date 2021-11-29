from . import views
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    ############ board ##########
    path('', views.home, name="home"),
    path('board/', views.Boardapi.as_view(), name="board"),
    path('board/<int:pk>/', views.Boardcommentapi_detail.as_view(), name="board_detail"),
    path('board/write/', views.Boardapi_writeview, name="board_write"),
    path('board/insert/', views.Boardapi_insert.as_view(), name="board_insert"),
    path('board/<int:pk>/update/', views.Boardapi_update.as_view(), name="board_update"),
    path('board/<int:pk>/delete/', views.Boardapi_delete.as_view(), name="board_delete"),
    
    ########## comment #########
    path('board/<int:pk>/comment/<int:id>/delete/', views.Commentapi_delete.as_view(), name="comment_delete"),
    path('board/<int:pk>/comment/<int:id>/update/', views.Commentapi_update.as_view(), name="comment_update"),
    
    ########## login ############
    path('accounts/login/', views.Login, name="loginview"),
    path('accouts/logout/', views.Logout, name="logoutview"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignupView.as_view(), name="signup"),

    #test
    # path('test11/<int:pk>/', views.xptmxm.as_view(), name="test1"),
    # path('test22/<int:pk>/', views.test2.as_view(), name="test2")

]