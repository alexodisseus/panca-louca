import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


shareholder = Blueprint('shareholder' , __name__ , url_prefix='/cotistas')


#usado para administrar os usuarios do sistema
@shareholder.route('/', methods = ['GET','POST'])
def index():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	#data = model.read_tasks(session['userid'])
	
	return render_template('shareholder/index.html' )
	#return render_template('login.html' )


@shareholder.route('/create', methods = ['GET','POST'])
def create():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	if request.method == 'POST':

		post_params = request.form.to_dict()
		
		model.create_shareholder(post_params)

		return redirect(url_for('admin.index'))

	
	return render_template('shareholder/create.html' )
	#return render_template('login.html' )



def configure(app):
	app.register_blueprint(shareholder)