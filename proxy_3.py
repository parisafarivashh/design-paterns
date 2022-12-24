import logging
from typing import Union

logging.basicConfig(level=logging.INFO)


"""
def division(a: Union[int, float], b: Union[int, float]) -> float:
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        logging.error(f"Argument b cannot be {b}")

    except TypeError:
        logging.error(f"Arguments must be integers/floats")

print(division(1.9, 2))

You can see this function is already doing three things at once which violates the Single Responsibility Principle. 
SRP says that a function or class should have only one reason to change. 
In this case, a change in any of the three responsibilities can force the function to change. 
Also this means, changing or extending the function can be difficult to keep track of.
Instead, you can write two classes. 
The primary class Division will only implement the core logic while another class ProxyDivision will extend 
the functionality of Division by adding exception handlers and loggers.
"""

class Division:
    def div(self, a: Union[int, float], b: Union[int, float]) -> float:
        return a / b


class ProxyDivision:
    def __init__(self) -> None:
        self._klass = Division()

    def div(self, a: Union[int, float], b: Union[int, float]) -> float:
        try:
            result = self._klass.div(a, b)
            return result

        except ZeroDivisionError:
            logging.error(f"Argument b cannot be {b}")

        except TypeError:
            logging.error(f"Arguments must be integers/floats")


klass = ProxyDivision()
print(klass.div(2, 0))
