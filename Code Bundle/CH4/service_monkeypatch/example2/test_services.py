import services


def test_start_service(monkeypatch):
    commands = []
    monkeypatch.setattr(services, "run", commands.append)
    services.start_service("web")
    assert commands == ["docker run web"]
