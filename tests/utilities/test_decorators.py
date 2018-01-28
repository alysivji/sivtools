"""Tests for decorators in the toolbox"""

from sivtools.utilities.decorators import print_, timer


def test_print_(capsys):
    # Arrange
    @print_
    def my_func(arg1, arg2, kwarg1=1):
        return (arg1, arg2, kwarg1)

    # Act
    my_func(1, 2, 'a')

    # Assert
    out, err = capsys.readouterr()
    assert out.startswith("(1, 2, 'a')")


def test_timer(capsys):
    # Arrange
    DELAY = .1

    @timer()
    def my_func(arg1, arg2, kwarg1=1):
        import time
        time.sleep(DELAY)
        return (arg1, arg2, kwarg1)

    # Act
    my_func(1, 1, 'a')

    # Assert
    out, err = capsys.readouterr()
    elapsed_time = float(out.split(':')[1].split('s')[0])
    assert elapsed_time >= DELAY
