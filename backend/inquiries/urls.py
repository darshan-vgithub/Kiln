from django.urls import path

from .views import InquiryCreateView, InquiryListView, InquiryStatusUpdateView

urlpatterns = [
    path("inquiries/", InquiryCreateView.as_view(), name="inquiry-create"),
    path("inquiries/list/", InquiryListView.as_view(), name="inquiry-list"),
    path("inquiries/<int:pk>/status/", InquiryStatusUpdateView.as_view(), name="inquiry-status"),
]
