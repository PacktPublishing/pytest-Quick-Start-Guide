import pytest


class WindowManager:

    def __init__(self, logging_directory):
        ...

    def close(self):
        """
        Close the WindowManager and all associated resources.        
        """
        ...


@pytest.fixture
def manager():
    return WindowManager()


def test_windows_creation(manager):
    window = manager.new_help_window("pipes_help.rst")
    assert window.title() == "Pipe Setup Help"


@pytest.fixture
def manager():
    return WindowManager()


def create_window_manager():
    return WindowManager()


def test_windows_creation():
    manager = create_window_manager()
    window = manager.new_help_window("pipes_help.rst")
    assert window.title() == "Pipe Setup Help"


def test_windows_creation():
    manager = WindowManager()
    window = manager.new_help_window("pipes_help.rst")
    assert window.title() == "Pipe Setup Help"


def create_window_manager(tmpdir, request):
    wm = WindowManager(str(tmpdir))
    request.addfinalizer(wm.close)
    return wm


def test_windows_creation(tmpdir, request):
    manager = create_window_manager(tmpdir, request)
    window = manager.new_help_window("pipes_help.rst")
    assert window.title() == "Pipe Setup Help"
