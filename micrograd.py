class Value:
    def __init__(self, value, children=(), op=None, label=None):
        self._value = value
        self._op = op
        self._children = set(children)
        self._label = label

    def __repr__(self):
        return f'Value({self._value})'

    def graph_str(self):
        label = f'{self._label}|' if self._label else ''
        label += f'p={self._value}'
        return label

    def __add__(self, other):
        other_value = other if isinstance(other, Value) else Value(other)
        return Value(self._value + other_value._value, (self, other_value), '+')

    
