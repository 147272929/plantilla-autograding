# Tarea de Programación con calificación automática

Este repositorio contiene 3 ejercicios de Python. Cada vez que haces `git push`,
GitHub Actions ejecuta pruebas automáticas y te dice **en minutos** qué está bien
y qué debes corregir. Ya no tienes que esperar a que el docente revise tu entrega.

## Cómo empezar (una sola vez)

1. Arriba en esta página, pulsa **Use this template → Create a new repository**.
2. Ponle de nombre `tarea-programacion-<tu-usuario>` y elige **Private**.
3. En tu nuevo repositorio ve a **Settings → Collaborators → Add people** y agrega
   al usuario de GitHub de tu docente, para que pueda ver tu trabajo y tus notas.
4. Clona **tu** repositorio en tu computadora y trabaja ahí:
   ```bash
   git clone https://github.com/<tu-usuario>/tarea-programacion-<tu-usuario>.git
   ```

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
3. Entra a la última ejecución de **Calificación automática** (tarda ~20 segundos).
4. Baja hasta **Resultado de tu entrega**: verás una tabla con ✅/❌ por ejercicio,
   tu puntaje total (sobre 100) y la lista **Qué debes corregir** con un mensaje
   de ayuda por cada prueba que falló.

Puedes hacer `push` todas las veces que quieras antes de la fecha de entrega.

## Probar en tu computadora (opcional)

```bash
pip install -r requirements.txt
python -m pytest -v
```
