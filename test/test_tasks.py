import requests
import json
import HtmlTestRunner
import unittest


class TestMethods(unittest.TestCase):

    def test_query_airplane(self):
        r = requests.post('http://127.0.0.1:5001/query_airplane', json = {'aireplane_id':1})
        result = json.loads(json.dumps(r.json()))
        self.assertEqual(result.get('code', 0), 1)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

