from django.contrib import admin

from .models import Book, Library, Librarian, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Author)



def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')