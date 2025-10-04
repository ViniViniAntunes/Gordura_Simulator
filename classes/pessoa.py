
class Pessoa(object):
	def __init__(self, nome=None, peso=None, altura=None):
		self.nome = nome
		self.peso = peso
		self.altura = altura
		self.dinheiro = 5
		self.cansaco = 0
		self.stress = 0

	def ganhar_peso(self, quantidade):
		self.peso += quantidade

	def perder_peso(self, quantidade):
		self.peso -= quantidade

	def ganhar_stress(self, quantidade):
		self.stress += quantidade

	def perder_stress(self, quantidade):
		self.stress -= quantidade
		if self.stress < 0:
			self.stress = 0

	def ganhar_cansaco(self, quantidade):
		self.cansaco += quantidade

	def perder_cansaco(self, quantidade):
		self.cansaco -= quantidade
		if self.cansaco < 0:
			self.cansaco = 0

	def ganhar_dinheiro(self, quantidade=1):
		self.dinheiro += quantidade

	def perder_dinheiro(self, quantidade=1):
		if self.dinheiro - quantidade < 0:
			return 'erroSemDinheiro'
		else:
			self.dinheiro -= quantidade

	def imc(self):
		return round(self.peso / ( self.altura / 100 ) ** 2, 2)
