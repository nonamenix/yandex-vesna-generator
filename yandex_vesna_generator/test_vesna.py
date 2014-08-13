import unittest
from yandex_vesna_generator.vesna import VesnaGenerator


class Test(unittest.TestCase):
    def setUp(self):
        self.header_wrapper = 'h1'
        self.vesna = VesnaGenerator(entry_options={'header_wrapper': self.header_wrapper})

    def test_generate_entry(self):
        entry = self.vesna.generate_entry()
        self.assertNotEqual(entry.title, "")
        self.assertNotEqual(entry.body, "")
        self.assertNotEqual(entry.header, "")

    def test_header_wrapper(self):
        entry = self.vesna.generate_entry()
        self.assertTrue(self.header_wrapper in entry.header)

if __name__ == '__main__':
    unittest.main()


