import graphene

from graphene_django.types import DjangoObjectType

from cookbook.ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        description = "This is a category"

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query(object):
    category = graphene.Field(CategoryType, id=graphene.Int(), name=graphene.String())
    all_categories = graphene.List(CategoryType)

    ingredient = graphene.Field(IngredientType, id=graphene.Int(), name=graphene.String())
    all_ingredients = graphene.List(IngredientType)


    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related("category").all()

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get("id", None)
        name = kwargs.get("name", None)

        if id is not None:
            return Ingredient.objects.get(id=id)

        if name is not None:
            return Ingredient.objects.get(name=name)

        return None

    def resolve_category(self, info, **kwargs):
        _id = kwargs.get("id", None)
        name = kwargs.get("name", None)

        if _id is not None:
            return Category.objects.get(id=_id)

        if name is not None:
            return Category.objects.get(name=name)

        return None