# pinax-news


!!! note "Pinax Ecosystem"
    This app is part of the Pinax ecosystem and is designed for use
    both with and independently of other Pinax apps.

    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

To install pinax-news:

    pip install pinax-news

Add `pinax-news` to your `INSTALLED_APPS` setting:

```python
    INSTALLED_APPS = (
        ...
        "imagekit",
        "pinax.news",
        ...
    )
```

You will need either `PIL` or `Pillow` installed for `imagekit` to work.  We
recommend `Pillow`:

    pip install Pillow


## Settings

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

## Usage

In your template where you want to display news or press releases:

First, load the template tags:

    {% load pinax_news_tags %}

For news:

    {% news as news_items %}

For press releases (new stories with the press_release boolean set to `True`):

    {% press_releases as press_release_items %}

And here is an example that how you can show the news or press releases:

```html
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

## Changelog

See [Changelog](./changelog.md).
