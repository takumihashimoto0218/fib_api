from flask import Flask, jsonify, request

app = Flask(__name__)

def fib(n):
  if n < 0:
    raise ValueError("nは非負の整数でなければなりません")
  elif n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      a, b = 0, 1
      for _ in range(2, n + 1):
          a, b = b, a + b
      return b

@app.route('/fib', methods=['GET'])
def get_fib():
    n = request.args.get('n', default=1, type=int)
    try:
        result = fib(n)
        return jsonify({'result': result}), 200
    except ValueError as e:
        return jsonify({'status': 400, 'message': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True) # 本番環境ではデバッグモードを無効にする
