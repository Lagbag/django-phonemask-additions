from django.urls import path
from django_phonemask_additions import views

# Маршруты для клиентской части
USER_ROUTES = [
    path('', views.main_page, name='home_page'),
    path('auth/', views.login_user, name='login_page'),
    path('exit/', views.logout_user, name='logout'),
    path('pass/reset/', views.update_password, name='password_change'),
    path('data/check/', views.validate_data, name='validation'),
]

ADMIN_ROUTES = [
    path('control/panel/', views.admin_control, name='admin_panel'),
    path('control/register/', views.register_user, name='user_registration'),
    path('control/edit/<int:user_id>/', views.edit_user, name='user_update'),
]

urlpatterns = USER_ROUTES + ADMIN_ROUTES