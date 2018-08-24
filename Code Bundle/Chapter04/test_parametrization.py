import json

import attr
import pytest


@attr.s
class Quantity:
    value = attr.ib()
    unit = attr.ib()


@attr.s
class Pipe:
    length = attr.ib()
    diameter = attr.ib()


class JSONSerializer:

    def serialize_quantity(self, quantity: Quantity) -> str:
        ...
        return json.dumps(attr.asdict(quantity))

    def deserialize_quantity(self, data: str) -> Quantity:
        ...
        return Quantity(**json.loads(data))

    def serialize_pipe(self, pipe: Pipe) -> str:
        ...
        return json.dumps(attr.asdict(pipe))

    def deserialize_pipe(self, data: str) -> Pipe:
        ...
        d = json.loads(data)
        return Pipe(
            length=Quantity(**d["length"]),
            diameter=Quantity(**d["diameter"]),
        )


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
        data = serializer.serialize_quantity(quantity)
        new_quantity = serializer.deserialize_quantity(data)
        assert new_quantity == quantity

    def test_pipe(self, serializer):
        pipe = Pipe(
            length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
        )
        data = serializer.serialize_pipe(pipe)
        new_pipe = serializer.deserialize_pipe(data)
        assert new_pipe == pipe
