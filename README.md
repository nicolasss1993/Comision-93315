# Hospital — Gestión de Departamentos y Médicos

Proyecto final de la cursada de Python Flex (Coderhouse, Comisión 93315). Es una aplicación web desarrollada con **Django** para la gestión interna de un hospital: administración de departamentos médicos, médicos y usuarios del sistema.

## Descripción del proyecto

La aplicación permite a personal administrativo autenticado llevar el registro de los **departamentos médicos** del hospital (con su cantidad de médicos, email de contacto, etc.) y del **staff médico**, asociando a cada médico una especialidad. Cada usuario cuenta con un perfil propio (con avatar, país, dirección y fecha de nacimiento) y debe iniciar sesión para acceder a la información del hospital.

- **Propósito:** ofrecer un panel interno simple para dar de alta, consultar, editar y eliminar departamentos y médicos.
- **Problema que resuelve:** centraliza en una sola aplicación datos que suelen estar dispersos (planillas, papeles) sobre la estructura médica de un hospital.
- **Usuario objetivo:** personal administrativo o de sistemas del hospital que necesita gestionar esta información desde un panel web.

## Funcionalidades principales

- **Panel de administración (Django Admin):** gestión de departamentos, médicos, especialidades y usuarios desde `/admin/`.
- **Registro y autenticación de usuarios:** alta de cuenta, login y logout con un modelo de usuario propio (`usuarios.Usuario`, extendiendo `AbstractUser`).
- **Perfil de usuario:** visualización y edición de datos personales (nombre, apellido, país, dirección, fecha de nacimiento, avatar y contraseña).
- **ABM de Departamentos Médicos:** listado (con búsqueda por nombre), detalle, alta, edición y baja, con validaciones propias (email del dominio `@hospital.com` y número de departamento único).
- **ABM de Médicos:** listado (con búsqueda por nombre), detalle, alta, edición y baja, implementado con vistas genéricas de Django (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`), asociando cada médico a una especialidad.
- **Acceso protegido:** todas las vistas de negocio requieren estar autenticado (`@login_required` / `LoginRequiredMixin`), redirigiendo al login si no hay sesión activa.

## Estructura del proyecto

```
Comision-93315/
├── hospital/          # Configuración del proyecto (settings, urls raíz, wsgi/asgi)
├── core/               # App de Departamentos Médicos (home + CRUD de departamentos)
├── medicos/            # App de Médicos y Especialidades
├── usuarios/           # App de Usuarios (registro, login/logout, perfil)
├── media/              # Archivos subidos por usuarios (avatares)
├── requirements.txt    # Dependencias del proyecto
├── manage.py
└── db.sqlite3          # Base de datos de desarrollo (SQLite)
```

## Requisitos previos

- Python 3.12+ (probado con Django 5.2.17)
- pip
- (Recomendado) un entorno virtual: `venv`

## Instalación y ejecución local

1. **Clonar el repositorio**

   ```bash
   git clone <URL-del-repositorio>
   cd Comision-93315
   ```

2. **Crear y activar un entorno virtual**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. **Instalar las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones**

   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario** (para acceder al panel `/admin/`)

   ```bash
   python manage.py createsuperuser
   ```

6. **Levantar el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

7. Abrir el navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Rutas principales

| Ruta | Descripción |
|---|---|
| `/` | Home |
| `/depas/` | Listado de departamentos médicos |
| `/crear_depa/` | Alta de departamento médico |
| `/ver_depa/<nro_departamento>` | Detalle de un departamento |
| `/editar_depa/<nro_departamento>` | Edición de un departamento |
| `/medicos/` | Listado de médicos |
| `/medicos/crear/` | Alta de médico |
| `/medicos/<code>/` | Detalle de un médico |
| `/registro/` | Registro de nuevo usuario |
| `/login/` | Inicio de sesión |
| `/logout/` | Cierre de sesión |
| `/usuario/datos` | Perfil del usuario logueado |
| `/usuario/actualizar_datos` | Edición del perfil |
| `/admin/` | Panel de administración de Django |

## Despliegue

El proyecto está preparado para ejecutarse en un entorno de despliegue simple ajustando `ALLOWED_HOSTS` (ya incluye soporte para túneles de **ngrok**), `DEBUG=False` en producción, y ejecutando `python manage.py collectstatic` para servir los archivos estáticos.

## Tecnologías utilizadas

- [Django](https://www.djangoproject.com/) 5.2.17
- SQLite (base de datos de desarrollo)
- Pillow (manejo de imágenes / avatares)

## Autor

Nicolás Dziuma — Proyecto final, Curso de Python Flex, Comisión 93315 (Coderhouse)
