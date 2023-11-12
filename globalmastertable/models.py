from django.db import models

# // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Country, State, City, location
# // ----- // ----- // ----- // ----- // ----- //


class GmtCountry(models.Model):
    name = models.TextField()
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    alfa3 = models.CharField(max_length=3, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    num = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtcountry'


class GmtState(models.Model):
    gmtcountry = models.ForeignKey(GmtCountry, models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gmtstate'


class GmtCity(models.Model):
    gmtstate = models.ForeignKey('Gmtstate', models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'gmtcity'

# // ----- // ----- // ----- // ----- // ----- //
# Section 1 - Finish Section
# // ----- // ----- // ----- // ----- // ----- //

# // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Language, Language, Communication
# // ----- // ----- // ----- // ----- // ----- //


class GmtLanguage(models.Model):
    name = models.TextField()
    alfa2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gmtlanguage'

# // ----- // ----- // ----- // ----- // ----- //
# Section 2 - Finish Section
# // ----- // ----- // ----- // ----- // ----- //
