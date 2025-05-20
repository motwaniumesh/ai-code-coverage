import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-20T15:32:02.156801)
def test_circle_area():
    assert Geometry.circle_area(0) == 0
    assert Geometry.circle_area(1) == Geometry.PI
    assert Geometry.circle_area(5) == 25 * Geometry.PI
    with pytest.raises(ValueError):
        Geometry.circle_area(-1)

def test_circle_perimeter():
    assert Geometry.circle_perimeter(0) == 0
    assert Geometry.circle_perimeter(1) == 2 * Geometry.PI
    assert Geometry.circle_perimeter(5) == 10 * Geometry.PI
    with pytest.raises(ValueError):
        Geometry.circle_perimeter(-1)

def test_rectangle_area():
    assert Geometry.rectangle_area(0, 0) == 0
    assert Geometry.rectangle_area(3, 4) == 12
    with pytest.raises(ValueError):
        Geometry.rectangle_area(-1, 2)
    with pytest.raises(ValueError):
        Geometry.rectangle_area(3, -4)

def test_triangle_area_using_heron():
    assert Geometry.triangle_area_using_heron(3, 4, 5) == 6
    assert Geometry.triangle_area_using_heron(6, 8, 10) == 24
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(1, 1, -1)
    with pytest.raises(ValueError):
        Geometry.triangle_area_using_heron(2, 4, 7)

def test_is_right_angled_triangle():
    assert Geometry.is_right_angled_triangle(3, 4, 5)
    assert not Geometry.is_right_angled_triangle(6, 8, 10)
    assert Geometry.is_right_angled_triangle(5, 12, 13)