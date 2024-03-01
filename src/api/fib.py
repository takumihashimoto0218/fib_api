from flask import request, jsonify
from src.fib_logic import fib

def get_fib():
  n_str = request.args.get('n', default="none")
  try:
    n = int(n_str)
    result = fib(n)
    return jsonify({'result': result}), 200
  except ValueError:
    return jsonify({'status': 400, 'message': 'Bad request'}), 400
