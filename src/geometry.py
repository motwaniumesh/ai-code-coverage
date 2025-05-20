class Geometry:
    PI = 3.14159
    
    @staticmethod
    def circle_area(radius: float) -> float:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return Geometry.PI * radius ** 2
    
    @staticmethod
    def circle_perimeter(radius: float) -> float:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 2 * Geometry.PI * radius
    
    @staticmethod
    def rectangle_area(length: float, width: float) -> float:
        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive")
        return length * width
    
    @staticmethod
    def triangle_area_using_heron(side1: float, side2: float, side3: float) -> float:
        sides = [side1, side2, side3]
        if any(s <= 0 for s in sides):
            raise ValueError("All sides must be positive")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Invalid triangle sides")
        
        s = sum(sides) / 2
        return (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    
    @staticmethod
    def is_right_angled_triangle(side1: float, side2: float, side3: float) -> bool:
        sides = sorted([side1, side2, side3])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9