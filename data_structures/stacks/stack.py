from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass


class Stack(Generic[T]):
    """A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit: int = 10):
        self.stack: list[T] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def apilar(self, data: T) -> None:
        """Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def desapilar(self) -> T:
        """
        Pop an element off of the top of the stack.

        >>> Stack().pop()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()

    def cima(self) -> T:
        """
        Peek at the top-most element of the stack.

        >>> Stack().pop()
        Traceback (most recent call last):
            ...
        data_structures.stacks.stack.StackUnderflowError
        """
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]

    def esta_vacia(self) -> bool:
        """Check if a stack is empty."""
        return not bool(self.stack)

    def esta_llena(self) -> bool:
        return self.tamanio() == self.limit

    def tamanio(self) -> int:
        """Return the size of the stack."""
        return len(self.stack)

    def __contains__(self, item: T) -> bool:
        """Check if item is in stack"""
        return item in self.stack


def test_stack() -> None:
    """
    >>> test_stack()
    """
    stack: Stack[int] = Stack(10)
    assert bool(stack) is False
    assert stack.esta_vacia() is True
    assert stack.esta_llena() is False
    assert str(stack) == "[]"

    try:
        _ = stack.desapilar()
        raise AssertionError()  # This should not happen
    except StackUnderflowError:
        assert True  # This should happen

    try:
        _ = stack.cima()
        raise AssertionError()  # This should not happen
    except StackUnderflowError:
        assert True  # This should happen

    for i in range(10):
        assert stack.tamanio() == i
        stack.apilar(i)

    assert bool(stack)
    assert not stack.esta_vacia()
    assert stack.esta_llena()
    assert str(stack) == str(list(range(10)))
    assert stack.desapilar() == 9
    assert stack.cima() == 8

    stack.apilar(100)
    assert str(stack) == str([0, 1, 2, 3, 4, 5, 6, 7, 8, 100])

    try:
        stack.apilar(200)
        raise AssertionError()  # This should not happen
    except StackOverflowError:
        assert True  # This should happen

    assert not stack.esta_vacia()
    assert stack.tamanio() == 10

    assert 5 in stack
    assert 55 not in stack


if __name__ == "__main__":
    test_stack()
