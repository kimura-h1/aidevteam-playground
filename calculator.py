"""小さな計算の関数（AI Development Team の実証用。外部の依存なし）。"""


def add(a: float, b: float) -> float:
    """a と b の和。"""
    return a + b


def subtract(a: float, b: float) -> float:
    """a から b を引いた差。"""
    return a - b


def multiply(a: float, b: float) -> float:
    """a と b の積。"""
    return a * b


def divide(a: float, b: float) -> float:
    """a を b で割った商。b が 0 なら ValueError。"""
    if b == 0:
        raise ValueError("0 では割れない")
    return a / b
