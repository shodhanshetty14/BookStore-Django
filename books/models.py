from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.URLField(max_length=2083, default=False)
    follow_author = models.URLField(max_length=2083, blank=True)
    book_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.publisher.name})"

class Order(models.Model):
    product = models.ForeignKey(Book, null=True, blank=True, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

# Create a publisher
# publisher = Publisher(name='Publisher 1', email='publisher@example.com')
# publisher.save()

# # Create an author
# author = Author(name='Author 1', gender='M', email='author@example.com')
# author.save()

# # Create a book
# book = Book(title='Book 1', author=author, publisher=publisher, price=10.99)
# book.save()
