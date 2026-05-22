# 🍳 GourmetWeb - Plataforma de Gestión de Recetas

GourmetWeb es una aplicación web desarrollada en **Python 3** utilizando el framework **Django**. Este proyecto ha sido diseñado siguiendo rigurosamente el patrón arquitectónico **MTV (Modelo - Template - Vista)** 

---

## 🏗️ Arquitectura y Estructura del Patrón MTV

La aplicación divide de forma estricta sus responsabilidades en tres capas diferenciadas para garantizar la mantenibilidad y un código limpio (PEP8):

* **Modelo (`recetas/models.py`):** Define la estructura de datos en la base de datos SQLite local. Cuenta con un modelo principal `Receta` compuesto por campos de texto corto, texto largo, fecha de creación automatizada (`auto_now_add`) y una relación de clave foránea (`ForeignKey`) vinculada al modelo nativo `User` de Django para asociar la autoría.
* **Vista (`recetas/views.py`):** Implementa la lógica de negocio mediante **Vistas Basadas en Clases (CBVs)** (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`). Cuenta con un robusto sistema de control de accesos gracias a `LoginRequiredMixin` y `UserPassesTestMixin`, asegurando que solo el creador del contenido o un miembro del **Staff (Excepción de Administración)** puedan modificar o eliminar registros.
* **Template (`templates/`):** La capa de presentación se gestiona de forma centralizada en la raíz del proyecto. Implementa **herencia de plantillas** a partir de un archivo común `base.html` y utiliza lógica de renderizado dinámico para adaptar el menú superior según el estado de autenticación del usuario.

---

## 🌟 Funcionalidades Adicionales Implementadas

Para alcanzar la máxima calificación en los apartados de desarrollo avanzado e interfaz de usuario, se han integrado de forma nativa las siguientes dos características adicionales:

1.  **🔍 Sistema de Búsqueda y Filtrado Avanzado (Q Objects):**
    El catálogo principal no es estático; incorpora una barra de búsqueda inteligente en la cabecera. Al realizar una consulta, la vista filtra de forma simultánea y no excluyente la base de datos buscando coincidencia de texto tanto en el **Título** como en la **Descripción** de la receta empleando operadores lógicos `Q` de Django (`Q(titulo__icontains=query) | Q(descripcion__icontains=query)`).
2.  **🎨 Integración del Framework CSS Bootstrap 5:**
    Se transformó por completo el diseño HTML plano en una interfaz moderna, completamente responsiva (adaptada a dispositivos móviles) y visualmente atractiva. Se aplicaron clases estéticas a todos los listados, botones y formularios dinámicos. Asimismo, las alertas nativas de **Django Messages** (mensajes de éxito o denegación de permisos) están sincronizadas con las clases cromáticas de Bootstrap (`success` y `danger`).

---

## 🛠️ Instrucciones de Instalación y Despliegue Local

Siga estos pasos en orden cronológico en su terminal para levantar el proyecto en su entorno local:

---

## Instalación Local
### 1. Clonar el repositorio y acceder a la raíz

```bash
git clone <url-del-repositorio>
```

### 2. Crear y activar el entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar (Linux/macOS)
source venv/bin/activate

# Activar (Windows)
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

### 6 Cargar los datos iniciales
```bash
python manage.py loaddata recetas_iniciales
```

### 7. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre **http://127.0.0.1:8000** en tu navegador.

---