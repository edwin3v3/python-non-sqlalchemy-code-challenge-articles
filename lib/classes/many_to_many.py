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
        

