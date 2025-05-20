import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-20T15:16:57.098451)
# content of test_geometry.py

import pytest
from src.geometry import Geometry

class TestGeometry:
    @pytest.mark.parametrize("radius, expected_area", [
        (0, 0),
        (1, 3.14159),
        (2, 12.56636),
        (10, 314.159),
    ])
    def test_circle_area(self, radius, expected_area):
        assert Geometry.circle_area(radius) == pytest.approx(expected_area, 0.00001)

    @pytest.mark.parametrize("radius, expected_perimeter", [
        (0, 0),
        (1, 6.28318),
        (2, 12.56636),
        (10, 62.8318),
    ])
    def test_circle_perimeter(self, radius, expected_perimeter):
        assert Geometry.circle_perimeter(radius) == pytest.approx(expected_perimeter, 0.00001)

    @pytest.mark.parametrize("length, width, expected_area", [
        (1, 1, 1),
        (2, 3, 6),
        (10, 0.5, 5),
    ])
    def test_rectangle_area(self, length, width, expected_area):
        assert Geometry.rectangle_area(length, width) == expected_area

    @pytest.mark.parametrize("side1, side2, side3, expected_area", [
        (3, 4, 5, 6),
        (1, 1, 1, 0.4330127),
        (5, 12, 13, 30),
    ])
    def test_triangle_area_using_heron(self, side1, side2, side3, expected_area):
        assert Geometry.triangle_area_using_heron(side1, side2, side3) == pytest.approx(expected_area, 0.00001)

    @pytest.mark.parametrize("side1, side2, side3, expected_result", [
        (3, 4, 5, True),
        (5, 12, 13, True),
        (1, 1, 1, False),  # This is not a right-angled triangle
    ])
    def test_is_right_angled_triangle(self, side1, side2, side3, expected_result):
        assert Geometry.is_right_angled_triangle(side1, side2, side3) == expected_result

    def test_circle_area_negative_radius(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            Geometry.circle_area(-1)

    def test_circle_perimeter_negative_radius(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            Geometry.circle_perimeter(-1)

    def test_rectangle_area_negative_dimensions(self):
        with pytest.raises(ValueError, match="Dimensions must be positive"):
            Geometry.rectangle_area(5, -2)

    def test_triangle_area_using_heron_invalid_triangle(self):
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Geometry.triangle_area_using_heron(1, 2, 3)