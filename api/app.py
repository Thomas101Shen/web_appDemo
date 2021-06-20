from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)

#in a real application all of this data would be pulled from a database

app.config['DEBUG'] = True
app.config['MAIL_SERVER'] = #ex:'smtp.gmail.com'
app.config['MAIL_PORT'] = #ex: 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEFAULT_SENDER'] = ('Name' ,'username')
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

CORS(app)

@app.route('/api', methods = ['POST'])
def addContact():
	contact_json = request.get_json()

	if not contact_json: return {'status': 'Missing JSON'}, 400

	name = contact_json.get('name')
	if not name: return {'status': 'Name is missing'}, 400

	email = contact_json.get('email')
	if not email: return {'status': 'Email is missing'}, 400

	message = contact_json.get('message')
	if not message: return {'status': 'No message'}, 400

	msg = Message(str(name), recipients = [username]) #can send to own email or a personal email
	msg.body = 'client\'s email address: ' + str(email) + '\n\n\n    ' + message
	mail.send(msg)

	confirmation = Message('Thanks for choosing us!', recipients = [str(email)])
	confirmation.html = '<h1>We are thrilled to have you!</h1>'
	mail.send(confirmation)

	return jsonify({ 'status': 'success!'}), 200