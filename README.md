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

