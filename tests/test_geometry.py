import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-21T14:11:41.650308)
# test_geometry.py

import pytest
from src.geometry import Geometry

def test_circle_area():
    assert Geometry.circle_area(0) == 0
    assert Geometry.circle_area(1) == pytest.approx(3.14159)
    with pytest.raises(ValueError):
        Geometry.circle_area(-1)

def test_circle_perimeter():
    assert Geometry.circle_perimeter(0) == 0
    assert Geometry.circle_perimeter(1) == pytest.approx(6.28318)
    with pytest.raises(ValueError):
        Geometry.circle_perimeter(-1)

def test_rectangle_area():
    assert Geometry.rectangle_area(0, 5) == 0
    assert Geometry.rectangle_area(2, 3) == 6
    with pytest.raises(ValueError):
        Geometry.rectangle_area(-1, 4)

def test_triangle_area_using_heron():
    assert Geometry.triangle_area_using_heron(3, 4, 5) == 6
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(-1, 2, 3)
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(1, 2, 3)

def test_is_right_angled_triangle():
    assert Geometry.is_right_angled_triangle(3, 4, 5) is True
    assert Geometry.is_right_angled_triangle(2, 2, 2) is False
    with pytest.raises(ValueError):
        Geometry.is_right_angled_triangle(-3, 4, 5)