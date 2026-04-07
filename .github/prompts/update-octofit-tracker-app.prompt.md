mode: 'agent'
model: GPT-4.1

# Django應用程式更新(Django App Updates)
- 所有Django專案檔案都位於octofit-tracker/backend/octofit_tracker目錄中。
1.更新settings.py以設定MongoDB連線(connection)與跨來源資源共享(CORS, Cross-Origin Resource Sharing)。
2.更新models.py、serializers.py、urls.py、views.py、tests.py與admin.py，以支援使用者(users)、團隊(teams)、活動(activities)、排行榜(leaderboard)與訓練(workouts)集合(collections)
3.確保/路徑指向API(api)，並且在urls.py中包含api_root
