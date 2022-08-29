from django.urls import path

from recipes.views import (
    # create_recipe,
    change_recipe,
    log_rating,
    # show_recipe,
    # show_recipes,
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
)

urlpatterns = [
    # path("", show_recipes, name="recipes_list"),
    path("", RecipeListView.as_view(), name="recipes_list"),
    # We're calling the as_view function on the CarListView class to
    # turn the class into a view that path can use.
    # path("<int:pk>/", show_recipe, name="recipe_detail"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    # path("new/", create_recipe, name="recipe_new"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("edit/", change_recipe, name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
]
