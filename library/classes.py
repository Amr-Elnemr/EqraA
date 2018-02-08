class BookDetail(object):
	"""docstring for BookDetail"""
	def __init__(self, Id,name,authorId,authorName,bookPic,desc):
		super(BookDetail, self).__init__()
		self.id = Id
		self.name = name
		self.authorId = authorId
		self.authorName = authorName
		self.pic=bookPic
		self.desc = desc

class categorybooks(object):
	"""docstring for categorybooks"""
	def __init__(self, book):
		self.book = book
		
