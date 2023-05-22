from django.shortcuts import redirect, resolve_url
from django.contrib import messages

class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.path != '/admin/':
            if not request.user.is_staff:
                messages.error(request, 'Acesso restrito aos administradores.')
                return redirect(resolve_url('admin:login'))

        response = self.get_response(request)
        return response
