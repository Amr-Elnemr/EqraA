class BookDetail(object):
	"""docstring for BookDetail"""
	def __init__(self, Id,name,authors,bookPic,desc):
		super(BookDetail, self).__init__()
		self.id = Id
		self.name = name
		self.authors = authors
		self.pic=bookPic
		self.desc = desc


		
