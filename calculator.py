#!/usr/bin/env python3
"""Ein simpler CLI-Rechner für Grundrechenarten."""


def calculate(a: float, operator: str, b: float) -> float:
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Division durch 0 ist nicht erlaubt.")
        return a / b
    raise ValueError(f"Unbekannter Operator: {operator}")


def main() -> None:
    print("=== Simpler Rechner ===")
    print("Unterstützte Operatoren: +, -, *, /")

    try:
        a = float(input("Erste Zahl: ").strip())
        operator = input("Operator: ").strip()
        b = float(input("Zweite Zahl: ").strip())

        result = calculate(a, operator, b)
        print(f"Ergebnis: {result}")
    except ValueError as err:
        print(f"Eingabefehler: {err}")
    except ZeroDivisionError as err:
        print(f"Rechenfehler: {err}")


if __name__ == "__main__":
    main()
