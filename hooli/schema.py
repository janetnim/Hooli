import graphene
from .apps.authentication.schema import Query as user_query
from .apps.authentication.schema import Mutation as create_user
from graphene import ObjectType

class Query(user_query, ObjectType):
  pass

class Mutation(create_user, ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
