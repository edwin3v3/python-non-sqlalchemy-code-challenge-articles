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

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass