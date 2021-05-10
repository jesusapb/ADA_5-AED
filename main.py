from Tablero_Galton import *

if __name__ == "__main__":
    proceso = prueba_10 = Tablero_Galton(10000,7)
    proceso.construir_tablero_rutas()
    proceso.simular_recorridos()
    proceso.sacar_probabilidades()
    proceso.imprimir_resultados()