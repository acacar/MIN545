import math

class Circle:

    def __init__(self, r=1):
        self._radius = self._validate_dimension(r)

    def radius(self, r=None):
        if r is None:
            return self._radius
        else:
            self._radius = self._validate_dimension(r)

    def diameter(self, d=None):
        if d is None:
            return 2*self.radius()
        else:
            self.radius(self._validate_dimension(d)/2.0)

    def area(self, a=None):
        if a is None:
            return math.pi * (self.radius() ** 2)
        else:
            self.radius(math.sqrt(self._validate_dimension(a) / (math.pi)))

    def _validate_dimension(self, d):
        try:
            d = float(d)
        except ValueError:
            raise ValueError("Circle dimensions must be numeric")
        if d < 0.0:
            raise ValueError("Circle dimensions must be non-negative")
        return d
            
    def __str__(self):
        return f"Circle({self._radius:.3})"

    def __repr__(self):
        return str(self)


### Exception raise and catch examples:

def foo(x):
    return bar(x)

def bar(x):
    try:
        return 2 * baz(x)
    except ArithmeticError:
        print("The baz call failed, retrying")
        return 2 * baz(x + 0.000001)
    except TypeError:
        pass

    
def baz(x):
    return  1.0 / x


def bat(x):
    pass
