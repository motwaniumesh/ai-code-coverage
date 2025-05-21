import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-21T11:53:57.673004)
def test_circle_area_positive_radius():
    radius = 5
    expected_area = Geometry.PI * radius ** 2
    assert Geometry.circle_area(radius) == expected_area

def test_circle_area_zero_radius():
    radius = 0
    expected_area = 0
    assert Geometry.circle_area(radius) == expected_area

def test_circle_area_negative_radius():
    with pytest.raises(ValueError):
        Geometry.circle_area(-2)

def test_circle_perimeter_positive_radius():
    radius = 5
    expected_perimeter = 2 * Geometry.PI * radius
    assert Geometry.circle_perimeter(radius) == expected_perimeter

def test_circle_perimeter_zero_radius():
    radius = 0
    expected_perimeter = 0
    assert Geometry.circle_perimeter(radius) == expected_perimeter

def test_circle_perimeter_negative_radius():
    with pytest.raises(ValueError):
        Geometry.circle_perimeter(-2)

def test_rectangle_area_positive_dimensions():
    length, width = 4, 3
    expected_area = length * width
    assert Geometry.rectangle_area(length, width) == expected_area

def test_rectangle_area_negative_dimensions():
    with pytest.raises(ValueError):
        Geometry.rectangle_area(-4, 3)
    with pytest.raises(ValueError):
        Geometry.rectangle_area(4, -3)

def test_triangle_area_using_heron_valid_triangle():
    side1, side2, side3 = 5, 12, 13
    s = sum([side1, side2, side3]) / 2
    expected_area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    assert Geometry.triangle_area_using_heron(side1, side2, side3) == expected_area

def test_triangle_area_using_heron_invalid_triangle_sides():
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(10, 20, 30)

def test_triangle_area_using_heron_negative_side():
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(5, -12, 13)

def test_is_right_angled_triangle_valid_right_triangle():
    side1, side2, side3 = 3, 4, 5
    assert Geometry.is_right_angled_triangle(side1, side2, side3)

def test_is_right_angled_triangle_invalid_right_triangle():
    side1, side2, side3 = 3, 4, 6
    assert not Geometry.is_right_angled_triangle(side1, side2, side3)

def test_is_right_angled_triangle_negative_side():
    with pytest.raises(ValueError):
        Geometry.is_right_angled_triangle(3, 4, -5)