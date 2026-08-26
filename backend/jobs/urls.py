from django.urls import path

from .views import JobListView, JobManageDetailView, JobManageListCreateView

urlpatterns = [
    path("jobs/", JobListView.as_view(), name="job-list"),
    path("jobs/manage/", JobManageListCreateView.as_view(), name="job-manage-list"),
    path("jobs/manage/<int:pk>/", JobManageDetailView.as_view(), name="job-manage-detail"),
]