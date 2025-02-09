# Guía de Instalación y Ejecución del Proyecto Django

## Requisitos Previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python** (Versión recomendada: `>=3.13.0`)
- **pip** (Gestor de paquetes de Python)
- **virtualenv** (Opcional, pero recomendado)
- **Git** (Opcional, pero recomendado)

Para verificar si tienes Python y pip instalados, ejecuta:
```sh
python --version
pip --version
```
Si no los tienes, descárgalos desde [Python.org](https://www.python.org/downloads/).

---

## Instalación del Proyecto

### Crear un Entorno Virtual (Opcional, pero recomendado)
Para evitar conflictos de dependencias, crea un entorno virtual con:
```sh
python -m venv venv
```
Luego, actívalo:
- En Windows:
  ```sh
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```sh
  source venv/bin/activate
  ```

### Instalar Dependencias
Ejecuta el siguiente comando para instalar las dependencias necesarias:
```sh
pip install -r requirements.txt
```

---

## Ejecución del Proyecto

### Aplicar Migraciones de la Base de Datos
Antes de ejecutar el servidor, aplica las migraciones necesarias:
```sh
python manage.py migrate
```

### Crear un Superusuario (Opcional)
Si necesitas acceso al panel de administración de Django, crea un superusuario:
```sh
python manage.py createsuperuser
```
Sigue las instrucciones e ingresa un nombre de usuario, correo y contraseña.

### Iniciar el Servidor de Desarrollo
Para ejecutar la aplicación en modo desarrollo, usa:
```sh
python manage.py runserver
```
Esto iniciará el servidor en `http://127.0.0.1:8000/`.

---

# **Documentación de la API - Orders API**

## **Base URL**
```
http://127.0.0.1:8000/
```

## **Endpoints Disponibles**

### **1 Obtener todas las Órdenes**
**`GET /orders/`**  
Obtiene la lista de todas las Ordenes.

#### **Respuesta Esperada**
```json
[
    {
        "orderId": "1001",
        "customerName": "Juan Pérez",
        "totalPrice": "250.00",
        "posId": "POS001",
        "createdAt": "2025-02-09T12:00:00Z",
        "status": "pending"
    },
    {
        "orderId": "1002",
        "customerName": "María López",
        "totalPrice": "320.50",
        "posId": "POS002",
        "createdAt": "2025-02-09T12:05:00Z",
        "status": "completed"
    }
]
```

---

### **2  Obtener una orden por ID**
**`GET /orders/{orderId}/`**  
Obtiene una orden específica.

#### **Parámetros**
- `orderId` (string) **ID de la orden a consultar.**

#### **Respuesta Esperada**
```json
{
    "orderId": "1001",
    "customerName": "Juan Pérez",
    "totalPrice": "250.00",
    "posId": "POS001",
    "createdAt": "2025-02-09T12:00:00Z",
    "status": "pending"
}
```

---

### **3 Crear una orden**
**`POST /orders/`**  
Crea una nueva orden en el sistema.

#### **Cuerpo de la Solicitud (`application/json`)**
```json
{
    "orderId": "1003",
    "customerName": "Carlos Díaz",
    "totalPrice": "150.75",
    "posId": "POS003"
}
```

#### **Respuesta Esperada (`201 Created`)**
```json
{
    "orderId": "1003",
    "customerName": "Carlos Díaz",
    "totalPrice": "150.75",
    "posId": "POS003",
    "createdAt": "2025-02-09T12:10:00Z",
    "status": "pending"
}
```

---

### **4 Actualizar una orden**
**`PUT /orders/{orderId}/`**  
Actualiza completamente una orden existente.

#### **Parámetros**
- `orderId` (string) **ID de la orden a actualizar.**

#### **Cuerpo de la Solicitud (`application/json`)**
```json
{
    "orderId": "1003",
    "customerName": "Carlos Díaz",
    "totalPrice": "200.00",
    "posId": "POS003",
    "status": "completed"
}
```

#### **Respuesta Esperada (`200 OK`)**
```json
{
    "orderId": "1003",
    "customerName": "Carlos Díaz",
    "totalPrice": "200.00",
    "posId": "POS003",
    "createdAt": "2025-02-09T12:10:00Z",
    "status": "completed"
}
```

---

### **5 Eliminar una orden**
**`DELETE /orders/{orderId}/`**  
Elimina una orden específica.

#### **Parámetros**
- `orderId` (string) **ID de la orden a eliminar.**

#### **Respuesta Esperada (`204 No Content`)**
```
Orden eliminada exitosamente.
```

---

### **6 Cargar Órdenes desde un archivo Excel**
**`POST /orders/uploadExcel/`**  
Permite subir un archivo Excel (`.xlsx`) con múltiples órdenes.

#### **Parámetros de la Solicitud**
- **Formato:** `multipart/form-data`
- **Archivo:** `file` (Subir archivo `.xlsx`)

#### **Ejemplo de Archivo Excel**
| orderId | customerName  | totalPrice | posId  |
|---------|--------------|------------|--------|
| 1004    | Ana Torres   | 280.00     | POS004 |
| 1005    | Luis Méndez  | 320.50     | POS005 |

#### **Respuesta Esperada (`201 Created`)**
```json
{
    "message": "Orders uploaded successfully",
    "orders": [
        {
            "orderId": "1004",
            "customerName": "Ana Torres",
            "totalPrice": "280.00",
            "posId": "POS004",
            "createdAt": "2025-02-09T12:20:00Z",
            "status": "completed"
        },
        {
            "orderId": "1005",
            "customerName": "Luis Méndez",
            "totalPrice": "320.50",
            "posId": "POS005",
            "createdAt": "2025-02-09T12:25:00Z",
            "status": "completed"
        }
    ]
}
```

---

