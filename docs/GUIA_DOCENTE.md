# Guía del prototipo (solo con GitHub)

> GitHub Classroom se retiró el 28 de agosto de 2026. Este prototipo funciona
> solo con GitHub: un **repositorio plantilla** + **GitHub Actions**. No requiere
> organización, plan de pago ni plataformas externas.

## Cómo funciona

```
Plantilla pública ──"Use this template"──▶ Repositorio privado de cada estudiante
                                                   │ git push
                                                   ▼
                                     GitHub Actions ejecuta las pruebas
                                                   │ ~20 segundos
                                                   ▼
                     Resumen: ✅/❌ por ejercicio, puntaje /100, qué corregir
```

1. **La plantilla** (`147272929/plantilla-autograding`) tiene los ejercicios
   vacíos, las pruebas y el workflow de calificación. Es pública: cualquiera ve los
   enunciados y las pruebas, pero **nunca** debe contener soluciones.
2. **Cada estudiante** crea su copia privada con *Use this template* y agrega al
   docente como colaborador (pasos en el `README.md`).
3. **Cada `git push`** ejecuta `.github/workflows/calificacion.yml`:
   instala Python, corre las pruebas de cada ejercicio (30 + 30 + 40 puntos) y
   escribe el resumen de retroalimentación con `.github/scripts/resumen.py`.
4. **El estudiante** ve su resultado en la pestaña **Actions** de su repositorio y
   puede corregir y volver a enviar cuantas veces quiera.
5. **El docente** abre la pestaña **Actions** del repositorio de cada estudiante
   para ver la nota y el historial de intentos.

## Agregar nuevos ejercicios

1. Crea `ejercicios/ejercicioN.py` con la descripción y la función vacía.
2. Crea `tests/test_ejercicioN.py`. Pon un mensaje claro en cada `assert`: es la
   retroalimentación que verá el estudiante.
3. En `.github/scripts/resumen.py`, agrega el ejercicio al diccionario
   `EJERCICIOS` con su nombre y puntos.
4. En `calificacion.yml`, copia un bloque `autograding-command-grader`, cambia
   `id`, `command` y `max-score`, y agrégalo a `env` y `runners` del reporte.

Los cambios solo llegan a los repositorios creados **después**; los estudiantes que
ya tienen su copia no los reciben.

## Plan de prueba con el grupo piloto

**Participantes:** 8–15 compañeros de Programación.

**Comparación:**
- *Antes (línea base):* una tarea entregada de la forma tradicional.
- *Después (prototipo):* una tarea equivalente usando esta plantilla.

**Métricas:**

| Métrica | Cómo se mide |
|---|---|
| Tiempo hasta recibir retroalimentación | Tradicional: fecha de entrega → fecha en que el docente devuelve la nota. Prototipo: duración de la ejecución en la pestaña Actions (~20 s). |
| Número de intentos | Cantidad de ejecuciones en Actions por estudiante. |
| Puntaje final | Última ejecución en Actions ("Puntaje total"). |
| Utilidad percibida | Encuesta (abajo). |

## Encuesta corta (5 minutos)

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

> Sugerencia: crea la encuesta en Google Forms o Microsoft Forms.

## Limitaciones del prototipo

- No hay un panel central de notas: el docente revisa cada repositorio.
- Un estudiante podría modificar las pruebas en su copia. Para el piloto basta con
  revisar que la carpeta `tests/` no cambió (historial de commits).
- Cuentas gratis: 2000 minutos de Actions al mes en repositorios privados; cada
  calificación usa menos de 1 minuto.
