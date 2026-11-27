# Actividad práctica 2 · Construye tu pipeline

Repositorio de la actividad: módulo de descuentos con pruebas automatizadas y un pipeline de
integración continua (GitHub Actions) que **detecta el defecto, bloquea el cambio y valida la corrección**.

## Contenido

| Archivo | Para qué sirve |
|---|---|
| `descuentos.py` | Módulo bajo prueba (`calcular_total`). |
| `test_descuentos.py` | 17 casos automatizados con pytest (incluye los valores límite 9, 10 y 11). |
| `hoja_seguimiento.csv` | Hoja de seguimiento de los casos, resultados y defectos. |
| `.github/workflows/ci.yml` | Pipeline: pruebas, cobertura mínima del 80 % y reportes como artefacto. |

## Flujo de la actividad

1. Subir `main` con el pipeline (la primera ejecución falla por el defecto del límite).
2. Registrar una incidencia con el enlace a la ejecución fallida.
3. Crear la rama `fix/descuento-limite`, cambiar `>` por `>=` en `descuentos.py` y abrir un pull request.
4. Proteger `main`: exigir pull request y que la verificación `pruebas` termine en verde.
5. Fusionar el pull request y revisar los reportes del artefacto `reportes-de-pruebas`.
