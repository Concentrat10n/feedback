from django.contrib import admin
from django.urls import path
from .views import FeedBackView, FeedBackUpdateView, DoneView

urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
]
