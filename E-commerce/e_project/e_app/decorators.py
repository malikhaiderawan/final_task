from functools import wraps
from django.http import HttpResponseForbidden

def admin_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to view this page.")
    return wrap

def user_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to view this page.")
    return wrap




