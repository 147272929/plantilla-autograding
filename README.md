# Tarea de Programación con calificación automática

Este repositorio contiene 3 ejercicios de Python. Cada vez que haces `git push`,
GitHub Actions ejecuta pruebas automáticas y te dice **en minutos** qué está bien
y qué debes corregir. Ya no tienes que esperar a que el docente revise tu entrega.

## Ejercicios

| Ejercicio | Archivo | Puntos |
|---|---|---|
| 1. Números pares | `ejercicios/ejercicio1.py` | 30 |
| 2. Factorial | `ejercicios/ejercicio2.py` | 30 |
| 3. Palíndromos | `ejercicios/ejercicio3.py` | 40 |

Lee el comentario al inicio de cada archivo y reemplaza el `pass` por tu solución.
**No modifiques la carpeta `tests/`.**

## Cómo ver tu retroalimentación

1. Sube tus cambios:
   ```bash
   git add .
   git commit -m "Resuelvo ejercicio 1"
   git push
   ```
2. En GitHub, abre la pestaña **Actions** de tu repositorio.
3. Entra a la última ejecución de **Calificación automática**.
   - ✅ verde: el ejercicio pasó todas las pruebas.
   - ❌ rojo: abre el paso del ejercicio para ver qué prueba falló y el mensaje de ayuda.
4. Al final verás tu puntaje total (sobre 100).

Puedes hacer `push` todas las veces que quieras antes de la fecha de entrega.

## Probar en tu computadora (opcional)

```bash
pip install -r requirements.txt
python -m pytest -v
```
