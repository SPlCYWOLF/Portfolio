from django.urls import path
from . import views
 
app_name = 'community'

urlpatterns = [
    path('reviews/', views.review_list),                                                            # 전체 리뷰글 조회
    path('movies/<int:movie_pk>/reviews/', views.review_create),                                    # 리뷰글 생성
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail_update_delete),      # 단일 리뷰글 조회/수정/삭제
    path('<int:user_id>/reviews/', views.my_review_list),    # 11/22 Review 모델에서 user 필드값으로 유저의 id 값을 받는것을 확인!                                      # 내 리뷰글 조회

    path('reviews/<int:review_pk>/comments/', views.detail_create_comment),     # 11/22 RESTful 하게 수정 & 댓글 불러오기 추가    # 댓글 생성
    path('reviews/<int:review_pk>/comments/<int:comment_pk>/', views.delete_comment), # 11/22         # 댓글 삭제
]