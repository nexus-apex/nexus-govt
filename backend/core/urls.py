from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('govservices/', views.govservice_list, name='govservice_list'),
    path('govservices/create/', views.govservice_create, name='govservice_create'),
    path('govservices/<int:pk>/edit/', views.govservice_edit, name='govservice_edit'),
    path('govservices/<int:pk>/delete/', views.govservice_delete, name='govservice_delete'),
    path('govapplications/', views.govapplication_list, name='govapplication_list'),
    path('govapplications/create/', views.govapplication_create, name='govapplication_create'),
    path('govapplications/<int:pk>/edit/', views.govapplication_edit, name='govapplication_edit'),
    path('govapplications/<int:pk>/delete/', views.govapplication_delete, name='govapplication_delete'),
    path('citizens/', views.citizen_list, name='citizen_list'),
    path('citizens/create/', views.citizen_create, name='citizen_create'),
    path('citizens/<int:pk>/edit/', views.citizen_edit, name='citizen_edit'),
    path('citizens/<int:pk>/delete/', views.citizen_delete, name='citizen_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
