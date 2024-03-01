from .fib import get_fib
from .errors import not_found, bad_request

def init_app(app):
  app.register_error_handler(404, not_found)
  app.register_error_handler(400, bad_request)
  app.add_url_rule('/fib', view_func=get_fib, methods=['GET'])
