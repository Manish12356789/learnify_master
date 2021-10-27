def teacher_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, displaying message if provided.
    """
    actual_decorator = user_passes_test(
        lambda u: u.user_type == "teacher",
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def student_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, displaying message if provided.
    """
    actual_decorator = user_passes_test(
        lambda u: u.user_type == "student",
        login_url=login_url,
        redirect_field_name=redirect_field_name,
        message=message
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator