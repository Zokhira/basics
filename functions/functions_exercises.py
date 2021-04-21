def favorite_book(book_title):
    print(f"One of my favorite books is '{book_title}'")
favorite_book("Harry Potter")

def multi_num(a: int, b: int):
    c = a * b
    print(f"product of {a} and {b} is {c}.")
multi_num(5, 6)
multi_num(0,6)
multi_num(-1, -1)
multi_num(True, True)

def swap(a,b):
    return a, b
swap(5,6)