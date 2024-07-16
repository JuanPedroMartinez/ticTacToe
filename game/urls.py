from django.urls import path

from game import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('new_game/', views.new_game, name='new_game'),
    path('play/<int:game_id>/', views.play, name='play'),
    path('board/<int:game_id>/', views.board, name='board'),

]
