# What's this?

With the growth of [py.test](http://pytest.org/) I've been working through Harry's book, but instead of using unittest or Django's own testing, I've been trying to work with py.test.

This respository is an attempt at a minimal conversion of the original book examples to work with py.test. One difference to how I'd prefer to work is that I've not renamed any files unless necessary — this is solely to make the differences easier to see. (Normally py.test looks for files called `test_*.py`, so instead I've told it to look for tests in every python file.) 

## Requirements

I am using a small package called [pytest-django](https://pytest-django.readthedocs.org/) by Andreas Pelme which is a plugin for py.test. It adds a number of very convenient things to py.test for working with Django. Installing it with `pip install pytest-django` was all I needed. Installing pytest-django will pull in py.test as a dependency as well. There's a [video from EuroPython 2013](https://www.youtube.com/watch?v=aUf8Fkb7TaY) about it.

## Caveats

I'm not particularly experienced with Django or py.test. There may be mistakes, or things may not be "best practice". I'm very open to suggestions how this could be done better.

This is incomplete. So far, I've done up to and including Chapter 5.

# Harry's Original README

This repository contains all the example code from my book, "Test-Driven Web
Development with Python", available at
[www.obeythetestinggoat.com](http://www.obeythetestinggoat.com)

## Checking out code for individual chapters

Each chapter in the book has its own branch, which contains all the commits for that chapter.  So, the state of the code in a branch is the state of the code at the *end* of that chapter.

In other words, if you want to start on a particular chapter in the book, you should check out the code for the *previous* chapter.

So, eg, [chapter_05](https://github.com/hjwp/book-example/tree/chapter_05) has all the commits up to the end of chapter 5, so it's the branch to check out if you want to skip to the beginning of chapter 6.

Branches follow the syntax chapter_XX, so they're zero-padded.
