import pytest
from src.geometry import Geometry

def test_positive_radius():
        assert Geometry.circle_area(2) == pytest.approx(12.56636, abs=1e-4)
        assert Geometry.circle_area(1.5) == pytest.approx(7.06858, rel=1e-4)

def test_zero_radius():
        """Test edge case of zero radius"""
        assert Geometry.circle_area(0) == 0

# Auto-generated tests (2025-05-20T15:17:40.683724)
# test_geometry.py

import pytest
from src.geometry import Geometry

class TestGeometry:
    def test_circle_area(self):
        assert Geometry.circle_area(0) == 0
        assert Geometry.circle_area(5) == 78.53975
        with pytest.raises(ValueError):
            Geometry.circle_area(-1)

    def test_circle_perimeter(self):
        assert Geometry.circle_perimeter(0) == 0
        assert Geometry.circle_perimeter(5) == 31.4159
        with pytest.raises(ValueError):
            Geometry.circle_perimeter(-1)

    def test_rectangle_area(self):
        assert Geometry.rectangle_area(0, 5) == 0
        assert Geometry.rectangle_area(4, 3) == 12
        with pytest.raises(ValueError):
            Geometry.rectangle_area(-1, 5)
    
    def test_triangle_area_using_heron(self):
        assert Geometry.triangle_area_using_heron(3, 4, 5) == 6
        assert Geometry.triangle_area_using_heron(6, 8, 10) == 24
        assert Geometry.triangle_area_using_heron(10, 15, 20) == 72.61843774138907
        with pytest.raises(ValueError):
            Geometry.triangle_area_using_heron(-3, 4, 5)

    def test_is_right_angled_triangle(self):
        assert Geometry.is_right_angled_triangle(3, 4, 5) == True
        assert Geometry.is_right_angled_triangle(5, 12, 13) == True
        assert Geometry.is_right_angled_triangle(6, 8, 10) == True
        assert Geometry.is_right_angled_triangle(5, 5, 8) == False