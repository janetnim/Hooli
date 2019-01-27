import graphene
from graphene_django.types import DjangoObjectType
from .models import User
from graphene import ObjectType, InputObjectType, Mutation

# Get all method
# Remember we will use the UserType graphQL model we defined to avoid conflicting
# with Django's User model(Our real user model)
class UserType(DjangoObjectType):
  class Meta:
    model = User

class Query(ObjectType):
  users = graphene.List(UserType)
  user = graphene.Field(UserType, username=graphene.String())

  # Get one user
  def resolve_user(self, info, **kwargs):
    username = kwargs.get('username')
    if username is not None:
      return User.objects.get(username=username)
    return None

  # Get all users
  def resolve_users(self, info, **kwargs):
    return User.objects.all()


# Create method

class UserInput(InputObjectType):
  username = graphene.String(required=True)
  email = graphene.String(required=True)
  password = graphene.String(required=True)

class CreateUser(Mutation):
  class Arguments:
    user_data = UserInput(required=True)
  user = graphene.Field(UserType)

  @staticmethod
  def mutate(root, info, user_data=None):
    user_instance = User(
      username=user_data.username,
      email=user_data.email,
      password=user_data.password
    )
    user_instance.save()
    return CreateUser(user=user_instance)


# Update method

class UpdateUser(Mutation):
  class Arguments:
    user_data = UserInput(required=True)
  user = graphene.Field(UserType)

  def mutate(root, info, username, user_data=None):
    user_instance = User.objects.get(username=username)
    if user_instance:
      user_instance.username = user_data.username,
      user_instance.email = user_data.email,
      user_instance.password = user_data.password
      user_instance.save()
      return UpdateUser(user=user_instance)
    return UpdateUser(user=None)

class DeleteUser(Mutation):
  class Arguments:
    user_data = UserInput(required=True)
  user = graphene.Field(UserType)

  def mutate(root, info, username, user_data=None):
    user_instance = User.objects.get(username=username)
    if user_instance:
      user_instance.delete()
      return DeleteUser(user=None)
    return DeleteUser(user=user_data)



class Mutation(ObjectType):
  create_user = CreateUser.Field()
  update_user = UpdateUser.Field()
  delet_user = DeleteUser.Field()
