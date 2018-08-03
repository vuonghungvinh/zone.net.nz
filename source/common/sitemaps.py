import datetime
from django.contrib import sitemaps

from catalogue.models import Category, SubCategory, Product, ProductGapWidth
from projects.models import Entry


class StaticPagesSitemap(sitemaps.Sitemap):
    """
    Sitemap class for static pages.
    """
    pages = {
        '/': (1.0, 'weekly'),
        '/contact/': (0.5, 'yearly'),
        '/about/about/': (0.5, 'yearly'),
        '/projects/': (1.0, 'monthly'),
    }

    def items(self):
        return self.pages.keys()

    def changefreq(self, url):
        return self.pages[url][1]

    def location(self, url):
        return url

    def priority(self, url):
        return self.pages[url][0]


class CatalogueSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated


class SubCatalogueSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return SubCategory.objects.all()

    def lastmod(self, obj):
        return obj.updated


class ProductSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated


class ProductGapWidthSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ProductGapWidth.objects.all()

    def lastmod(self, obj):
        return obj.updated


class ProjectSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Entry.objects.all()

    def lastmod(self, obj):
        return obj.updated
