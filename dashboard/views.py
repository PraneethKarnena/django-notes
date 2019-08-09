from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def home_view(request):
    """
    View for Home page. Simply render the Home template.
    """

    return render(request, 'notes/home.html')