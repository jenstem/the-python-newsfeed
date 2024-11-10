from flask import session, redirect
from functools import wraps

def login_required(func):
  """
  Decorator to ensure that a user is logged in before accessing a function.

  Args:
    func (function): The function to be wrapped.

  Returns:
    function: The wrapped function that checks loging status.
  """
  @wraps(func)
  def wrapped_function(*args, **kwargs):
    """
    Inner function that checks if the user is logged in.

    Args:
      *args: Positional arguments to pass to the original function.
      **kwargs: Keyword arguments to pass to the original function.

    Returns:
      function or redirect:  Calls the original function if logged in,
                                otherwise redirects to the login page.
    """
    # if logged in, call original function with original arguments
    if session.get('loggedIn') == True:
      return func(*args, **kwargs)

    return redirect('/login')

  return wrapped_function
