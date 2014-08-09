from tastypie.resources import ModelResource
from .models import Person
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication


class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
        allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        authentication = Authentication()
        authorization = Authorization()
