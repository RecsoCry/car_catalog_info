from django.urls import path
from .views import index, get_models

urlpatterns = [
    path('', index, name='index'),
    path('models/<int:carmake_id>/', get_models, name='models'),
]
