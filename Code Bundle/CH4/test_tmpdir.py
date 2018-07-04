import json
import os
from pathlib import Path

import pytest


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


def download_images(param, images_dir):
    pass


def extract_images(param):
    pass


@pytest.fixture(scope="session")
def images_dir(tmpdir_factory):
    directory = tmpdir_factory.mktemp("images")
    download_images("https://example.com/samples.zip", directory)
    extract_images(directory / "samples.zip")
    return directory


def apply_blur_filter(param):
    pass


def test_blur_filter(images_dir):
    output_image = apply_blur_filter(images_dir / "rock1.png")
    ...
