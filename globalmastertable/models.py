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


# // ----- // ----- // ----- // ----- // ----- //
# Section x - TestingTask1
# // ----- // ----- // ----- // ----- // ----- //

class Textingtask1(models.Model):
    serialid1 = models.AutoField()
    # blank --> especifica si el campo puede estar vacio
    # true --> puede estar vacio
    # false --> no puede estar vacio
    text1 = models.TextField(blank=True, null=True)
    character1 = models.CharField(max_length=10, blank=True, null=True)
    char1 = models.CharField(max_length=1, blank=True, null=True)
    money1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    date1 = models.DateField(blank=True, null=True)
    timestamp1 = models.DateTimeField(blank=True, null=True)

    # meta se usa para configurar opciones adicionales
    class Meta:
        # managed --> indica que django no administra la tabla
        # y lo hace la base de datos
        managed = False
        db_table = 'textingtask1' # Tablename

# // ----- // ----- // ----- // ----- // ----- //
# Section X - TestingTask1
# // ----- // ----- // ----- // ----- // ----- //
