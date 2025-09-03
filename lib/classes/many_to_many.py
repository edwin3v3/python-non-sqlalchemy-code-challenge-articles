class Article:
    all = [] # class-leve list to hold all articles

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    # --- author property ---
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.classes.many_to_many import Author
        if not isinstance(value, Author):
            raise TypeError("author must be an Author instance")
        self._author = value

    # --- magazine property ---
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from lib.classes.many_to_many import Magazine
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        self._magazine = value

    # --- title property (write-once only) ---
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):  # only allow first assignment
            raise AttributeError("title cannot be changed after initialization")
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("title must be between 5 and 50 characters")
        self._title = value
        
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
        pass

    def contributing_authors(self):
        pass