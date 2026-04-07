from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='pass', team=team)
        self.assertEqual(user.email, 'test@test.com')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, calories=100)
        self.assertEqual(activity.type, 'run')

    def test_workout_create(self):
        workout = Workout.objects.create(name='Pushup', description='desc', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushup')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='test', email='test@test.com', password='pass', team=team)
        lb = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(lb.score, 100)
