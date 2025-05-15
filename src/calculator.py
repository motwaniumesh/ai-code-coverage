class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def __init__(self):
        self.last_result = 0
        
    def add(self, a: float, b: float) -> float:
        """Add two numbers and store the result."""
        self.last_result = a + b
        return self.last_result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a and store the result."""
        self.last_result = a - b
        return self.last_result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and store the result."""
        self.last_result = a * b
        return self.last_result
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b and store the result.
        
        Args:
            a (float): numerator
            b (float): denominator
            
        Returns:
            float: result of division
            
        Raises:
            ValueError: if attempting to divide by zero
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        self.last_result = a / b
        return self.last_result
    
    def get_last_result(self) -> float:
        """Return the last calculated result."""
        return self.last_result
    
    def clear_last_result(self) -> None:
        """Clear the last result by setting it to 0."""
        self.last_result = 0