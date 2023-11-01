from django.db import models


class Work(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    Type = models.CharField(max_length=100, null=False, blank=False)
    Body = models.TextField(verbose_name="message body", null=False, blank=False)

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"

    def __str__(self):
        return self.Title


class Blog(models.Model):
    Title = models.CharField(max_length=100, null=False, blank=False, unique=True)
    Picture = models.ImageField()
    Body = models.TextField(verbose_name="message body", null=False, blank=False)

    class Meta:
        verbose_name = "Bllog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.Title


