from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __unicode__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Info(models.Model):
    owner = models.ForeignKey(Person)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    obs = models.TextField()
