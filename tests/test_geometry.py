import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-20T15:22:14.867773)
from src.geometry import Geometry
import pytest

class TestGeometry:

    def test_circle_area_positive_radius(self):
        assert Geometry.circle_area(1) == 3.14159

    def test_circle_area_zero_radius(self):
        assert Geometry.circle_area(0) == 0

    def test_circle_area_negative_radius(self):
        with pytest.raises(ValueError):
            Geometry.circle_area(-1)

    def test_circle_perimeter_positive_radius(self):
        assert Geometry.circle_perimeter(1) == 6.28318

    def test_circle_perimeter_zero_radius(self):
        assert Geometry.circle_perimeter(0) == 0

    def test_circle_perimeter_negative_radius(self):
        with pytest.raises(ValueError):
            Geometry.circle_perimeter(-1)

    def test_rectangle_area_positive_dimensions(self):
        assert Geometry.rectangle_area(2, 3) == 6

    def test_rectangle_area_zero_dimensions(self):
        assert Geometry.rectangle_area(0, 0) == 0

    def test_rectangle_area_negative_dimensions(self):
        with pytest.raises(ValueError):
            Geometry.rectangle_area(-2, 3)

    def test_triangle_area_using_heron_positive_sides(self):
        assert Geometry.triangle_area_using_heron(3, 4, 5) == 6

    def test_triangle_area_using_heron_zero_sides(self):
        assert Geometry.triangle_area_using_heron(0, 0, 0) == 0

    def test_triangle_area_using_heron_negative_sides(self):
        with pytest.raises(ValueError):
            Geometry.triangle_area_using_heron(-3, 4, 5)

    def test_triangle_area_using_heron_invalid_triangle(self):
        with pytest.raises(ValueError):
            Geometry.triangle_area_using_heron(2, 3, 7)

    def test_is_right_angled_triangle_right_triangle(self):
        assert Geometry.is_right_angled_triangle(3, 4, 5) == True

    def test_is_right_angled_triangle_wrong_triangle(self):
        assert Geometry.is_right_angled_triangle(1, 2, 3) == False