"""
Crear una clase GlobalCounter que:
- Sea un singleton usando __new__
- Permita incrementar, decrementar y reset del contador
- Tenga múltiples contadores con nombres (como un diccionario)
- Permita obtener el valor actual de cualquier contador
- Tenga un método para listar todos los contadores
"""

class GlobalCounter:
    _instance = None
    _counters = {}
    # TODO: Implementar singleton con __new__
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    # TODO: Implementar increment, decrement, reset, get_value, list_counters

    def increment(self, counter_name):
        if counter_name in self._counters:
            self._counters[counter_name] += 1
            return
        self._counters.update({counter_name: 1})
    
    def decrement(self, counter_name):
        self._counters[counter_name] -= 1
    
    def reset(self, counter_name):
        self._counters[counter_name] = 0

    def get_value(self, counter_name):
        return self._counters[counter_name]

    def list_counters(self):
        print(self._counters)