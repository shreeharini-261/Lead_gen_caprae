from functools import wraps
from flask import flash, redirect, url_for, request
from flask_login import current_user

def role_required(*roles):
    """
    Decorator to restrict access to specific user roles.

    Usage:
        @role_required('admin')
        @role_required('admin', 'developer')

    Redirects:
        - If not logged in: redirects to login page with a flash message
        - If role not allowed: redirects to index page with a flash message
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Please log in to access this page.', 'danger')
                return redirect(url_for('auth.login', next=request.url))
            
            if current_user.role not in roles:
                allowed_roles = ", ".join(roles)
                flash(f'Access denied. This page requires one of the following roles: {allowed_roles}', 'danger')
                return redirect(url_for('main.index'))

            return f(*args, **kwargs)
        return decorated_function
    return decorator


def subscription_required(f):
    """
    Decorator to ensure the current user has an active subscription.
    Usage: @subscription_required
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to continue.', 'danger')
            return redirect(url_for('auth.login', next=request.url))

        if not hasattr(current_user, 'subscription') or current_user.subscription is None:
            flash('You need an active subscription to access this feature.', 'warning')
            return redirect(url_for('main.subscribe'))

        return f(*args, **kwargs)
    return decorated_function
