from django.urls import path, include
from .views import Information

# create urls (bruass)
urlpatterns = [
    path('info/', Information.as_view(), name='teachers_info'),
    path('info/<int:pk>', Information.as_view(), name='teacher_info'),
]
