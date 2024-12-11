from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib.admin.views.decorators import staff_member_required
from .views import (
    home,
    register,
    login_view,
    logout_view,
    dashboard,
    submit_form,
    save_drawing,
    admin_dashboard,
    edit_submission,
    delete_submission,
    export_submissions,
    about,
    report,
    all_time_report,
    weekly_report,
    monthly_report,
    export_report_csv,
    create_password_reset_request,
    approve_password_reset_request,
    activate,
    privacy_policy,
    terms_of_service,
    notifications_view,
    mark_as_read,
    mark_as_unread,
    unread_notifications_count_view  # Add this import
)

urlpatterns = [
    # Public URLs
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-of-service/', terms_of_service, name='terms_of_service'),

    # User Authentication
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Password Reset
    path('password-reset/', PasswordResetView.as_view(template_name='shegarland/password_reset.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='shegarland/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='shegarland/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='shegarland/password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-request/', create_password_reset_request, name='create_password_reset_request'),
    path('approve-password-reset/<int:request_id>/', approve_password_reset_request, name='approve_password_reset_request'),

    # Account Activation
    path('activate/<uidb64>/<token>/', activate, name='activate'),

    # User Dashboard & Forms
    path('dashboard/', dashboard, name='dashboard'),
    path('submit-form/', submit_form, name='submit_form'),
    path('save-drawing/', save_drawing, name='save_drawing'),

    # Admin-Only Views
    path('admin/dashboard/', staff_member_required(admin_dashboard), name='admin_dashboard'),
    path('admin/report/', staff_member_required(report), name='report'),
    path('admin/report/all-time/', all_time_report, name='all_time_report'),
    path('admin/report/weekly/', staff_member_required(weekly_report), name='weekly_report'),
    path('admin/report/monthly/', staff_member_required(monthly_report), name='monthly_report'),
    path('admin/export/report/csv/', export_report_csv, name='export_report_csv'),

    # Submission Management
    path('submission/edit/<int:submission_id>/', edit_submission, name='edit_submission'),
    path('submission/delete/<int:submission_id>/', delete_submission, name='delete_submission'),
    path('submissions/export/', export_submissions, name='export_submissions'),

    # Notifications
    path('notifications/', notifications_view, name='notifications'),
    path('notification/read/<int:notification_id>/', mark_as_read, name='mark_as_read'),
    path('notification/unread/<int:notification_id>/', mark_as_unread, name='mark_as_unread'),

    # Add the unread notifications count endpoint
    path('notifications/unread_count/', unread_notifications_count_view, name='unread_notifications_count'),
]