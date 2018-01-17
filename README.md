![](http://pinaxproject.com/pinax-design/patches/pinax-news.svg)

# Pinax News

[![](https://img.shields.io/pypi/v/pinax-news.svg)](https://pypi.python.org/pypi/pinax-news/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-news.svg)](https://circleci.com/gh/pinax/pinax-news)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-news.svg)](https://codecov.io/gh/pinax/pinax-news)
[![](https://img.shields.io/github/contributors/pinax/pinax-news.svg)](https://github.com/pinax/pinax-news/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-news.svg)](https://github.com/pinax/pinax-news/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-news.svg)](https://github.com/pinax/pinax-news/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Settings](#settings)
  * [Usage](#usage)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)

## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.


## pinax-news

### Overview

``pinax-news`` is a simple app for publishing links to news articles on your site.

#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *


## Documentation

### Installation

To install pinax-news:

```commandline
$ pip install pinax-news
```

Add `pinax-news` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # other apps
    "imagekit",
    "pinax.news",
]
```

You will need either `PIL` or `Pillow` installed for `imagekit` to work.  We
recommend `Pillow`:

```commandline
$ pip install Pillow
```

### Settings

There are two settings that have defaults but if you want to override them you
need to just set them to the dotted-notation path to the `ImageSpec` class that
you wish to use to process the `image` and `secondary_image` files for the
`image_thumb` and `secondary_image_thumb` attributes on the `News` model.

```python
PINAX_NEWS_IMAGE_THUMBNAIL_SPEC = "pinax.news.specs.ImageThumbnail"
PINAX_NEWS_SECONDARY_IMAGE_THUMBNAIL_SPEC = "pinax.news.specs.SecondaryImageThumbnail"
```

To create your own `ImageSpec` classes you can reference the defaults, but it is
basically subclassing `imagekit.ImageSpec`.

### Usage

In your template where you want to display news or press releases:

First, load the template tags:

```djangotemplate
{% load pinax_news_tags %}
```

For news:

```djangotemplate
{% news as news_items %}
```

For press releases (new stories with the press_release boolean set to `True`):

```djangotemplate
{% press_releases as press_release_items %}
```

Here is an example news item list display:

```djangotemplate
{% for news_item in news_items %}
    <article class="news-article" style="{% if news_item.secondary_image_thumb %}background-image:url({% static news_item.secondary_image_thumb.url %});{% endif %}">
        <h3>
            <a href="{{ news_item.url }}">
                {% if news_item.image_thumb %}<img src="{{ news_item.image_thumb.url }}" width="168" />{% endif %}
                <span>{{ news_item.title }}</span>
            </a>
        </h3>
    </article>
{% endfor %}
```

Add and manage news and press releases via the Django admin.


## Change Log

### 2.0.3

* Add django>=1.11 to requirements
* Update CI config
* Remove doc build support
* Add sorting guidance for 3rd-party app imports
* Improve documentation markup

### 2.0.2

* setup.py changes to support PyPi doc display 

### 2.0.1

* Fix setup.py LONG_DESCRIPTION for PyPi

### 2.0.0

* Add Django 2.0 compatibility testing
* Drop Django 1.8, 1.9, 1.10 and Python 3.3 support
* Move documentation into README
* Standardize documentation layout
* Convert CI and coverage to CircleCi and CodeCov
* Add PyPi-compatible long description

### 1.1.2

* fix packaging

### 1.1.1

* fix packaging

### 1.1.0

* added support for secondary images
* added support for customized image sizing

### 1.0.0

* added docs and tests and wired up CI

### 0.1

* initial release


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).

## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
