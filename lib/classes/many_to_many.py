class Article:
    def __init__(self, author, magazine, title):
     
        from lib.classes.many_to_many import Author, Magazine  
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine instance")

        # validate title
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("title must be between 5 and 50 characters")

        # store values
        self._author = author
        self._magazine = magazine
        self._title = title   

    # --- title property (read-only) ---
    @property
    def title(self):
        return self._title

    # --- author property (read-only for now) ---
    @property
    def author(self):
        return self._author

    # --- magazine property (read-only for now) ---
    @property
    def magazine(self):
        return self._magazine
        
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
        pass

    def magazines(self):
        pass

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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass