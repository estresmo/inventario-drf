# Sistema de Inventario

Sistema de Inventario para resolver prueba técnica usando Django Rest Framework con Json Web Tokens.

## Requerimientos

- Python >= 3.9

## Instalación

Ejecutar comandos en la terminal:

1. Clonar el repositorio
´´´
git clone https://github.com/estresmo/inventario-drf.git
´´´

2. Entrar al directorio del proyecto
´´´
cd inventario-drf
´´´

3. Crear un entorno virtual
´´´
python -m venv venv
´´´

4. Activar el entorno virtual
´´´
source venv/bin/activate
´´´

5. Instalar dependencias
´´´
pip install -r requirements.txt
´´´

6. Correr el servidor
´´´
python manage.py runserver
´´´

7. Acceder a la aplicación en http://127.0.0.1:8000/

## Estructura del proyecto

- inventario: API de inventario
- productos: API de productos y categorías
- clientes: API de clientes
- custom_auth: API de usuarios
- frontend: Vistas HTML
- static: Archivos estáticos
- templates: Archivos HTML
- core: Configuración de Django

## Por hacer

- Cambiar la locación del JSON Web Token de localStorage a http only cookie
- Paginación en el frontend

## Notas

Se uso la carpeta fronted unicamente para renderizar html, por comodidad para poder usar base.html como plantilla. La base de datos sqlite se subió con las migraciones hecha, para facilitar el uso de la aplicación.

## Autor

Juan Suarez