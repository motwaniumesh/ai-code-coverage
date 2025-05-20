import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-20T15:32:33.160060)
def test_circle_area_positive_radius():
    assert Geometry.circle_area(5) == 78.53975

def test_circle_area_zero_radius():
    assert Geometry.circle_area(0) == 0

def test_circle_area_negative_radius():
    with pytest.raises(ValueError):
        Geometry.circle_area(-5)

def test_circle_perimeter_positive_radius():
    assert Geometry.circle_perimeter(5) == 31.4159

def test_circle_perimeter_zero_radius():
    assert Geometry.circle_perimeter(0) == 0

def test_circle_perimeter_negative_radius():
    with pytest.raises(ValueError):
        Geometry.circle_perimeter(-5)

def test_rectangle_area_positive_dimensions():
    assert Geometry.rectangle_area(3, 4) == 12

def test_rectangle_area_zero_dimension():
    assert Geometry.rectangle_area(5, 0) == 0

def test_rectangle_area_negative_dimension():
    with pytest.raises(ValueError):
        Geometry.rectangle_area(-3, 4)

def test_triangle_area_using_heron_positive_sides():
    assert Geometry.triangle_area_using_heron(3, 4, 5) == 6

def test_triangle_area_using_heron_invalid_sides():
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(1, 1, 3)

def test_triangle_area_using_heron_negative_sides():
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(-3, 4, 5)

def test_is_right_angled_triangle_right_angled_triangle():
    assert Geometry.is_right_angled_triangle(3, 4, 5) == True

def test_is_right_angled_triangle_not_right_angled_triangle():
    assert Geometry.is_right_angled_triangle(3, 4, 6) == False

def test_is_right_angled_triangle_negative_sides():
    assert Geometry.is_right_angled_triangle(-3, 4, 5) == False