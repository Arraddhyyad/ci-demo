import pytest
from budget_impact import budget_impact

def test_basic():
    assert budget_impact(1000, 5000, 0.1) == 500000.0

def test_zero_uptake():
    assert budget_impact(1000, 5000, 0) == 0.0

def test_bad_uptake():
    with pytest.raises(ValueError):
        budget_impact(1000, 5000, 1.5)

def test_full_uptake():
    assert budget_impact(100, 1000, 1) == 100000.0
