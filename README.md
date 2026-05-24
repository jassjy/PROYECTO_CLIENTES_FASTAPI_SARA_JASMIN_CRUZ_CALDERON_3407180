# Proyecto nombre_pro_clientes

---

# Información del Aprendiz

**Nombre:** Sara Jasmin Cruz Calderon  
**Programa de Formación:** Tecnólogo en Análisis y Desarrollo de Software (ADSO)  

---

# Descripción del Proyecto

El presente proyecto fue desarrollado utilizando **Python** y el framework **FastAPI**, con el propósito de practicar la creación de APIs, endpoints y rutas dinámicas.

La aplicación permite:

- Crear endpoints básicos.
- Retornar mensajes personalizados.
- Mostrar listas de clientes.
- Utilizar parámetros dinámicos en las rutas.

El proyecto fue realizado con **Visual Studio Code** utilizando un entorno virtual de Python.

---

# Objetivos del Proyecto

- Comprender el funcionamiento básico de FastAPI.
- Implementar endpoints utilizando el método GET.
- Manipular parámetros en rutas dinámicas.
- Ejecutar aplicaciones web locales utilizando Uvicorn.
- Organizar correctamente la estructura de un proyecto backend.

---

# Herramientas Utilizadas

| Tecnología | Descripción |
| Python | Lenguaje de programación principal |
| FastAPI | Framework para construcción de APIs |
| Uvicorn | Servidor ASGI para ejecutar FastAPI |
| Visual Studio Code | Entorno de desarrollo |

---

# Procedimiento Realizado

## 1. Creación de la carpeta del proyecto

```bash
mkdir nombre_pro_clientes
```

Este comando se utiliza para crear una nueva carpeta llamada **nombre_pro_clientes**, donde se almacenarán todos los archivos y recursos del proyecto.

---

## 2. Acceso a la carpeta del proyecto

```bash
cd nombre_pro_clientes
```

Este comando permite ingresar a la carpeta del proyecto para comenzar a trabajar en ella.

---

## 3. Creación del entorno virtual

```bash
python -m venv venv
```

Este comando se utiliza para crear un entorno virtual en Python, permitiendo instalar las librerías del proyecto de forma organizada e independiente.

---

## 4. Activación del entorno virtual

```bash
venv\Scripts\activate
```

Este comando se utiliza para activar el entorno virtual previamente creado en el proyecto.

---

## 5. Instalación de dependencias

```bash
pip install "fastapi[standard]"
```

Este comando se utiliza para instalar FastAPI junto con sus dependencias recomendadas para un funcionamiento más completo del proyecto.

---

## 6. Creación del archivo principal

Se creó el archivo:

```text
main.py
```

`main.py` es el archivo principal del proyecto donde se escribe el código de la aplicación FastAPI.

---

## 7. Ejecución del servidor

```bash
fastapi dev main.py
```

Este comando se utiliza para ejecutar la aplicación FastAPI en modo desarrollo.

---

# Endpoints Implementados

## Endpoint Principal

### Ruta

```text
/
```

### Función

Retorna un mensaje principal relacionado con el proyecto.

---

## Endpoint Clientes

### Ruta

```text
/clientes
```

### Función

Retorna una lista de clientes registrados.

### Clientes registrados

- Camilo Villarruel
- Mateo Palacios
- Silvana Estrada

---

## Endpoint Saludo Personalizado

### Ruta

```text
/saludar/{nombre}
```

### Ejemplo

```text
/saludar/CamiloVillarruel
```

### Función

Retorna un saludo personalizado utilizando parámetros dinámicos.

---

## Endpoint Nombre y Apellido

### Ruta

```text
/saludar/{nombre}/{apellido}
```

### Ejemplo

```text
/saludar/Mateo/Palacios
```

### Función

Retorna un saludo utilizando nombre y apellido.

---

## Endpoint con Parámetro de Edad

### Ruta

```text
/saludar/Silvana/Estrada?edad=15
```

### Función

Retorna un saludo incluyendo un parámetro adicional de edad mediante query parameters.

---

# Estructura del Proyecto

```text
nombre_pro_clientes/
│
├── venv/
├── main.py
└── README.md
```

---

