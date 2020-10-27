from django.db import models

# Create your models here.


class LanguageList(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TagList(models.Model):
    name = models.CharField(_("tag name""), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TagContent(models.Model):
    tag_list_id = models.ForeignKey(
        TagList, verbose_name=_(""), on_delete=models.CASCADE)
    language_list_id = models.ForeignKey(
        LanguageList, verbose_name=_("relaction language"), on_delete=models.CASCADE)
    name = models.CharField(_(""), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
