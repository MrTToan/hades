from django.urls import path
from fraud_score import views

urlpatterns = [
    path('test/', views.predict_score),
    # path('snippets/<int:pk>/', views.snippet_detail),
]