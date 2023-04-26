# from django.contrib.auth.models import User
import datetime
from django.db import models

from usersapp.models import CustomUser as User

Admin = User.objects.filter(username='admin')


class HabitType(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.title



class Habit(models.Model):
    CHOICES = (('H', 'Hour'), ('D', 'Day'), ('W', 'Week'), ('M', 'Month'), ('Y', 'Year'))

    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_type = models.ForeignKey(HabitType, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    goal_count = models.IntegerField(default=1)
    goal_count_unit = models.CharField(max_length=50, default="ml")
    goal_rep = models.IntegerField(default=1)
    goal_rep_unit = models.CharField(max_length=50, choices=CHOICES, default='Week')



class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, default=1, related_name="habit_url")
    date = models.DateField(default=datetime.date.today)
    goal_done = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["date", "habit"], name="unique datelog"),
        ]

    def __str__(self):
        return f"Date: {self.date} | Amount: {self.goal_done}"