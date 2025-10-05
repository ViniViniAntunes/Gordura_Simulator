
class Item(object):
	def __init__(self):
		self.data = {
            'ovo' : 0,
            'leite' : 0,
            'banana' : 0,
            'trigo' : 0,
            'margarina' : 0,  # <- Uma colher = 0.08
            'acucar' : 0,
            'fermento' : 0,
            'oleo' : 0,
            'sal' : 0,
            'bolo' : 0,
            'pao' : 0,
            'ovo_frito' : 0,  # unidade
            'panqueca' : 0,  # unidade
        }

	def ganhar_item(self, **kwargs):
		for kw in kwargs:
			self.data[kw] += kwargs[kw]

	def perder_item(self, **kwargs):
		for kw in kwargs:
			self.data[kw] -= kwargs[kw]
			if self.data[kw] < 0:
				self.data[kw] = 0

	def debug(self):
		for i in self.data:
			self.data[i] = 500
