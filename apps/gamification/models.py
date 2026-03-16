from django.db import models


class Badge(models.Model):
    """
    Modelo mínimo de ejemplo para gamificación.
    """

    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name

