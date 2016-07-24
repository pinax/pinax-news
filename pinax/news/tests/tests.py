from django.test import TestCase

from pinax.news.models import News
from pinax.news.templatetags.pinax_news_tags import news, press_releases


class Tests(TestCase):

    def test_html_generated_on_save(self):
        news = News.objects.create(
            title="Test News",
            url="http://example.com",
            description="### The Main Event\n\n* Item Number 1\n* Item Number 2"
        )
        self.assertEquals(news.description_html, "<h3>The Main Event</h3>\n<ul>\n<li>Item Number 1</li>\n<li>Item Number 2</li>\n</ul>")

    def test_news_tag(self):
        News.objects.create(
            title="Test News",
            url="http://example.com",
            description="### The Main Event\n\n* Item Number 1\n* Item Number 2"
        )
        self.assertEquals(news().count(), 1)
        self.assertEquals(press_releases().count(), 0)

    def test_press_releases_tag(self):
        News.objects.create(
            title="Test News",
            url="http://example.com",
            description="### The Main Event\n\n* Item Number 1\n* Item Number 2",
            press_release=True
        )
        self.assertEquals(news().count(), 0)
        self.assertEquals(press_releases().count(), 1)
