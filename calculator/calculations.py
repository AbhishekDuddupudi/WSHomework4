class Calculations:
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls):
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str):
        """Find and return calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
