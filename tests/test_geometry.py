import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-21T15:15:38.137430)
def test_circle_area():
    assert Geometry.circle_area(0) == 0
    assert Geometry.circle_area(1) == 3.14159
    assert Geometry.circle_area(5) == 78.53975
    with pytest.raises(ValueError):
        Geometry.circle_area(-3)

def test_circle_perimeter():
    assert Geometry.circle_perimeter(0) == 0
    assert Geometry.circle_perimeter(1) == 6.28318
    assert Geometry.circle_perimeter(5) == 31.4159
    with pytest.raises(ValueError):
        Geometry.circle_perimeter(-3)

def test_rectangle_area():
    assert Geometry.rectangle_area(0, 0) == 0
    assert Geometry.rectangle_area(3, 4) == 12
    with pytest.raises(ValueError):
        Geometry.rectangle_area(-2, 5)

def test_triangle_area_using_heron():
    assert Geometry.triangle_area_using_heron(3, 4, 5) == 6
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(1, 2, 3)

def test_is_right_angled_triangle():
    assert Geometry.is_right_angled_triangle(3, 4, 5) == True
    assert Geometry.is_right_angled_triangle(5, 12, 13) == True
    assert Geometry.is_right_angled_triangle(2, 2, 2) == False
    with pytest.raises(ValueError):
        Geometry.is_right_angled_triangle(-3, 4, 5)

def test_circle_diameter():
    assert Geometry.circle_diameter(0) == 0
    assert Geometry.circle_diameter(5) == 10