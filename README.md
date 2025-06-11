# 🧾 Proyecto Fullstack – Suscripciones con Stripe (React + Django + Docker)

Este proyecto implementa una aplicación fullstack funcional para gestionar suscripciones mensuales mediante **Stripe Checkout**, cumpliendo con los requerimientos del reto técnico de Pai.

Incluye:

* Backend en **Django + SQLite** 
* Frontend en **Vite + React + TypeScript**
* Contenedores Docker para backend y frontend
* Pruebas unitarias en backend

---

## ⚙ Tecnologías utilizadas

| Componente    | Tecnología                                       |
| ------------- | ------------------------------------------------ |
| Frontend      | Vite + React + TypeScript                        |
| Backend       | Django 5 + Python 3.11                           |
| Base de datos | SQLite3                                          |
| API externa   | Stripe Checkout (modo test)                      |
| Contenedores  | Docker + Docker Compose                          |
| Tests         | Django TestCase                                  |

---

## 🚀 Instrucciones de instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <repo-url>
cd <carpeta-del-proyecto>
```

### 2. Variables de entorno

#### Backend (`Backend/.env`)

```env
STRIPE_SECRET_KEY=sk_test_xxx
STRIPE_PUBLIC_KEY=pk_test_xxx
```

> Asegúrate de usar claves de modo **test** de tu cuenta de Stripe.

### 3. Construir y levantar contenedores

```bash
docker-compose up --build
```

* Backend: [http://localhost:8000](http://localhost:8000)
* Frontend: [http://localhost:5173](http://localhost:5173)

---

## 🧪 Pruebas

### 📌 Backend (Django)

Ubicadas en `Backend/subscriptions/tests.py`

```bash
docker-compose exec backend python manage.py test subscriptions
```



## 📄 Descripción funcional

### 1. Pantalla principal

Formulario para suscribirse:

* Input: Nombre
* Input: Correo electrónico
* Botón: "Suscribirse"

Envía los datos al backend, que:

* Crea el `Customer` en Stripe
* Crea una `Checkout Session`
* Devuelve la URL del Checkout
* Guarda al suscriptor localmente en SQLite

El frontend redirige al Checkout de Stripe.

---

### 2. Pantalla de Dashboard

Después del pago, el usuario es redirigido a:

```
/dashboard?session_id=cs_test_...
```

El frontend:

* Llama al backend con ese `session_id`
* El backend consulta a Stripe y responde con:

  * Nombre
  * Correo
  * Estado de la suscripción (`active`, `incomplete`)

El dashboard muestra esta información al usuario.

---

## 🧪 Tarjetas de prueba Stripe

| Escenario            | Número de tarjeta   | Expiración | CVC | Resultado          |
| -------------------- | ------------------- | ---------- | --- | ------------------ |
| Pago exitoso (Visa)  | 4242 4242 4242 4242 | 12/34      | 123 | Éxito              |
| Fondos insuficientes | 4000 0000 0000 9995 | 12/34      | 123 | Rechazado          |
| Tarjeta robada       | 4100 0000 0000 0019 | 12/34      | 123 | Rechazo por fraude |


## 🔗 Enlaces opcionales

* [Dashboard de Stripe](https://dashboard.stripe.com/test)
* Checkout real de ejemplo (opcional):
  [https://checkout.stripe.com/c/pay/cs\_test\_xxxxxxxxxxx](https://checkout.stripe.com/c/pay/cs_test_xxxxxxxxxxx)

---

## 📁 Estructura de carpetas

```
Pai/
├── Backend/
│   ├── pai_backend/
│   ├── subscriptions/  
│   ├── manage.py
│   ├── db.sqlite3
├── Frontend/
│   ├── src/
│   ├── index.html
├── Infra
│   ├── Frontend.Dockerfile
│   ├── Backend.Dockerfile
│   ├── Compose.yml
├── README.md
```

