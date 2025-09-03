from lib.classes.many_to_many import Author, Magazine, Article

a = Author("Blake")

# a.name = "kinuya"
print(a.name)

m1 = Magazine("aaa", "News")

print(m1.name)
print(m1.category)

a1 = Author("Alice")
m2 = Magazine("TechToday", "Technology")

article = Article(a1, m2, "The Future of AI")
print(article.title)      # The Future of AI
print(article.author.name)   # Alice
print(article.magazine.name) # TechToday