from django.db import models


class Mission(models.Model):
    """
    Modelo mínimo de ejemplo para misiones.
    """

    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

