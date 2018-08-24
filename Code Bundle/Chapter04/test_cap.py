from textwrap import dedent


def script_main(args):
    if not args:
        show_usage()
        return 0
    ...


def show_usage():
    print("Create/update webhooks.")
    print("  Usage: hooks REPO URL")


def test_usage(capsys):
    script_main([])
    captured = capsys.readouterr()
    expected = dedent(
        """\
        Create/update webhooks.
          Usage: hooks REPO URL
    """
    )
    assert captured.out == expected
