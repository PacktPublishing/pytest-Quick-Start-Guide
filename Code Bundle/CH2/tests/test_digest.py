import hashlib


def commit_hash(contents):
    size = len(contents)
    print("content size", size)
    hash_contents = str(size) + "\0" + contents
    result = hashlib.sha1(hash_contents.encode("UTF-8")).hexdigest()
    print(result)
    return result[:8]


def test_commit_hash():
    contents = "some text contents for commit"
    assert commit_hash(contents) == "0cf85793"
