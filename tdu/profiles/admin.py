from django.contrib import admin
from .models import UserProfile #UserProfileモデルをインポート


admin.site.register(UserProfile) #モデルをadminページで見るにはこれで登録
