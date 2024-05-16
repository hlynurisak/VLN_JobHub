from django.shortcuts import redirect
from functools import wraps


def anonymous_required(redirect_url):
    """ Redirects a logged-in user to a specified URL if trying to access a view that's meant for anonymous users only. """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
