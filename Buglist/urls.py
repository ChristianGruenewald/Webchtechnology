from django.urls import path

from Buglist.views import index, EnterNewBug, addNewBug, ChangeBug, ProcessChangedBug, DeleteBug
urlpatterns = [
    path('index', index),
    path('NewBug/',EnterNewBug),
    path('addNewBug/',addNewBug), 
    path('ChangeBug',ChangeBug), 
    path('ProcessChangeBug', ProcessChangedBug),
    path('Deletebug', DeleteBug),
]