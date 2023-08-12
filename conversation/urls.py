from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:conversation_id>/', views.detail, name='detail'),
    path('new/<int:item_id>/', views.new_conversation, name='new'),
]
