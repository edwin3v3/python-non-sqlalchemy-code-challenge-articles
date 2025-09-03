from lib.classes.many_to_many import Author, Magazine

a = Author("Blake")
a = Author("Tom")

# a.name = "kinuya"
print(a.name)

m1 = Magazine("aaa", "")

print(m1.name)
print(m1.category)