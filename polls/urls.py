
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from . import views

urlpatterns = [
    # # ex: /polls/
    # url(r'^$', views.index, name = 'index'),
    # # ex: /polls/5/
    # #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^details/(?P<question_id>[0-9]+)/$', views.detail, name = 'detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = 'results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = "vote"),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/vote/$', views.vote, name = 'vote'),


]
"""
Regex (biểu thức chính quy) là một chủ đề khá lớn, Regex cho phép chúng ta tạo ra các mẫu định dạng text dùng trong tìm kiếm, xác thực… ở đây Regex giúp tạo các đường dẫn tới các hàm trả về nội dung HTML một cách tự động. Để tạo các chuỗi Regex thì có một số quy luật sau đây:

^ – bắt đầu regex
$ – kết thúc regex
\d – một kí tự số
+ –  kí tự phía trước có thể lặp lại một hoặc nhiều lần
/ – có một dấu /
() – gom nhóm một số kí tự nhất định lại với nhau
"""

