from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'middle_name',
        'email',
        'role',
        'is_staff',
        'is_superuser',
    )


admin.site.register(CustomUser, CustomUserAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'surname',
        'patronymic',
        'get_books'
    )

    def get_books(self, obj):
        return ', '.join([book.name for book in obj.books.all()])

    get_books.short_description = 'books'

    fieldsets = (
        ('Author\'s full name', {
            'fields': ('name', 'surname', 'patronymic')
        }),
        ('Author\'s book', {
            'fields': ('books',)
        })
    )


admin.site.register(Author, AuthorAdmin)


class AuthorFilter(SimpleListFilter):
    title = 'Authors'
    parameter_name = 'authors'

    def lookups(self, request, model_admin):
        authors = Author.objects.all()
        return [(author.id, f'{author.name} {author.surname} {author.patronymic}') for author in authors]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(authors__id=self.value())


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'changeable',
        'not_changeable',
    )

    def changeable(self, obj):
        return f"Books count: {obj.count} || Date of issue:{obj.date_of_issue}"

    def not_changeable(self, obj):
        return f"Book name: {obj.name} || Description: {obj.description} || Year of publication: {obj.year_of_publication} || Author: {', '.join([f'{author.name} {author.surname} {author.patronymic}' for author in obj.authors.all()])} "

    not_changeable.short_description = 'Not changeable'
    changeable.short_description = 'changeable'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'year_of_publication', 'description', 'year_of_publication']
        else:
            return []

    list_filter = ['id', 'name', AuthorFilter]

    fieldsets = (
        ('Name of the book', {
            'fields': ('name', 'description')
        }),
        ('Number of copies in library', {
            'fields': ('count',)
        }),
        ('Year of publication and issue', {
            'fields': ('year_of_publication', 'date_of_issue')
        })
    )


admin.site.register(Book, BookAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'get_book',
        'get_user',
        'created_at',
        'plated_end_at'
    )

    def get_book(self, obj):
        return obj.book.name if obj.book else ''

    def get_user(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name} {obj.user.middle_name}' if obj.user else ''

    get_book.short_description = 'book'
    get_user.short_description = 'user'


admin.site.register(Order, OrderAdmin)
