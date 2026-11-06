"""
Genera un resumen de retroalimentación en español a partir del reporte JUnit
de pytest. Si existe la variable GITHUB_STEP_SUMMARY (GitHub Actions), el
resumen se escribe ahí; si no, se imprime en pantalla.

Uso: python .github/scripts/resumen.py reporte.xml
"""

import os
import sys
import xml.etree.ElementTree as ET

EJERCICIOS = {
    "test_ejercicio1": ("Ejercicio 1 - Números pares", 30),
    "test_ejercicio2": ("Ejercicio 2 - Factorial", 30),
    "test_ejercicio3": ("Ejercicio 3 - Palíndromos", 40),
}


def leer_resultados(ruta):
    resultados = {clave: [] for clave in EJERCICIOS}
    for caso in ET.parse(ruta).iter("testcase"):
        modulo = caso.get("classname", "").split(".")[-1]
        if modulo not in resultados:
            continue
        fallo = caso.find("failure")
        if fallo is None:
            fallo = caso.find("error")
        mensaje = None
        if fallo is not None:
            mensaje = (fallo.get("message") or "Error").splitlines()[0]
            for prefijo in ("AssertionError: ", "Failed: "):
                mensaje = mensaje.replace(prefijo, "")
        resultados[modulo].append((caso.get("name"), mensaje))
    return resultados


def construir_resumen(resultados):
    lineas = ["## Resultado de tu entrega", ""]
    lineas += ["| Ejercicio | Pruebas superadas | Puntos |", "|---|---|---|"]
    total = 0
    for clave, (nombre, puntos) in EJERCICIOS.items():
        casos = resultados[clave]
        ok = sum(1 for _, msg in casos if msg is None)
        completo = casos and ok == len(casos)
        obtenidos = puntos if completo else 0
        total += obtenidos
        icono = "✅" if completo else "❌"
        lineas.append(f"| {icono} {nombre} | {ok}/{len(casos)} | {obtenidos}/{puntos} |")
    lineas += ["", f"**Puntaje total: {total}/100**", ""]

    fallos = [
        (EJERCICIOS[clave][0], prueba, msg)
        for clave, casos in resultados.items()
        for prueba, msg in casos
        if msg is not None
    ]
    if fallos:
        lineas += ["### Qué debes corregir", ""]
        for nombre, prueba, msg in fallos:
            lineas.append(f"- **{nombre}** → `{prueba}`: {msg}")
        lineas += ["", "Corrige tu código y vuelve a hacer `git push` para recalificar."]
    else:
        lineas.append("🎉 ¡Todo correcto! Superaste todas las pruebas.")
    return "\n".join(lineas) + "\n"


def main():
    resumen = construir_resumen(leer_resultados(sys.argv[1]))
    destino = os.environ.get("GITHUB_STEP_SUMMARY")
    if destino:
        with open(destino, "a", encoding="utf-8") as f:
            f.write(resumen)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(resumen)


if __name__ == "__main__":
    main()
