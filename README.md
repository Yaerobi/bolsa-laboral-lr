[![codecov](https://codecov.io/gh/Yaerobi/bolsa-laboral-lr/branch/main/graph/badge.svg?token=XHDLECG321)](https://codecov.io/gh/Yaerobi/bolsa-laboral-lr)


# bolsa-laboral-lr
Bolsa de Trabajo de La Rioja


# Levantar el sistema de backend.

Para levantar el sistema de backend debemos tener instalado Python 3.9+. Luego
ejecutar los siguientes pasos:

  1. Crear virtual environment

  ```bash
  python3 -m venv venv
  ````

  2. Entrar al venv

  ```bash
  source venv/bin/activate
  ```

  3. Instalar los requrimientos

  ```bash
  pip install -r requriments.txt
  ```

  4. Exportar nombre de la app

  ```bash
  export FLASK_APP=manage.py
  ```

  5. Ejecutar migraciones

  ```bash
  python manage.py db upgrade
  ```

  6. Ejecutar app

  ```bash
  python manage.py run
  ```

Se accede al `127.0.0.1:5000` y en la raiz se encuentra el swagger.
