from src.thermo import thermo
import pytest

def test_thermo_us1():
    

def test_thermo_us4():
    rst = thermo(None)
    assert rst == 0

def test_thermo_us5():
    temperature = [1] * 100001
    with pytest.raises(ValueError):
        thermo(temperature)