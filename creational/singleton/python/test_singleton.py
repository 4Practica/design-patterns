from .global_counter import GlobalCounter

def test_global_counter():
    counter1 = GlobalCounter()
    counter2 = GlobalCounter()
    
    # Verificar singleton
    assert counter1 is counter2, "No es singleton"
    
    # Probar funcionalidad
    counter1.increment("visits")
    counter1.increment("visits")
    counter1.increment("errors")
    
    counter2.increment("visits")  # Desde otra instancia
    counter2.decrement("errors")
    
    assert counter1.get_value('visits') == 3
    assert counter2.get_value('errors') == 0
    
    counter1.list_counters()
    print("✓ Ejercicio 2 completado")