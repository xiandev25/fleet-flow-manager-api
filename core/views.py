from django.http import JsonResponse
from django.views.defaults import page_not_found, server_error

def custom_handler404(request, exception=None):
    """
    Custom 404 handler.
    Returns clean JSON for API endpoints, and standard HTML for browser pages.
    """
    if request.path.startswith('/api/'):
        return JsonResponse({
            'error': 'Not Found',
            'detail': f"The requested API path '{request.path}' was not found."
        }, status=404)
    
    return page_not_found(request, exception)

def custom_handler500(request):
    """
    Custom 500 handler.
    Returns clean JSON for API endpoints, and standard HTML for browser pages.
    """
    if request.path.startswith('/api/'):
        return JsonResponse({
            'error': 'Internal Server Error',
            'detail': 'An unexpected error occurred on the server.'
        }, status=500)
        
    return server_error(request)
