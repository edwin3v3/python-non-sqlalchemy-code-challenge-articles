from lib.classes.many_to_many import Author, Magazine, Article

1 = Author("Blake")

# a.name = "kinuya"
print(a1.name)

m1 = Magazine("aaa", "News")

print(m1.name)
print(m1.category)

a1 = Author("Alice")
a2 = Author("Bob")
m2 = Magazine("TechToday", "Technology")

article = Article(a1, m2, "The Future of AI")
print(article.title)      # The Future of AI
print(article.author.name)   # Alice
print(article.magazine.name) # TechToday

article.author = a1
print(article.author.name)

print(article.magazine.name)

art1 = Article(a1, m1, "The Future of AI")
art2 = Article(a1, m2, "Staying Healthy with AI")
art3 = Article(a2, m1, "Tech and Society")

print([a.title for a in a1.articles()])

print([m.name for m in a1.magazines()])
