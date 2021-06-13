books = []
books.append("book1")
books.append("book2")
books.append("books3")

print(books)

books.pop()
print("Now top book : ",books[-1])
books.pop()
print("now top books: ", books[-1])
books.pop()


if not books:
    print("no books")