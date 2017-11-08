from django.urls import path
from general.views import myfunc1, myfunc, myfunc2, myfunc3, myfunc4


urlpatterns = [
    path('one/', myfunc),
    path('two/', myfunc1),
    path('three/', myfunc2),
    path('four/', myfunc3),
    path('five/',myfunc4),
]