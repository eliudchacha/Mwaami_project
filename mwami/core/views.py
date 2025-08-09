from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to mwaami foundation',
        'endpoints': {
            'children': '/children/',
            'sponsors': '/sponsors/',
            'donation': '/donation/',
            'media': '/media/',
            'ads': '/ads/',
            'hero': '/hero/',
            'about': '/about/',
            'programs': '/programs/',
            'Impact': '/impact/',
            'testimonials': '/testimonials/',
            'staff': '/staff/',
            'slides': '/slides/'
        }
    })