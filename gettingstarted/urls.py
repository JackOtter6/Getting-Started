from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("about/", hello.views.about, name="about"),
    path("hangman/", hello.views.hangman, name="hangman"),
    path("scrabble/", hello.views.scrabble, name="scrabble"),
    path("caesar_cipher/", hello.views.caesar_cipher, name="caesar_cipher"),
    path("madlibs/", hello.views.madlibs, name="madlibs"),
]
