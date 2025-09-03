class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be String")
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value
    
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be at least 1 character long")
        self._category = value
    


    def articles(self):
        from lib.classes.many_to_many import Article
        return [article for article in Article.all if article.magazine == self]


    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        """Return a list of all article titles for this magazine"""
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        """Return authors with more than 2 articles in this magazine"""
        authors = {}
        for article in self.articles():
            authors[article.author] = authors.get(article.author, 0) + 1

        # filter authors with more than 2 publications
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        """Retrun the magazine with the most articles. Return None if no articles exist"""
        if not hasattr(cls, "all") or not cls.all:
            return None
        
        from lib.classes.article import Article

        if not Article.all:
            return None
        
        #count articles per magazine
        magazine_counts = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_counts[magazine] = magazine_counts.get(magazine, 0) + 1
        
        if not magazine_counts:
            return None
        
        return max(magazine_counts, key=magazine_counts.get)
    
