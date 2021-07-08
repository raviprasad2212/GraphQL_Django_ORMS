from graphene import ObjectType, Schema
from aggregation.schema import GetDataAuthor, GetObjects, AggregateFunction
class Query(GetObjects, GetDataAuthor, AggregateFunction, ObjectType):
    pass


schema = Schema(query=Query)