from django.db import models


class Inquiry(models.Model):
    class ProjectType(models.TextChoices):
        NEW_APP = "new_app", "New app build"
        EXISTING = "existing", "Existing product / ongoing work"
        MVP = "mvp", "MVP / prototype"
        CONSULTING = "consulting", "Technical consulting"
        OTHER = "other", "Something else"

    class Budget(models.TextChoices):
        UNDER_5K = "under_5k", "Under $5k"
        R5_15K = "5_15k", "$5k - $15k"
        R15_50K = "15_50k", "$15k - $50k"
        OVER_50K = "over_50k", "$50k+"
        NOT_SURE = "not_sure", "Not sure yet"

    class Status(models.TextChoices):
        NEW = "new", "New"
        REVIEWED = "reviewed", "Reviewed"
        CONTACTED = "contacted", "Contacted"
        ARCHIVED = "archived", "Archived"

    name = models.CharField(max_length=150)
    email = models.EmailField()
    company = models.CharField(max_length=150, blank=True)
    project_type = models.CharField(max_length=20, choices=ProjectType.choices, default=ProjectType.NEW_APP)
    budget = models.CharField(max_length=20, choices=Budget.choices, default=Budget.NOT_SURE)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.created_at:%Y-%m-%d}"
