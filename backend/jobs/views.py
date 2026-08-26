from rest_framework import generics, permissions

from .models import Job
from .serializers import JobSerializer


class JobListView(generics.ListAPIView):
    """Public endpoint: only currently-active postings, newest first."""

    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def get_queryset(self):
        return Job.objects.filter(is_active=True)


class JobManageListCreateView(generics.ListCreateAPIView):
    """Team-only: list every posting (active or not) and create new ones."""

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class JobManageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Team-only: edit, toggle active, or delete a single posting."""

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]