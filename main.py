import Adafruit_GPIO.MCP230xx as MCP
import Adafruit_GPIO as GPIO
from enum import Enum
class MCP:
    def __init__(self, i2c_address, max_bit):
        self.i2c_address = i2c_address
        self._mcp = MCP.MCP23017(address = i2c_address)
        if self._mcp is None:
            raise Exception("Unable to instantiate MCP")
        self.bit_range = range(0, max_bit)
        for b in self.bit_range:
            self._mcp.setup(b, GPIO.OUT)
            # self._mcp.pullup(b, True)


class CalcKeys(Enum):
    K0 = 0
    K1 = 1
    K3 = 2
    K4 = 3
    K5 = 4
    K6 = 6
    K7 = 7
    K8 = 8
    K9 = 9
    KCLEAR = 10
    KPRINT = 11

    @classmethod
    def set_of_keys(cls):
        return set(cls.__members__.values())

class CalcDriver:
    def __init__(self, mcp, **init_dict):
        self.key_map = init_dict.copy()
        
        # make sure all keys are there
        assert len(set(self.key_map.keys()) - CalcKeys.set_of_keys()) == 0
