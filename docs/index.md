# pinax-news


!!! note "Pinax Ecosystem"
    This app is part of the Pinax ecosystem and is designed for use
    both with and independently of other Pinax apps.

    To learn more about Pinax, see <http://pinaxproject.com/>


## Quickstart

To install pinax-news:

    pip install pinax-news

Add `pinax-news` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        "pinax.news",
        ...
    )

## Usage

In your template where you want to display news or press releases:

First, load the template tags:

    {% load pinax_news_tags %}

For news:

    {% news as news_items %}

For press releases (new stories with the press_release boolean set to `True`):

    {% press_releases as press_release_items %}

And here is an example that how you can show the news or press releases:

        {% for news_item in news_items %}
            <article class="news-article">
                <h3>
                    <a href="{{ news_item.url }}">
                        {% if news_item.image %}<img src="{{ news_item.image.url }}" width="168" />{% endif %}
                        <span>{{ news_item.title }}</span>
                    </a>
                </h3>
            </article>
        {% endfor %}

Add and manage news and press releases via the Django admin.

## Changelog

See [Changelog](./changelog.md).
