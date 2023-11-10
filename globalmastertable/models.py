from django.db import models


class GmtCountry(models.Model):
    name = models.TextField()
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    alfa3 = models.CharField(max_length=3, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    num = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtcountry'


class GmtLanguage(models.Model):
    name = models.TextField()
    alfa2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtlanguage'


class GmtState(models.Model):
    gmtcountry = models.ForeignKey(GmtCountry, models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gmtstate'
