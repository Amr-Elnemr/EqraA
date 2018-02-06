class BookDetail(object):
	"""docstring for BookDetail"""
	def __init__(self, Id,name,authorId,authorName):
		super(BookDetail, self).__init__()
		self.id = Id
		self.name = name
		self.authorId = authorId
		self.authorName = authorName
