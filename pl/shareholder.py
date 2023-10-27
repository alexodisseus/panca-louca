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
		# Para obter todos os parâmetros da solicitação (GET, POST, etc.):
		params = request.args.to_dict()
		# Para obter apenas os parâmetros de um método POST:
		post_params = request.form.to_dict()
		# Para obter os parâmetros da URL (GET) e do corpo da solicitação (POST):
		all_params = {**params, **post_params}
		
		print('aqui')
		print(all_params)
		

		return redirect(url_for('admin.index'))

	
	return render_template('shareholder/create.html' )
	#return render_template('login.html' )



def configure(app):
	app.register_blueprint(shareholder)