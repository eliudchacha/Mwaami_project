# core/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    """
    DRF API Root – shows links to all main resources.
    """
    return Response({
        'children': reverse('child-list', request=request, format=format),
        'sponsors': reverse('sponsor-list', request=request, format=format),
        'volunteers': reverse('volunteer-list', request=request, format=format),
        'blogposts': reverse('blogpost-list', request=request, format=format),
        'slides': reverse('slide-list', request=request, format=format),
        'mediacontent': reverse('mediacontent-list', request=request, format=format),
        'advertisements': reverse('advertisement-list', request=request, format=format),
        'herosections': reverse('herosection-list', request=request, format=format),
        'programs': reverse('program-list', request=request, format=format),
        'impactstats': reverse('impactstat-list', request=request, format=format),
        'aboutcontent': reverse('aboutcontent-list', request=request, format=format),
    })
