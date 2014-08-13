# -*- coding: utf-8 -*-
from lxml import etree
from slugify import slugify


class Entry(object):
    def __init__(self, title="", paragraphs=[], themes=[], **kwargs):
        self.title = title
        self.paragraphs = paragraphs
        self.themes = themes
        self.header_wrapper = kwargs.get("header_wrapper", "h2")
        self.paragraph_wrapper = kwargs.get("paragraph_wrapper", "p")
        self.slug = slugify(title, to_lower=True)

    def render_html(self):
        html = self.header
        html += self.body
        return html

    @property
    def header(self):
        return "<%(wrapper)s>%(title)s</%(wrapper)s> \n" % {
            'title': self.title,
            'wrapper': self.header_wrapper
        }

    @property
    def body(self):
        return "".join(["<%(wrapper)s>%(text)s</$(wrapper)s> \n" % {
            "text": p,
            "wrapper": self.paragraph_wrapper
        } for p in self.paragraphs])

    def __repr__(self):
        return '<Entry theme="%s" id="%s">' % (", ".join(self.themes), hex(id(self)))

    def __getitem__(self, field):
        return self.__dict__[field]


class VesnaGenerator(object):
    """ Class for generate crazy text on your site """

    # Themes
    AVAILABLE_THEMES = [
        'astronomy', 'geology', 'gyroscope', 'literature', 'marketing', 'mathematics', 'music', 'polit',
        'agrobiologia', 'law', 'psychology', 'geography', 'physics', 'philosophy', 'chemistry']

    def __init__(self, themes=[], entry_options={}):
        self.themes = [theme for theme in themes if theme in self.AVAILABLE_THEMES] or self.AVAILABLE_THEMES
        self.entry_options = entry_options

        # Generate yandex vesna url
        self.base_url = "http://referats.yandex.ru/referats/"
        self.url = self.base_url + "?t=" + "+".join(self.themes)

        self.entries = []

    def generate_entry(self):
        self.parser = etree.HTMLParser(recover=True)
        self.doc = etree.parse(self.url, self.parser)

        title = self.doc.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/strong')[0].text
        title = title.encode('utf-8').replace('Тема: «', '').replace('»', '').decode('utf-8')
        paragraps = self.doc.xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/p')

        return Entry(
            title=title,
            paragraphs=[p.text for p in paragraps],
            themes=self.themes,
            **self.entry_options
        )