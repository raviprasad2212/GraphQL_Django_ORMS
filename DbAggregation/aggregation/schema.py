from graphene import ObjectType, String, List, Field, Int, Float
from graphene.types.scalars import Float, Int
from graphene_django import DjangoObjectType
from .models import Author
from django.db.models import Avg, Max

class AllAuthorData(DjangoObjectType):
    class Meta:
        model = Author


class GetDataAuthor(ObjectType):

    getauthorage = List(AllAuthorData)

    def resolve_getauthorage(self, info):
        number_of_authors = Author.objects.all()
        return number_of_authors

class MyOjects(ObjectType):
    Authors = Int()

class GetObjects(ObjectType):
    showObject = Field(MyOjects)

    def resolve_showObject(self, request):
        get_obj = Author.objects.count()

        return MyOjects(Authors=get_obj)


# Average age of author

class AverageAge(ObjectType):
    avg_age_author = Float()

class AggregateFunction(ObjectType):
    
    showavgauthor = Field(AverageAge)

    def resolve_showavgauthor(self, info):
        avg_age = Author.objects.all().aggregate(Avg('age'))
        print(avg_age)
        return AverageAge(avg_age_author=avg_age.get('age__avg'))

