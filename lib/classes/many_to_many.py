from lib.classes.author import Author
from lib.classes.magazine import Magazine
from lib.classes.article import Article

__all__ = ["Author", "Magazine", "Article"]

class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self) 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be String")
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

    # ----------------------
    # ADD THIS METHOD
    # ----------------------
    @classmethod
    def top_publisher(cls):
        """Return the magazine with the most articles, or None if no articles exist."""
        from lib.classes.article import Article  # import here to avoid circular import

        if not Article.all:
            return None

        magazine_counts = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_counts[magazine] = magazine_counts.get(magazine, 0) + 1

        return max(magazine_counts, key=magazine_counts.get, default=None)
        

