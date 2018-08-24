from unittest.mock import MagicMock

import pytest


class BotFixture:

    def __init__(self):
        self.store = {"TEST": {"token": None}}

    def say(self, msg):
        result = MagicMock()
        if msg == "hello":
            result.text = "Hey, how can I help you?"
        elif msg == "my token is ASLKM8KJAN":
            self.store["TEST"]["token"] = "ASLKM8KJAN"
            result.text = "OK, your token was saved"
        else:
            assert False
        return result


@pytest.fixture
def bot():
    return BotFixture()


def test_hello(bot):
    reply = bot.say("hello")
    assert reply.text == "Hey, how can I help you?"


def test_store_deploy_token(bot):
    assert bot.store["TEST"]["token"] is None
    reply = bot.say("my token is ASLKM8KJAN")
    assert reply.text == "OK, your token was saved"
    assert bot.store["TEST"]["token"] == "ASLKM8KJAN"
