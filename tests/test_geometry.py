import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-21T11:50:23.855821)
def test_circle_area():
    assert Geometry.circle_area(0) == 0
    assert Geometry.circle_area(1) == 3.14159
    assert Geometry.circle_area(5) == 78.53975
    try:
        Geometry.circle_area(-1)
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"

def test_circle_perimeter():
    assert Geometry.circle_perimeter(0) == 0
    assert Geometry.circle_perimeter(1) == 6.28318
    assert Geometry.circle_perimeter(5) == 31.4159
    try:
        Geometry.circle_perimeter(-1)
    except ValueError as e:
        assert str(e) == "Radius cannot be negative"

def test_rectangle_area():
    assert Geometry.rectangle_area(0, 0) == 0
    assert Geometry.rectangle_area(2, 3) == 6
    assert Geometry.rectangle_area(4.5, 7.8) == 35.1
    try:
        Geometry.rectangle_area(-1, 2)
    except ValueError as e:
        assert str(e) == "Dimensions must be positive"

def test_triangle_area_using_heron():
    assert Geometry.triangle_area_using_heron(3, 4, 5) == 6.0
    assert Geometry.triangle_area_using_heron(6, 8, 10) == 24.0
    try:
        Geometry.triangle_area_using_heron(-2, 3, 4)
    except ValueError as e:
        assert str(e) == "All sides must be positive"
    try:
        Geometry.triangle_area_using_heron(1, 2, 3)
    except ValueError as e:
        assert str(e) == "Invalid triangle sides"

def test_is_right_angled_triangle():
    assert Geometry.is_right_angled_triangle(3, 4, 5) is True
    assert Geometry.is_right_angled_triangle(5, 12, 13) is True
    assert Geometry.is_right_angled_triangle(7, 24, 25) is True
    assert Geometry.is_right_angled_triangle(8, 15, 17) is True
    assert Geometry.is_right_angled_triangle(5, 5, 5) is False
    try:
        Geometry.is_right_angled_triangle(-3, 4, 5)
    except ValueError as e:
        assert str(e) == "All sides must be positive"