from django.urls import path
from none_db.views import mysite, mysite1, mysite2, mysite3, mysite4


urlpatterns = [
    path('', mysite),
    path('one/', mysite1),
    path('two/', mysite2),
    path('free/', mysite3),
    path('four/', mysite4),
]