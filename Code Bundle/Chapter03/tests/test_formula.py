import math

import pytest
import attr


class FormulaTokenizer(object):
    pass


@attr.s
class Formula(object):

    expr = attr.ib()

    @classmethod
    def from_string(cls, expr, tokenizer):
        return cls(expr)

    def eval(self, **kwargs):
        kwargs.update(
            {
                n: getattr(math, n)
                for n in dir(math)
                if not n.startswith("_")
            }
        )
        return eval(self.expr, kwargs)


def test_formula_parsing():
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string("C0 * x + 10", tokenizer)
    assert formula.eval(x=1.0, C0=2.0) == pytest.approx(12.0)

    formula = Formula.from_string("sin(x) + 2 * cos(x)", tokenizer)
    assert formula.eval(x=0.7) == pytest.approx(2.1739021)

    formula = Formula.from_string("log(x) + 3", tokenizer)
    assert formula.eval(x=2.71828182846) == pytest.approx(4.0)


def test_formula_parsing2():
    values = [
        ("C0 * x + 10", dict(x=1.0, C0=2.0), 12.0),
        ("sin(x) + 2 * cos(x)", dict(x=0.7), 2.1739021),
        ("log(x) + 3", dict(x=2.71828182846), 4.0),
    ]
    tokenizer = FormulaTokenizer()
    for formula, inputs, result in values:
        formula = Formula.from_string(formula, tokenizer)
        assert formula.eval(**inputs) == pytest.approx(result)


@pytest.mark.parametrize(
    "formula, inputs, result",
    [
        ("C0 * x + 10", dict(x=1.0, C0=2.0), 12.0),
        ("sin(x) + 2 * cos(x)", dict(x=0.7), 2.1739021),
        ("log(x) + 3", dict(x=2.71828182846), 4.0),
        pytest.param(
            "hypot(x, y)",
            dict(x=3, y=4),
            5.0,
            marks=pytest.mark.xfail(reason="not implemented: #102"),
        ),
    ],
)
def test_formula(formula, inputs, result):
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string(formula, tokenizer)
    assert formula.eval(**inputs) == pytest.approx(result)


@pytest.mark.parametrize(
    "formula, inputs, result",
    [
        pytest.param("x + 3", dict(x=1.0), 4.0, id="add"),
        pytest.param("x - 1", dict(x=6.0), 5.0, id="sub"),
    ],
)
def test_formula_simple(formula, inputs, result):
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string(formula, tokenizer)
    assert formula.eval(**inputs) == pytest.approx(result)


class TestSeparated:

    def test_formula_linear(self):
        tokenizer = FormulaTokenizer()
        formula = Formula.from_string("C0 * x + 10", tokenizer)
        assert formula.eval(x=1.0, C0=2.0) == pytest.approx(12.0)

    def test_formula_sin_cos(self):
        tokenizer = FormulaTokenizer()
        formula = Formula.from_string(
            "sin(x) + 2 * cos(x)", tokenizer
        )
        assert formula.eval(x=0.7) == pytest.approx(2.1739021)

    def test_formula_log(self):
        tokenizer = FormulaTokenizer()
        formula = Formula.from_string("log(x) + 3", tokenizer)
        assert formula.eval(x=2.71828182846) == pytest.approx(4.0)
