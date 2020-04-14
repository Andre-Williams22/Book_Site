# Book_Site

How would we filter for all books with titles containing the word ‘Django’? Book.objects.filter(books__name='Django')
How would we filter for all books with tag ‘Fiction’? Book.objects.filter(title='Fiction)
How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it! Book.objects.filter(book__contains='Django)