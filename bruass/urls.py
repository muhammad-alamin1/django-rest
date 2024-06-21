from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import Information


# create urls (bruass)
urlpatterns = [
    path('info/', Information.as_view(), name='teachers_info'),
    path('info/<int:pk>', Information.as_view(), name='teacher_info'),
    path('bruass/teacher/create/', Information.as_view(), name='teacher_create'),
    path('bruass/teacher/update/<int:pk>', Information.as_view(), name='teacher_update'),
    path('bruass/teacher/delete/<int:pk>', Information.as_view(), name='teacher_delete'),
]
