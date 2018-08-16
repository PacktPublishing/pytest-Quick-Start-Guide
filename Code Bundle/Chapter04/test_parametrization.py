import functools
from typing import Any

import pytest
import attr


@attr.s
class Quantity:
    value = attr.ib()
    unit = attr.ib()


@attr.s
class Pipe:
    length = attr.ib()
    diameter = attr.ib()


class JSONSerializer:

    @functools.singledispatch
    def serialize(self, obj: Any) -> str:
        raise NotImplementedError(f"{obj:!r}")

    @functools.singledispatch
    def deserialize(self, data: str) -> Any:
        raise NotImplementedError(f"{data:!r}")

    @serialize.register(Quantity)
    def _serialize_quantity(self, quantity: Quantity) -> str:
        ...

    @deserialize.register(Quantity)
    def _deserialize_quantity(self, data: str) -> Quantity:
        ...

    @serialize.register(Pipe)
    def _serialize_pipe(self, pipe: Pipe) -> str:
        ...

    @deserialize.register(Pipe)
    def _deserialize_pipe(self, data: str) -> Pipe:
        ...


class XMLSerializer(JSONSerializer):
    pass


class YAMLSerializer(JSONSerializer):
    pass


class Test:

    @pytest.fixture(
        params=[JSONSerializer, XMLSerializer, YAMLSerializer]
    )
    def serializer(self, request):
        return request.param()

    def test_quantity(self, serializer):
        quantity = Quantity(10, "m")
        data = serializer.serialize(quantity)
        new_quantity = serializer.deserialize(data)
        assert new_quantity == quantity

    def test_pipe(self, serializer):
        pipe = Pipe(
            length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
        )
        data = serializer.serialize(pipe)
        new_pipe = serializer.deserialize(data)
        assert new_pipe == pipe
