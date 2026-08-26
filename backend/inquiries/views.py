from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView

from .models import Inquiry
from .serializers import InquirySerializer, InquiryStatusSerializer


class InquiryThrottle(AnonRateThrottle):
    rate = "5/hour"


class InquiryCreateView(APIView):
    """Public endpoint: accepts inquiry/contact form submissions."""

    permission_classes = [permissions.AllowAny]
    throttle_classes = [InquiryThrottle]

    def post(self, request):
        serializer = InquirySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Thanks — we'll be in touch within 1-2 business days."}, status=201)


class InquiryListView(generics.ListAPIView):
    """Team-only: list submitted inquiries, newest first. Requires login."""

    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        status_filter = self.request.query_params.get("status")
        if status_filter:
            qs = qs.filter(status=status_filter)
        return qs


class InquiryStatusUpdateView(generics.UpdateAPIView):
    """Team-only: update an inquiry's status (New / Reviewed / Contacted / Archived)."""

    queryset = Inquiry.objects.all()
    serializer_class = InquiryStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["patch"]
