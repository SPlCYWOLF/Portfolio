from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),                       # 회원가입
    path('api-token-auth/', obtain_jwt_token),           # jwt_token_발급
    path('<str:username>/', views.profile),              # 내 프로필


    # path('login/', views.login),                       # 로그인 [Client]
    # path('logout/', views.logout),                     # 로그아웃 [Client]
    # path('delete/', views.delete, name='delete'),      # 회원탈퇴 [보류]
    # path('update/', views.update),                     # 회원정보수정 [보류]
    # path('password/', views.change_password),          # 비밀번호 수정 [보류]
]
