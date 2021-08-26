from django.urls import path
from . views import detail, index

app_name = 'polls'

urlpatterns = [
    path('details/<int:question_id>/', view=detail, name='details'),
]
