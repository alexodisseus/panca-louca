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
		nome = request.form.get('name')
		email = request.form.get('email')
		cpf = request.form.get('cpf')
		birth = request.form.get('birth')
		telephone = request.form.get('telephone')
		cell = request.form.get('cell')
		addresses = request.form.get('addresses')
		accounts = request.form.get('accounts')
		# Faça algo com os dados recebidos, por exemplo, imprima-os
		print("Nome:", nome)
		print("Email:", email)
		print("CPF:", cpf)
		print("Data de Nascimento:", birth)
		print("Telefone:", telephone)
		print("Celular:", cell)
		print("Endereços:", addresses)
		print("Contas:", accounts)

		model.create_shareholder(nome, email,cpf,birth,telephone, cell)

		return redirect(url_for('admin.index'))

	
	return render_template('shareholder/create.html' )
	#return render_template('login.html' )



def configure(app):
	app.register_blueprint(shareholder)

