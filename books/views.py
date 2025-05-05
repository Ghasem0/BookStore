from .models import Book
from .forms import BookForm
from django.views import generic
from django.urls import reverse_lazy


class BooksListView(generic.ListView):
    model = Book
    paginate_by = 4   # for paginate books 4 by 4
    template_name = 'books/books_list_view.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BooksDetailView(generic.DetailView):
    model = Book
    template_name = 'books/books_detail_view.html'
    context_object_name = 'book'


class BooksCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/books_create_view.html'

    # we can also write like below
    # model = Book
    # fields = ['title', 'author', 'description', 'price']
    # template_name = 'books/books_create_view.html'
    # and this code no need to create a forms.py file in our project


class BooksUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/books_update_view.html'
    context_object_name = 'book'


class BooksDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/books_delete_view.html'
    success_url = reverse_lazy('books_list')