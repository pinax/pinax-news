from setuptools import find_packages, setup

VERSION = "3.0.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-news.svg
    :target: https://pypi.python.org/pypi/pinax-news/

==========
Pinax News
==========

.. image:: https://img.shields.io/pypi/v/pinax-news.svg
    :target: https://pypi.python.org/pypi/pinax-news/

\

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-news.svg
    :target: https://circleci.com/gh/pinax/pinax-news
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-news.svg
    :target: https://codecov.io/gh/pinax/pinax-news
.. image:: https://img.shields.io/github/contributors/pinax/pinax-news.svg
    :target: https://github.com/pinax/pinax-news/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-news.svg
    :target: https://github.com/pinax/pinax-news/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-news.svg
    :target: https://github.com/pinax/pinax-news/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\

``pinax-news`` is a simple app for publishing links to news articles on your site.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+
| Django / Python | 3.6 | 3.7 | 3.8 |
+=================+=====+=====+=====+
|  2.2            |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
|  3.0            |  *  |  *  |  *  |
+-----------------+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a simple app for publishing links to news articles on your site",
    name="pinax-news",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-news/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.news": []
    },
    test_suite="runtests.runtests",
    tests_require=[
        "Pillow>=7.1.1"
    ],
    install_requires=[
        "django>=2.22",
        "django-imagekit>=4.0.2",
        "Markdown>=3.2.1"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
