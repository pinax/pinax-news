import pkg_resources


default_app_config = "pinax.news.apps.AppConfig"
__version__ = pkg_resources.get_distribution("pinax-news").version
