from lxml import etree


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
        return '<Entry object with theme: "%s" at %s>' % (", ".join(self.themes), hex(id(self)))


class VesnaGenerator(object):
    """ Class for generate crazy text on your site """

    def __init__(self, themes=[]):
        # Themes
        self.available_themes = [
            'astronomy', 'geology', 'gyroscope', 'literature', 'marketing', 'mathematics', 'music', 'polit',
            'agrobiologia', 'law', 'psychology', 'geography', 'physics', 'philosophy', 'chemistry']

        self.themes = [theme for theme in themes if theme in self.available_themes] or ['astronomy']

        # Generate yandex vesna url
        self.base_url = "http://vesna.yandex.ru/all.xml"
        self.url = self.base_url + "?mix=" + \
                   "%2C".join(self.themes) + \
                   "=on&".join(self.themes)
        # Parser
        self.parser = etree.HTMLParser(recover=True)
        self.doc = etree.parse(self.url, self.parser)

    def generate_entry(self):
        # doc.xpath('//td[@colspan="9"]/div')[0]
        topic = self.doc.xpath('//td[@colspan="9"]/div/h1')[0]
        paragraps = self.doc.xpath('//td[@colspan="9"]/div/p')

        return Entry(
            topic=topic.text,
            paragraphs=[p.text for p in paragraps],
            themes=self.themes
        )