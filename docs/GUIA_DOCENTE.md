# Guía para montar el prototipo en GitHub Classroom

## 1. Subir la plantilla a GitHub

1. Crea un repositorio nuevo en GitHub (por ejemplo `plantilla-autograding`).
2. Sube el contenido de esta carpeta:
   ```bash
   git init
   git add .
   git commit -m "Plantilla inicial"
   git branch -M main
   git remote add origin https://github.com/<tu-usuario>/plantilla-autograding.git
   git push -u origin main
   ```
3. En **Settings → General**, marca **Template repository**.

## 2. Crear la tarea en GitHub Classroom

1. Entra a <https://classroom.github.com> y crea un *Classroom* para el curso.
2. **New assignment → Individual assignment**.
3. En *Starter code*, elige el repositorio `plantilla-autograding`.
4. En *Autograding* no hace falta agregar pruebas: el archivo
   `.github/workflows/classroom.yml` ya las define (3 ejercicios, 100 puntos).
5. Comparte el enlace de invitación con el grupo piloto.

Cada estudiante recibe su propia copia del repositorio. Al hacer `push`, las
pruebas se ejecutan y el puntaje aparece en el panel de Classroom del docente.

## 3. Agregar nuevos ejercicios

1. Crea `ejercicios/ejercicioN.py` con la descripción y la función vacía.
2. Crea `tests/test_ejercicioN.py` con las pruebas (usa mensajes claros en los `assert`;
   son la retroalimentación que verá el estudiante).
3. Copia un bloque `autograding-command-grader` en `classroom.yml`, cambia `id`,
   `command` y `max-score`, y agrégalo a `env` y `runners` del reporte.

## 4. Plan de prueba con el grupo piloto

**Participantes:** 8–15 compañeros de Programación.

**Grupos:**
- *Antes (línea base):* una tarea entregada de la forma tradicional.
- *Después (prototipo):* una tarea equivalente usando este repositorio.

**Métricas:**

| Métrica | Cómo se mide |
|---|---|
| Tiempo hasta recibir retroalimentación | Tradicional: fecha de entrega → fecha de nota del docente. Prototipo: hora del `push` → hora del resultado en Actions (se ve en la pestaña Actions). |
| Número de intentos | Cantidad de `push` por estudiante (historial de commits). |
| Puntaje final | Panel de GitHub Classroom. |
| Utilidad percibida | Encuesta (abajo). |

## 5. Encuesta corta (5 minutos)

Escala: 1 = Totalmente en desacuerdo … 5 = Totalmente de acuerdo

1. Recibí la retroalimentación lo suficientemente rápido para corregir mis errores.
2. Los mensajes de las pruebas me ayudaron a entender qué estaba mal.
3. Fue fácil ver mi resultado en GitHub (pestaña Actions).
4. Corregí mi código al menos una vez gracias a la retroalimentación automática.
5. Me gustaría usar este sistema en otras materias de programación.

Preguntas abiertas:

6. ¿Cuánto tiempo aproximado tardaste en saber si tu ejercicio estaba bien?
7. ¿Qué fue lo más difícil de usar?
8. ¿Qué mejorarías?

> Sugerencia: crea la encuesta en Google Forms o Microsoft Forms y comparte el enlace
> junto con la invitación de Classroom.
