import logging

from pymoutility.src.debugger import debugger, timeit, FunctionCounter


class TestDebugger:
    """Test debugger utilities."""

    def test_timeit_print(self, capfd):
        """Test timeit decorator for print."""
        @timeit(print)
        def add(x: int, y: int = 10) -> int:
            return x + y

        add(10)
        captured = capfd.readouterr()
        assert (
            "Finished execution of add function, runtime:"
            in captured.out
        )

    def test_timeit_logger(self, caplog):
        """Test timeit decorator for logger."""
        logger = logging.getLogger("Test")
        caplog.set_level(logging.DEBUG)

        @timeit(logger)
        def add(x: int, y: int = 10) -> int:
            return x + y

        add(10)
        assert "Finished execution of add function, runtime:" in caplog.text
        
    def test_debugger_print(self, capfd):
        """Test debugger decorator for print."""
        @debugger(print)
        def add(x: int, y: int = 10) -> int:
            return x + y

        add(10)
        captured = capfd.readouterr()
        assert (
            "Calling add({'x': 10, 'y': 10})"
            in captured.out
        )

    def test_debugger_logger(self, caplog):
        """Test debugger decorator for logger."""
        logger = logging.getLogger("Test")
        caplog.set_level(logging.DEBUG)

        @debugger(logger)
        def add(x: int, y: int = 10) -> int:
            return x + y

        add(10)
        assert "Calling add({'x': 10, 'y': 10})" in caplog.text  
        
    def test_function_counter(self):
        """Test FunctionCounter decorator."""
        @FunctionCounter
        def addition(a: int, b:int) -> int:
            return a + b

        @FunctionCounter
        def hello_name(name: str):
            print(f"Hello! {name}")
        
        addition(2, 3)
        addition(4, 4)
        hello_name("Jasmeet")

        assert FunctionCounter.get_counts() == {'addition': 2, 'hello_name': 1}
