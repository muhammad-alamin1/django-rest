from django.urls import path, include
from .views import Information, LoginView, SomeProtectedView

# create urls (bruass)
urlpatterns = [
    path('info/', Information.as_view(), name='teachers_info'),
    path('info/<int:pk>', Information.as_view(), name='teacher_info'),
    path('bruass/teacher/create/', Information.as_view(), name='teacher_create'),
    
]
