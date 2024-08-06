"""Models for My App."""
from django.db import models

from nautobot.apps.models import extras_features
from nautobot.apps.models import PrimaryModel


@extras_features(
    "custom_fields",
    "custom_validators",
    "export_templates",
    "graphql",
    "relationships",
    "webhooks",
)
class TestModel(PrimaryModel):
    """
    Test model.
    """

    location = models.OneToOneField(to="dcim.Location", on_delete=models.CASCADE, related_name="test_model")

    class Meta:
        """Metaclass attributes."""

        ordering = ["location___name"]

