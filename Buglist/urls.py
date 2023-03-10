from django.urls import path

from Buglist.views import index, EnterNewBug, addNewBug, ChangeBug, ProcessChangedBug, DeleteBug, RedircetToIndex
urlpatterns = [

    path('', RedircetToIndex),
    path('index', index),
    path('NewBug/',EnterNewBug),
    path('addNewBug/',addNewBug), 
    path('ChangeBug',ChangeBug), 
    path('ProcessChangeBug', ProcessChangedBug),
    path('Deletebug', DeleteBug),
]