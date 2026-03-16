from django.db import models


class Profile(models.Model):
    """
    Modelo mínimo de ejemplo.
    """

    display_name = models.CharField(max_length=150, blank=True, default="")

    def __str__(self) -> str:
        return self.display_name or f"Profile<{self.pk}>"

