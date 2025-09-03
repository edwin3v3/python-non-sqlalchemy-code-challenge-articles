from lib.classes.author import Author
from lib.classes.magazine import Magazine

class Article:
    all = []  # keep track of all Article instances

    def __init__(self, author, magazine, title):
        # Validate author
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        # Validate magazine
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        # Validate title
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")

        # Assign values (title only once using hasattr pattern)
        self._author = author
        self._magazine = magazine
        if hasattr(self, "_title"):
            raise AttributeError("title can't be changed once set")
        self._title = title

        # Track this article globally
        Article.all.append(self)

    # --- Properties ---
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        self._magazine = value

    @property
    def title(self):
        return self._title