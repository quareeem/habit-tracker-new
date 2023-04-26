from datetime import timedelta
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from mainapp import models


def get_consecutive_days(date_list):
    """
    Given a list of dates, returns the number of consecutive days in the list.
    """
    if not date_list:
        return 0

    max_streak = 1
    current_streak = 1

    for i in range(1, len(date_list)):
        if date_list[i] == date_list[i-1] + timedelta(days=1):
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 1
    return max(max_streak, current_streak)



class HabitTypeSerializer(ModelSerializer):
    class Meta:
        model = models.HabitType
        fields = ['id', 'title']


class HabitSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    habit_type = serializers.SlugRelatedField(read_only=False, slug_field='title', queryset=models.HabitType.objects.all())
    
    class Meta:
        model = models.Habit
        fields = '__all__'


class HabitRecordSerializer(ModelSerializer):
    user = serializers.SerializerMethodField()
    goal_streak = serializers.SerializerMethodField()
    goal_count_unit = serializers.SerializerMethodField()

    class Meta:
        model = models.HabitRecord
        fields = ['user', 'habit', 'date', 'goal_done', 'goal_streak', 'goal_count_unit']


    def get_user(self, obj):
        qs = models.Habit.objects.filter(user=obj.habit.user)
        user = get_object_or_404(qs)
        return str(user.user)

    def get_goal_streak(self, obj):    
        habit_records = models.HabitRecord.objects.filter(habit=obj.habit).order_by('-date')
        date_list = [record.date for record in habit_records]
        streak = get_consecutive_days(date_list)
        return streak
    
    def get_goal_count_unit(self, obj):
        habit = models.Habit.objects.get(goal_count_unit=obj.habit.goal_count_unit)
        return habit.goal_count_unit
