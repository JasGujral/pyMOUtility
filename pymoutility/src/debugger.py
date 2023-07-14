"""Utilities to help you debug your code better."""


from typing import Callable, Any, Union, Dict
from functools import wraps
import logging
import time
import inspect


def timeit(output: Union[logging.Logger, Callable[..., None]]):
    """
    Decorator to log the start, end and runtime of a function.

    Args:
        output: Logger instance or print function used for output.
    """
    def decorator_log_time(func: Callable):
        """
        Decorator function.
        """
        @wraps(func)
        def wrapper_log_time(*args, **kwargs) -> Any:
            """
            Wrapper function.
            """
            start_time = time.time()
            
            if isinstance(output, logging.Logger):
                output.info(f'Started execution of {func.__name__} function')
            else:
                output(f'Started execution of {func.__name__} function')
            
            result = func(*args, **kwargs)
            
            end_time = time.time()
            run_time = end_time - start_time

            if isinstance(output, logging.Logger):
                output.info(f'Finished execution of {func.__name__} function, runtime: {run_time} seconds')
            else:
                output(f'Finished execution of {func.__name__} function, runtime: {run_time} seconds')

            return result

        return wrapper_log_time

    return decorator_log_time


def debugger(output: Union[logging.Logger, Callable[..., None]]):
    """
    Decorator for debugging purposes.

    Logs the function name, arguments and output.

    Args:
        output: Logger instance or print function used for output.
    """
    def decorator_debug(func: Callable):
        """
        Decorator function.
        """
        func_sig = inspect.signature(func)
        @wraps(func)
        def wrapper_debug(*args, **kwargs) -> Any:
            """
            Wrapper function.
            """
            bound_args = func_sig.bind(*args, **kwargs)
            bound_args.apply_defaults()        
            
            if isinstance(output, logging.Logger):
                output.debug(f"Calling {func.__name__}({bound_args.arguments})")
            else:
                output(f"Calling {func.__name__}({bound_args.arguments})")

            result = func(*args, **kwargs)

            if isinstance(output, logging.Logger):
                output.debug(f"{func.__name__!r} returned {result!r}")   
            else:
                output(f"{func.__name__!r} returned {result!r}") 

            return result

        return wrapper_debug

    return decorator_debug


class FunctionCounter:
    """
    A class that keeps a count of calls to multiple functions.

    When used as a decorator, it increments the count for the
    decorated function each time the function is called.
    """
    function_counts: Dict[str, int] = {}

    def __init__(self, func: Callable[..., Any]):
        self.func: Callable[..., Any] = func
        self.function_counts[func.__name__] = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.function_counts[self.func.__name__] += 1
        return self.func(*args, **kwargs)

    @classmethod
    def get_counts(cls) -> Dict[str, int]:
        """Returns the funciton names and call counts for the decorated functions.

        Returns:
            Dict[str, int]: Dictionary of function names and counts of calls.
        """
        return cls.function_counts
