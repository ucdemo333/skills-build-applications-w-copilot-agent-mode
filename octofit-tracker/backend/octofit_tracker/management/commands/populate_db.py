from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # 清空資料
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 建立隊伍
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # 建立使用者
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # 建立活動
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=captain, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=batman, type='swim', duration=60, calories=500)
        Activity.objects.create(user=superman, type='run', duration=50, calories=450)

        # 建立運動
        Workout.objects.create(name='Pushups', description='Standard pushups', difficulty='Easy')
        Workout.objects.create(name='Pullups', description='Standard pullups', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Bodyweight squats', difficulty='Easy')

        # 建立排行榜
        Leaderboard.objects.create(user=ironman, score=1000)
        Leaderboard.objects.create(user=captain, score=900)
        Leaderboard.objects.create(user=batman, score=950)
        Leaderboard.objects.create(user=superman, score=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db 已成功填充測試資料'))
