from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('users/<int:pk>/', UserDetail.as_view()),
    path('users', UserList.as_view()),
    path('session', Session.as_view()),
    path('register', Register.as_view()),
    path('puns/<int:pk>/', PunDetail.as_view()),
    path('puns', PunList.as_view()),
    path('calls/<int:pk>/', CallDetail.as_view()),
    path('calls', CallList.as_view()),
    path('deceased/<int:pk>/', DeceasedDetail.as_view()),
    path('deceased', DeceasedList.as_view()),
    path('', include(router.urls)),
]
