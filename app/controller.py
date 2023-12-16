import os

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/mutate', methods=['POST'])
def mutate():
  admission_review = request.json

  if admission_review.get('request'):
    # Extract the admission request object
    admission_request = admission_review['request']

    # Extract the resource
    original_spec = admission_request.get('object')

    # Create an admission response
    admission_response = {
      'apiVersion': 'admission.k8s.io/v1',
      'kind': 'AdmissionReview',
      'response': {
        'allowed': True,
        'uid': admission_request.get('uid'),
        'patchType': 'JSONPatch',
        'patch': '',
        'status': { 'message': 'Admission allowed without mutation'},
        'warnings': []
      }
    }

    # Return the admission review
    return jsonify(admission_response)

  return jsonify({'error': 'Invalid admission review request'}), 400

@app.route('/healthz')
def health():
  return jsonify({'status': 'ok'})

if __name__ == '__main__':
  if os.getenv('FLASK_ENV') == 'development':
    app.run(host='0.0.0.0', port=8080, debug=True)
  else:
    app.run(host='0.0.0.0', port=8080, ssl_context=('/tls/tls.crt', '/tls/tls.key'))
