from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view to return contents of shopping bag """

    return render(request, 'bag/bag.html')