from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs): # no importan la cantidad de argumentos posicionales ni nombrados, la funcion los recibe.
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("pasaron" + str(time_elapsed.total_seconds()) + " segundos")

    return wrapper

@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Ricardo"):
    print("Hola " + nombre)
suma(2,4)
random_func() 
saludo("Richard")