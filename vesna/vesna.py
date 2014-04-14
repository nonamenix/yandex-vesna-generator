from lxml import etree
from vesna.database import EntriesDatabase


class Entry(object):
    def __init__(self, topic="", paragraphs=[], themes=[], **kwargs):
        self.topic = topic
        self.paragraphs = paragraphs
        self.themes = themes
        self.header_wrapper = kwargs.get('header_wrapper', "h2")

    def render_html(self):
        html = self.header
        html += self.body
        return html

    @property
    def header(self):
        return "<%(header_wrapper)s>%(topic)s</%(header_wrapper)s> \n" % {
            'topic': self.topic,
            'header_wrapper': self.header_wrapper
        }

    @property
    def body(self):
        return "".join(["<p>%s</p> \n" % p for p in self.paragraphs])

    def __repr__(self):
        return '<Entry theme="%s" id="%s">' % (", ".join(self.themes), hex(id(self)))


class VesnaGenerator(object):
    """ Class for generate crazy text on your site """

    # Themes
    AVAILABLE_THEMES = [
        'astronomy', 'geology', 'gyroscope', 'literature', 'marketing', 'mathematics', 'music', 'polit',
        'agrobiologia', 'law', 'psychology', 'geography', 'physics', 'philosophy', 'chemistry']

    def __init__(self, themes=[]):
        self.themes = [theme for theme in themes if theme in self.AVAILABLE_THEMES] or self.AVAILABLE_THEMES

        # Generate yandex vesna url
        self.base_url = "http://vesna.yandex.ru/all.xml"
        self.url = self.base_url + "?mix=" + "%2C".join(self.themes) + "=on&".join(self.themes)

    def generate_entry(self):
        self.parser = etree.HTMLParser(recover=True)
        self.doc = etree.parse(self.url, self.parser)

        topic = self.doc.xpath('//td[@colspan="9"]/div/h1')[0]
        paragraps = self.doc.xpath('//td[@colspan="9"]/div/p')

        return Entry(
            topic=topic.text,
            paragraphs=[p.text for p in paragraps],
            themes=self.themes
        )