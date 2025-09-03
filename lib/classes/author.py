from .article import Article
from .magazine import Magazine

class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # prevent changing after instantiation
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed once set.")
        
        #must be string
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty")
        
        self._name = value


    def articles(self):
        from lib.classes.many_to_many import Article
        # find alll article objects that belong to this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

   # --- New methods ---
    def add_article(self, magazine, title):
        """
        Creates and returns a new Article instance
        with this author, the given magazine, and title.
        """
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        return Article(self, magazine, title)

    def topic_areas(self):
        """
        Returns a unique list of categories of magazines
        this author has contributed to.
        Returns None if no articles exist.
        """
        if not self.articles():
            return None
        return list({magazine.category for magazine in self.magazines()})