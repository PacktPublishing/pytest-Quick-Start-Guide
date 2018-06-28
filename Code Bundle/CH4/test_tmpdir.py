import json
import os
from pathlib import Path


def write_json(f, data):
    Path(f).write_text(json.dumps(data))


def test_empty(tmpdir):
    assert os.path.isdir(tmpdir)
    assert os.listdir(tmpdir) == []


def test_save_curves(tmpdir):
    data = dict(status_code=200, values=[225, 300])
    fn = tmpdir.join("somefile.json")
    write_json(fn, data)
    assert fn.read() == '{"status_code": 200, "values": [225, 300]}'
