import pytest
from hiero_sdk_python.tokens.supply_type import SupplyType

def test_members():
    assert SupplyType.FINITE.value == 0
    assert SupplyType.INFINITE.value == 1

def test_name():
    assert SupplyType.FINITE.name == "FINITE"
    assert SupplyType.INFINITE.name == "INFINITE"

