from django.db import models


class TimeStampedModel(models.Model):
    """TimeStampedModel"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # extra information
        abstract = True  # 데이터베이스에는 나타나지 않는 model 임을 가리킴.
