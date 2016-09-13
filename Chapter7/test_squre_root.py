from pylsy import pylsytable
import math
from mysqrt import mysqrt

def test_squre_root():
    while True:
        attributes = ["a", "mysqrt(a)", "math.sqrt(a)", "diff"]
        table = pylsytable(attributes)
        a = ["1.0", "2.0", "3.0", "4.0", "5.0","6.0","7.0","8.0","9.0"]
        for i in range(8):
            m = mysqrt(a,5)
            n = math.sqrt(a)
            y = abs(m - n)
            table.add_data("a", a)
            table.add_data("diff",y)
            table.add_data("mysqrt(a)",m)
            table.add_data("math.sqrt(a)",n)
            table.create_table()

test_squre_root()
