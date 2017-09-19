class Request(object):

	def __init__(self):
		self.url = "",
		self.version = "1.1"
		self.method = None
		self.headers = {}
		self.body = []

	def __str__(self):
		return self.url.decode()