import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
  return jsonify({'status': 'ok'})

if __name__ == '__main__':
  if os.getenv('FLASK_ENV') == 'development':
    app.run(host='0.0.0.0', port=8080, debug=True)
  else:
    app.run(host='0.0.0.0', port=8080, ssl_context=('/tls/tls.cert', '/tls/tls.key'))
