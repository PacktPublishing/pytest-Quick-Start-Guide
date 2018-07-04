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
    assert (
        captured.out
        == dedent(
            """\
        Create/update webhooks.
          Usage: hooks REPO URL
    """
        )
    )


import _image_processing


def process_pending_events():
    print("")
