# Clonar el repositorio
- git clone URL del repositorio
- cd nombre-del-repositorio

# Crear un entorno virtual
python -m venv env

# Activar el entorno virtual
-En Windows:
env\Scripts\activate

-En macOS/Linux:
source env/bin/activate

# Instala las dependencias
pip install -r requirements.txt

# Crea la base de datos local para el proyecto:
CREATE DATABASE nombre_de_tu_base_de_datos;

# Configura las variables de entorno:
Copia el archivo .env.example y llamalo .env.local
Ajusta las variables según sea necesario

# Corre las migraciones
python manage.py migrate

# Corre el servidor
python manage.py runserver

# Crea una aplicación de la siguiente manera:
## Creación de la app:
python manage.py startapp nombre_de_la_app
## Crea los archivos serializer.py y urls.py dentro de la app a partir del example.
## Migrar la app:
- python manage.py makemigrations
- python manage.py migrate
