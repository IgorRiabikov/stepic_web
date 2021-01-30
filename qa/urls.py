from django.urls import path

from web.qa.views import test

app_name = 'qa'

urlpatterns = [

    path('', test),
    path('login/', test),
    path('signup/', test),
    path('question/', test),
    path('ask/', test),
    path('popular/', test),
    path('new/', test),
    ]
