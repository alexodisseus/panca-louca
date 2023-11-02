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


	filters = request.args.get('search')
	
	data = model.list_users_shareholder(filters)

	
	return render_template('shareholder/index.html' , data=data)
	#return render_template('login.html' )




@shareholder.route('/create', methods = ['GET','POST'])
def create():
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	if request.method == 'POST':
		nome = request.form.get('name')
		email = request.form.get('email')
		cpf = request.form.get('cpf')
		birth = request.form.get('birth')
		telephone = request.form.get('telephone')
		cell = request.form.get('cell')
		addresses = request.form.get('addresses')
		accounts = request.form.get('accounts')
	
		model.create_shareholder(nome, email,cpf,birth,telephone, cell)

		return redirect(url_for('shareholder.index'))

	
	return render_template('shareholder/create.html' )
	

@shareholder.route('/view/<id>', methods = ['GET','POST'])
def view(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	data = model.view_user_shareholder(id)
	
	return render_template('shareholder/view.html', data=data)
	

@shareholder.route('/edit/<id>', methods = ['GET','POST'])

def edit(id):
	"""
	if 'username' not in session:
		return redirect(url_for('admin.login'))

	"""

	if request.method == 'POST':
		nome = request.form.get('name')
		email = request.form.get('email')
		cpf = request.form.get('cpf')
		birth = request.form.get('birth')
		telephone = request.form.get('telephone')
		cell = request.form.get('cell')
		addresses = request.form.get('addresses')
		accounts = request.form.get('accounts')
		print(id)
	
		model.update_shareholder(nome, email,cpf,birth,telephone, cell, id)

		return redirect(url_for('shareholder.view' , id = id))

	data = model.view_user_shareholder(id)
	
	return render_template('shareholder/edit.html' , data=data )
	#return render_template('login.html' )

def configure(app):
	app.register_blueprint(shareholder)

