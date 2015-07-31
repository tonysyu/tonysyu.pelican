======================================
Readable regular expressions in Python
======================================

:tags: python, regex
:date: 2015-07-30


Awhile back, I needed to parse some strings that were created using Python's
`string formatter`_.  There's actually a package called parse_ that's intended
to do just that: Reuse the string formatting syntax to extract data from
a string.  Unfortunately, there were a couple of reasons that prevented me from
using that package, so I rolled a quick version of my own using `regular
expressions`_ (i.e. "regexes").

Note that this article assumes you're already familiar with the basic
syntax of regexes. If you're not familiar with regexes,
http://regexone.com/ offers a good interactive tutorial.

.. _string formatter: https://mkaz.com/2012/10/10/python-string-format
.. _parse: https://pypi.python.org/pypi/parse
.. _regular expressions: http://www.regular-expressions.info/quickstart.html


Named regex patterns
====================

For this use case, I'm going to be using named regex patterns (a.k.a.
`named capturing groups`_).
Unfortunately, the syntax for named regex patterns hurts my eyes. To fix
that, let's create a really simple ``name_regex`` function that makes it
more readable:

.. _named capturing groups: <http://www.regular-expressions.info/named.html>

.. code-block:: python

    def name_regex(name, pattern):
        """Return regex string as a named capture group."""
        return r'(?P<{name}>{pattern})'.format(name=name, pattern=pattern)

To clarify what's going on, you can just pass in two strings:

.. code-block:: python

    print name_regex('myname', 'Tony')

which gives:

.. parsed-literal::

    (?P<myname>Tony)


This string can be used as a regex to find the desired pattern
(``'Tony'``) and store the result as a named group (``'myname'``).

For a more interesting example, suppose you want to extract a price from some
text: You could look for a dollar sign, followed by numbers and decimal points.

.. code-block:: python

    # This isn't a great regex pattern for a price because any number of decimal
    # points and digits are accepted, but let's keep this simple.
    rx_price = name_regex('price', r'\$[\d.]+')

You can just use this like any other regex pattern with Python's built-in regex
package, ``re``:

.. code-block:: python

    import re

    match = re.search(rx_price, "All your's for only $9.95!")
    print match.groupdict()['price']


.. parsed-literal::

    $9.95


That extracted the text we wanted, but saving a named regex isn't that
useful if you're looking for a single value.


Named regexes with string formatting
====================================

Instead of creating a single named regex, let's create a dictionary with (name,
pattern) pairs:

.. code-block:: python

    def named_regexes(**names_and_patterns):
        """Return dictionary with regexes transformed into named capture groups.
        """
        return {k: name_regex(k, p) for k, p in names_and_patterns.items()}

If that looks a bit strange, we're just `packing arbitrary keyword-arguments
into a dictionary`_ and applying a `dictionary comprehension`_ on that
dictionary. We can use this to create regexes for parts of a timestamp:

.. _packing arbitrary keyword-arguments into a dictionary:
   http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python
.. _dictionary comprehension:
   http://www.diveintopython3.net/comprehensions.html#dictionarycomprehension

.. code-block:: python

    rx_letters = r'[A-z]+'
    rx_patterns = named_regexes(
        month=rx_letters,           # any letters
        day=r'\d{1,2}',             # 1 or 2 digits
        time=r'\d{2}:\d{2}:\d{2}',  # 3 pairs of digits separated by ':'
        year=r'\d{4}'               # 4 digits
    )

The result looks like:

.. code-block:: python

    from pprint import pprint

    pprint(rx_patterns)


.. parsed-literal::

    {'day': '(?P<day>\\d{1,2})',
     'month': '(?P<month>[A-z]+)',
     'time': '(?P<time>\\d{2}:\\d{2}:\\d{2})',
     'year': '(?P<year>\\d{4})'}


That's not really readable, but the point is to actually use it. For
example, let's consider the following timestamp:

.. code-block:: python

    timestamp = "Date: Apr 12 09:51:23 2015 -0500"

We can parse data from it with a format string and the dictionary of
regex patterns that we just defined:

.. code-block:: python

    rx_timestamp = "Date: {month} {day} {time} {year}".format(**rx_patterns)
    print re.search(rx_timestamp, timestamp).groupdict()


.. parsed-literal::

    {'month': 'Apr', 'year': '2015', 'day': '12', 'time': '09:51:23'}


Success! We've extracted the data we wanted in a form that's easy use.


Putting it all together
=======================

Let's wrap this up into a single function that returns a dictionary of
interesting data from a string containing that data, a template string,
and named regexes:

.. code-block:: python

    def match_regex_template(string, template, **keys_and_patterns):
        """Return dictionary of matches.

        Parameters
        ----------
        string : str
            String containing desired data.
        template : str
            Template string with named fields.
        keys_and_patterns : str
            Regexes for each field in the template.
        """
        named_patterns = named_regexes(**keys_and_patterns)
        pattern = template.format(**named_patterns)

        match = re.search(pattern, string)
        if match is None:
            raise RuntimeError(error_message.format(string=string,
                                                    template=template,
                                                    pattern=pattern))
        return match.groupdict()

    error_message = """
        string: {string}
        template: {template}
        pattern: {pattern}
    """

All this really does is combine the pieces that we discussed above.
Inevitably, you'll run into errors when writing regexes, so there's also
a bit of error handling to help with debugging.

To test this out, let's do a roundtrip: First, we take a template
string, plus some data, and produce an output string.

.. code-block:: python

    greeting_template = "Hey {name}! Welcome to {site}!"
    input_attrs = dict(name='you', site='tonysyu.github.io')
    greeting = greeting_template.format(**input_attrs)
    print greeting


.. parsed-literal::

    Hey you! Welcome to tonysyu.github.io!


Then let's take the output string and extract the data using
``match_regex_template``.

.. code-block:: python

    rx_anything = '.+'
    attrs = match_regex_template(greeting,
                                 greeting_template,
                                 name=rx_anything,
                                 site=rx_anything)
    print attrs


.. parsed-literal::

    {'name': 'you', 'site': 'tonysyu.github.io'}


Success!


Caveats
=======

That regex worked as expected, but you should be careful. This was a
pretty lazy attempt at regexes: ``rx_anything`` just captures ... uhm...
anything. If you have clear data boundaries, then this isn't an issue.
If the boundary is a bit more ambiguous, then you'll have to apply some
knowledge about the problem. For example, we can modify the greeting
above:

.. code-block:: python

    excited_greeting = greeting + '!!!'
    print excited_greeting


.. parsed-literal::

    Hello you! Welcome to tonysyu.github.io!!!!


Using the same regexes from above, we get

.. code-block:: python

    attrs = match_regex_template(excited_greeting,
                                 greeting_template,
                                 name=rx_anything,
                                 site=rx_anything)
    print attrs['site']


.. parsed-literal::

    tonysyu.github.io!!!


That enthusiasm is a bit too much to handle. To get back the desired
data, we can just be a bit more strict with the allowed text by
excluding exclamation marks:

.. code-block:: python

    rx_site = '[^!]+'  # anything other than '!'
    attrs = match_regex_template(excited_greeting,
                                 greeting_template,
                                 name=rx_anything,
                                 site=rx_site)
    print attrs['site']


.. parsed-literal::

    tonysyu.github.io


This is a simple and contrived example, but you get the idea.

Regexes are notoriously confounding, but they can be pretty readable if
you're careful to break up your parsing up into small, labeled chunks. A
little discipline will make future-you hate past-you a little less.
