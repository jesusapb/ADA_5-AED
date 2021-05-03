from Tablero_galuar import *

if __name__ == "__main__":
    proceso = prueba_10 = Tablero_galuar(100)
    proceso.construir_tablero_rutas()
    proceso.simular_recorridos()
    proceso.sacar_probabilidades()
    proceso.imprimir_resultados()