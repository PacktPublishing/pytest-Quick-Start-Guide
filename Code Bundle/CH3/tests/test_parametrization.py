import functools
from enum import Enum
from typing import Any

import attr
import pytest


class ElementType(Enum):
    TRIANGLE = 1
    QUAD = 2
    TETRA = 3
    HEXA = 4
    PYRAMID = 5
    WEDGE = 6


def get_number_of_vertices(element_type):
    ...
    return {
        ElementType.TRIANGLE: 3,
        ElementType.QUAD: 4,
        ElementType.TETRA: 4,
        ElementType.HEXA: 8,
        ElementType.PYRAMID: 5,
        ElementType.WEDGE: 6,
    }[
        element_type
    ]


def get_number_of_sides(element_type):
    ...
    return {
        ElementType.TRIANGLE: 3,
        ElementType.QUAD: 4,
        ElementType.TETRA: 4,
        ElementType.HEXA: 6,
        ElementType.PYRAMID: 5,
        ElementType.WEDGE: 5,
    }[
        element_type
    ]


class TestBundled:

    def test_vertices_and_sides(self):
        assert get_number_of_vertices(ElementType.TRIANGLE) == 3
        assert get_number_of_sides(ElementType.TRIANGLE) == 3

        assert get_number_of_vertices(ElementType.QUAD) == 4
        assert get_number_of_sides(ElementType.QUAD) == 4

        assert get_number_of_vertices(ElementType.TETRA) == 4
        assert get_number_of_sides(ElementType.TETRA) == 4

        assert get_number_of_vertices(ElementType.HEXA) == 8
        assert get_number_of_sides(ElementType.HEXA) == 6

        assert get_number_of_vertices(ElementType.PYRAMID) == 5
        assert get_number_of_sides(ElementType.PYRAMID) == 5

        assert get_number_of_vertices(ElementType.WEDGE) == 6
        assert get_number_of_sides(ElementType.WEDGE) == 5


class TestSeparated:

    def test_triangle_vertices_and_sides(self):
        assert get_number_of_vertices(ElementType.TRIANGLE) == 3
        assert get_number_of_sides(ElementType.TRIANGLE) == 3

    def test_triangle_vertices_and_sides(self):
        assert get_number_of_vertices(ElementType.QUAD) == 4
        assert get_number_of_sides(ElementType.QUAD) == 4

    def test_triangle_vertices_and_sides(self):
        assert get_number_of_vertices(ElementType.TETRA) == 4
        assert get_number_of_sides(ElementType.TETRA) == 4

    def test_triangle_vertices_and_sides(self):
        assert get_number_of_vertices(ElementType.HEXA) == 8
        assert get_number_of_sides(ElementType.HEXA) == 6

    def test_triangle_vertices_and_sides(self):
        assert get_number_of_vertices(ElementType.PYRAMID) == 5
        assert get_number_of_sides(ElementType.PYRAMID) == 5

    def test_triangle_vertices_and_sides(self):
        assert get_number_of_vertices(ElementType.WEDGE) == 6
        assert get_number_of_sides(ElementType.WEDGE) == 5


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

    def deserialize_quantity(self, data: str) -> Quantity:
        ...

    def serialize_pipe(self, pipe: Pipe) -> str:
        ...

    def deserialize_pipe(self, data: str) -> Pipe:
        ...


class JSONSerializer:

    @functools.singledispatch
    def serialize(self, obj: Any) -> str:
        raise NotImplementedError(f"{obj:!r}")

    @functools.singledispatch
    def deserialize(self, data: str) -> Any:
        raise NotImplementedError(f"{obj:!r}")

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


class Test:

    def test_quantity(self):
        serializer = JSONSerializer()
        quantity = Quantity(10, "m")
        data = serializer.serialize(quantity)
        new_quantity = serializer.deserialize(data)
        assert new_quantity == quantity

    def test_pipe(self):
        serializer = JSONSerializer()
        pipe = Pipe(
            length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
        )
        data = serializer.serialize(pipe)
        new_pipe = serializer.deserialize(data)
        assert new_pipe == pipe


class XMLSerializer(JSONSerializer):
    pass


class YAMLSerializer(JSONSerializer):
    pass


class Test:

    def test_quantity(self):
        for serializer in [
            JSONSerializer(), XMLSerializer(), YAMLSerializer()
        ]:
            quantity = Quantity(10, "m")
            data = serializer.serialize(quantity)
            new_quantity = serializer.deserialize(data)
            assert new_quantity == quantity

    def test_pipe(self):
        for serializer in [
            JSONSerializer(), XMLSerializer(), YAMLSerializer()
        ]:
            pipe = Pipe(
                length=Quantity(1000, "m"),
                diameter=Quantity(35, "cm"),
            )
            data = serializer.serialize(pipe)
            new_pipe = serializer.deserialize(data)
            assert new_pipe == pipe


@pytest.mark.parametrize(
    "serializer_class",
    [JSONSerializer, XMLSerializer, YAMLSerializer],
)
class Test:

    def test_quantity(self, serializer_class):
        serializer = serializer_class()
        quantity = Quantity(10, "m")
        data = serializer.serialize(quantity)
        new_quantity = serializer.deserialize(data)
        assert new_quantity == quantity

    def test_pipe(self, serializer_class):
        serializer = serializer_class()
        pipe = Pipe(
            length=Quantity(1000, "m"), diameter=Quantity(35, "cm")
        )
        data = serializer.serialize(pipe)
        new_pipe = serializer.deserialize(data)
        assert new_pipe == pipe
