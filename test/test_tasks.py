import requests
import json
from nose.tools import assert_equal

def test_query_airplane():
    r = requests.post('http://localhost:5001/query_airplane', json = {'aireplane_id':1})
    result = json.loads(json.dumps(r.json()))
    assert_equal(result.get('code', 0), 1)