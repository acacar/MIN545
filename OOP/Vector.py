
class Vector:

    def __init__(self, from_list = None, d = 2):
        if from_list is None:
            self._coords = [0.0] * d
        else:
            self._coords = [0.0] * len(from_list)
            for i in range(len(from_list)):
                self._coords[i] = float(from_list[i])


    def __str__(self):
        newstr = "< "
        if len(self) == 0:
            return "< >"
        for i in self._coords:
            newstr += str(i) + ", "
        return newstr[:-2] + " >"

    def __repr__(self):
        return str(self)
    
    def __getitem__(self, k):
        return self._coords[k]

    def __setitem__(self, k, v):
        self._coords[k] = float(v)

    def __len__(self):
        return len(self._coords)
        
    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                result = Vector(d=len(self))
                for i in range(len(self)):
                    result[i] = self[i] + other[i]
                return result
            else:
                raise(IndexError("Dimension mismatch!"))
        else:
            raise(TypeError("Works only with vector!"))    

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) == len(other):
                result = 0
                for i in range(len(self)):
                    result += self[i] * other[i]
                return result
            else:
                raise(IndexError("Dimension mismatch!"))
        elif isinstance(other, (int, float)):
            result = Vector(d=len(self))
            for i in range(len(self)):
                result[i] = self[i] * other
            return result
        else:
            raise(TypeError("Works only with vector!"))    

v1 = Vector(from_list=[43.3,34.3,4])
v2 = Vector(from_list=[3,2,1])
v3 = Vector(d=2)
v4 = Vector(from_list=[1,2,3])
