from django.db import models


class Job(models.Model):
    class EmploymentType(models.TextChoices):
        FULL_TIME = "full_time", "Full-time"
        PART_TIME = "part_time", "Part-time"
        CONTRACT = "contract", "Contract"
        INTERNSHIP = "internship", "Internship"

    title = models.CharField(max_length=150)
    employment_type = models.CharField(
        max_length=20, choices=EmploymentType.choices, default=EmploymentType.FULL_TIME
    )
    location = models.CharField(max_length=100, default="Remote")
    description = models.TextField()
    apply_email = models.EmailField(help_text="Where applications for this role should be sent.")
    is_active = models.BooleanField(
        default=True, help_text="Uncheck to hide this posting from the careers page without deleting it."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title