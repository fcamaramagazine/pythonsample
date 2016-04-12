# ----------------------------------
# This is a small sample showing how to connect to twitter Rest API using urllib3 and get client credentials
# Just Python - Flask framework - It shows how to use OAuth 1
# Code by Fernando Matsuo Santos
# Date: 2016/04/11
# ----------------------------------
import requests, json
from flask import Flask
from flask import g, session, request, url_for, flash
from flask import redirect, render_template
from flask import jsonify
from flask_oauthlib.client import OAuth

# Begin the app with Flask Framework
app = Flask(__name__)
app.debug = True
app.secret_key = 'development'

# Uses Twitter OAuth 1 endpoint
oauth = OAuth(app)

twitter = oauth.remote_app(
    'twitter',
    consumer_key='xBeXxg9lyElUgwZT6AZ0A',
    consumer_secret='aawnSpNTOVuDCjx7HMh6uSXetjNN8zWLpZwCEU4LBrk',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)

# Get Twitter token
@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        response = session['twitter_oauth']
        return response['oauth_token'], response['oauth_token_secret']

# Verify user session 
@app.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']

# Default home route
@app.route('/')
def index():
    tweets = None
    if g.user is not None:
        response = twitter.request('statuses/home_timeline.json')
        if response.status == 200:
            tweets = response.data
        else:
            flash('Unable to load tweets from Twitter.')
    return render_template('index.html', tweets=tweets)

# Search CEP information 
@app.route('/cep', methods=['POST'])
def search_cep():
    #cep = request.form['cep']
	cep = '01327000'
	url = 'https://viacep.com.br/ws/' + cep + '/json/'
	response = requests.get(url)
	json_data = json.loads(response.text)
	cidade = (u'%s' % json_data['localidade'])
	flash(cidade)
	return redirect(url_for('index'))

# Login at Twitter
@app.route('/login')
def login():
    callback_url = url_for('oauthorized', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)

# Logout from twitter
@app.route('/logout')
def logout():
    session.pop('twitter_oauth', None)
    return redirect(url_for('index'))

# Get sign in status
@app.route('/oauthorized')
def oauthorized():
    response = twitter.authorized_response()
    if response is None:
        flash('You denied the request to sign in.')
    else:
        session['twitter_oauth'] = response
    return redirect(url_for('index'))

# 404 file not found error
@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	#return '404 Error', 4044
	return render_template('404.html'), 4044

# handle errors and exceptions
@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)