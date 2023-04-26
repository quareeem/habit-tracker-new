from django.contrib import admin

from mainapp.models import Habit, HabitType, HabitRecord


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Habit._meta.fields]
    list_display_links = list_display


@admin.register(HabitType)
class HabitTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(HabitRecord)
class HabitRecordAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HabitRecord._meta.fields]
    list_display_links = list_display

