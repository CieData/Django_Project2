from django.urls import path
from .	import views
urlpatterns =	[
    path('aa/',views.aa_page),
    path('bb/',views.bb_page),
    path('hansua/',views.hansua_page),
    path('jihyun/',views.jihyun_page),
    path('hansua/mbti/',views.mbti_page),
    path('limdoyoung/',views.limdoyoung_page),
    path('',views.index), 
]
