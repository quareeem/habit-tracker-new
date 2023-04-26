from django.urls import path, include
from rest_framework import routers
from mainapp import views

router = routers.DefaultRouter()
router.register('habit-types', views.HabitTypeViewSet)
router.register('habits', views.HabitViewSet)
router.register('habit-records', views.HabitRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
