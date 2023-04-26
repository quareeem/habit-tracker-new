from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from mainapp.models import Habit, HabitType, HabitRecord
from mainapp.serializers import HabitSerializer, HabitTypeSerializer, HabitRecordSerializer


class HabitTypeViewSet(viewsets.ModelViewSet):
    queryset = HabitType.objects.all()
    permission_classes = [AllowAny]
    serializer_class = HabitTypeSerializer


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]
    serializer_class = HabitSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class HabitRecordViewSet(viewsets.ModelViewSet):
    queryset = HabitRecord.objects.all()
    permission_classes = [AllowAny]
    serializer_class = HabitRecordSerializer

    # def get_queryset(self):
    #     habit = Habit.objects.filter(user=request.user)
    #     return self.queryset.filter(user=habit.user)

    
    def create(self, request, *args, **kwargs):
        try:
            habit_record = self.get_queryset().get(date=request.data['date'])
        except HabitRecord.DoesNotExist:
            habit_record = None

        if habit_record:
            habit_record.goal_done += request.data['goal_done']
            habit_record.save()
            serializer = self.get_serializer(habit_record)
            return Response(serializer.data)
        return super().create(request, *args, **kwargs)