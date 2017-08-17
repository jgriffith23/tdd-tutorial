Originally, a project to work through this book: 
https://www.obeythetestinggoat.com/

But I figured while I'm at it, I could use this as an excuse to get practice 
with continuous integration/testing and automation. So far, I've tried out 
Travis. See?

.. image:: https://travis-ci.org/jgriffith23/tdd-tutorial.svg?branch=master
    :target: https://travis-ci.org/jgriffith23/tdd-tutorial

When I created this readme, the build was passing. Hooray!

Things I've learned along the way that have nothing to do with the TDD book:

- Django can handle setup/teardown of a live server from within a test context.
  https://docs.djangoproject.com/en/1.8/topics/testing/tools/#liveservertestcase

- Writing a configuration in YAML is so much nicer than running all those 
  commands yourself!

- I have more to learn if I want to let the robots do all the work.

More toolage and wisdom bullets to come...
