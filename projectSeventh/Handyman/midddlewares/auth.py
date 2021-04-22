from django.shortcuts import redirect


def authMiddleware(get_response):

    def middleware(request):
        if not request.session.get('user'):
            return redirect('login')
        response = get_response(request)
        return response
    return middleware