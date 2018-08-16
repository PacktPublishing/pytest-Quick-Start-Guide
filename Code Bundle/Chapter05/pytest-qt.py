def test_main_window(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)
    qtbot.mouseClick(widget.about_button, QtCore.Qt.LeftButton)

    qtbot.waitUntil(widget.about_box.isVisible)
    assert widget.about_box.text() == "This is a GUI App"
