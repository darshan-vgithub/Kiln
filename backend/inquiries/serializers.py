from rest_framework import serializers

from .models import Inquiry


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            "id",
            "name",
            "email",
            "company",
            "project_type",
            "budget",
            "message",
            "status",
            "created_at",
        ]
        read_only_fields = ["id", "status", "created_at"]

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Tell us a little more about the project (10+ characters).")
        return value


class InquiryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ["id", "status"]
        read_only_fields = ["id"]
