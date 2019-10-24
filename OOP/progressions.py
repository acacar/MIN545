class Progression:

    def __init__(self, start, stop):
        self._current = start
        self._end = stop

    def next(self):
        # 1. save current value to temp
        tmp = self._current
        # 2. advance
        if self._current is not None:
            self._advance()
        # 3. check if you need to stop
        self._checkstop()
        # 4. return saved current value
        return tmp

    # All progression classes themselves are iterators
    def __iter__(self):
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        return self.next()
    
    def peek(self):
        return self._current
    
    def _advance(self):
        pass

    def _checkstop(self):
        if self._current == self._end:
            self._current = None
            


class ArithmeticProgression(Progression):

    def __init__(self, start=0, stop=None, step=1):
        super().__init__(start, stop)
        self._step = step

    # We are "Overriding" the parent's _advance
    def _advance(self):
        self._current += self._step


class GeometricProgression(Progression):

    def __init__(self, start=1, stop=None, multiplier=2):
        super().__init__(start, stop)
        self._multiplier = multiplier

    def _advance(self):
        self._current *= self._multiplier


class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1, stop=None):
        super().__init__(first, stop)
        self._next = second
        
    def _advance(self):
        # equivalent to:
        # self._current, self._next = self._next, self._current + self._next
        tmp = self._current + self._next
        self._current = self._next
        self._next = tmp

    
