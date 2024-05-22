from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menuitems(request, dish):
    items = {
        "Pad Thai": "Stir-fried rice noodles with vegetables, protein (chicken, tofu, etc.), and a sweet and savory sauce.",
        "Pizza Margherita": "Tomato sauce, mozzarella cheese, and fresh basil leaves on a classic Italian flatbread.",
         "Sushi": "Vinegared rice topped with various ingredients like raw fish, vegetables, and pickled ginger."
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)