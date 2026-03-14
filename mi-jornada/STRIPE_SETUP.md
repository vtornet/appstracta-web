# Guía de Configuración de Stripe para Mi Jornada Premium

## Resumen del sistema

```
Usuario → Pulsa "Obtener Premium" → Stripe Checkout → Pago → Código Premium
                                                        ↓
                                            Backend genera código único
                                                        ↓
                                    Usuario recibe código y lo canjea en la app
```

---

## Paso 1: Obtener claves de Stripe

1. Ve a https://dashboard.stripe.com/
2. Regístrate o inicia sesión
3. Ve a **Developers** → **API keys**
4. Copia las claves:
   - **Publishable key**: `pk_test_...` (para pruebas) o `pk_live_...` (producción)
   - **Secret key**: `sk_test_...` (para pruebas) o `sk_live_...` (producción)

⚠️ **IMPORTANTE**: La Secret key NUNCA debe ir en el código frontend. Solo en el backend.

---

## Paso 2: Configurar Firebase Functions

### 2.1. Instalar dependencias

```bash
cd D:\AndroidStudioProjects\control-salario-backend
npm install stripe
```

### 2.2. Copiar el código

1. Abre `functions/src/index.ts`
2. Añade el contenido de `stripe-functions.ts` al final del archivo

### 2.3. Configurar variables de entorno

```bash
# Modo test (pruebas)
firebase functions:config:set stripe.secret_key="sk_test_TU_CLAVE_TEST" stripe.webhook_secret="whsec_TU_WEBHOOK_TEST"

# Modo producción
firebase functions:config:set stripe.secret_key="sk_live_TU_CLAVE_PROD" stripe.webhook_secret="whsec_TU_WEBHOOK_PROD"
```

### 2.4. Actualizar frontend con tu Publishable Key

En `E:\Appstracta\Web\mi-jornada\premium.html`, línea ~320:

```javascript
// Reemplaza con tu clave
const STRIPE_PUBLISHABLE_KEY = 'pk_test_TU_CLAVE_AQUI';
```

---

## Paso 3: Desplegar las Functions

```bash
cd D:\AndroidStudioProjects\control-salario-backend
firebase deploy --only functions
```

Las URLs de tus funciones serán:
- `createPaymentIntent`: `https://europe-west1-miappsalarios.cloudfunctions.net/createPaymentIntent`
- `getPremiumCode`: `https://europe-west1-miappsalarios.cloudfunctions.net/getPremiumCode`
- `stripeWebhook`: `https://europe-west1-miappsalarios.cloudfunctions.net/stripeWebhook`

---

## Paso 4: Configurar Webhook en Stripe

1. Ve a https://dashboard.stripe.com/webhooks
2. Crea un nuevo endpoint:
   - **URL**: `https://europe-west1-miappsalarios.cloudfunctions.net/stripeWebhook`
   - **Eventos**: Selecciona `checkout.session.completed`
3. Copia el **Signing secret** (empieza por `whsec_...`)
4. Añádelo a las config de Firebase:
   ```bash
   firebase functions:config:set stripe.webhook_secret="whsec_..."
   ```

---

## Paso 5: Probar el pago (modo test)

1. Usa las claves de test (`pk_test_...`, `sk_test_...`)
2. En Stripe Dashboard, ve a "Payments" y activa "Test mode toggle"
3. Usa tarjetas de prueba:
   - **Número**: `4242 4242 4242 4242`
   - **CVC**: Cualquier 3 dígitos
   - **Fecha**: Cualquier fecha futura
   - **Código postal**: Cualquier código postal

4. Haz un test de compra en `https://appstracta.app/mi-jornada/premium.html`

---

## Paso 6: Ir a producción

Cuando todo funcione en modo test:

1. Cambia las claves en el frontend (`premium.html`):
   ```javascript
   const STRIPE_PUBLISHABLE_KEY = 'pk_live_TU_CLAVE_PROD';
   ```

2. Actualiza las config de Firebase:
   ```bash
   firebase functions:config:set stripe.secret_key="sk_live_TU_CLAVE_PROD"
   ```

3. Re-despliega las functions:
   ```bash
   firebase deploy --only functions
   ```

4. Actualiza el webhook de Stripe con la URL de producción

---

## Flujo completo de datos

```
1. Usuario pulsa "Obtener Premium"
   ↓
2. Frontend llama a createPaymentIntent
   ↓
3. Backend genera código premium en Firestore (pendingPayment=true)
   ↓
4. Backend crea Checkout Session de Stripe
   ↓
5. Frontend redirige a Stripe Checkout
   ↓
6. Usuario completa pago en Stripe
   ↓
7. Stripe redirige a premium.html?success=true&session_id=...
   ↓
8. Frontend llama a getPremiumCode con el sessionId
   ↓
9. Backend verifica el pago en Stripe y actualiza el código (pendingPayment=false)
   ↓
10. Frontend muestra el código al usuario
   ↓
11. Usuario canjea el código en la app
```

---

## Precios y comisiones

| Concepto | Importe |
|----------|---------|
| Precio usuario | 2,99€ |
| Comisión Stripe (1.4% + 0,25€) | ~0,29€ |
| Ingreso neto | ~2,70€ |

---

## Solución de problemas

### Error: "No such file or module 'stripe'"
```bash
cd D:\AndroidStudioProjects\control-salario-backend
npm install stripe
```

### Error: "Webhook signature verification failed"
- Verifica que el webhook secret esté configurado correctamente
- Verifica que estás usando el modo correcto (test/live)

### El código no aparece tras el pago
- Verifica en Firebase Console que el código se creó en la colección `premiumCodes`
- Verifica los logs de Firebase Functions

### Error CORS
- Las funciones ya tienen headers CORS configurados
- Verifica que las URLs sean correctas

---

## Archivos modificados

1. `E:\Appstracta\Web\mi-jornada\premium.html` - Página de pago
2. `E:\Appstracta\Web\index.html` - Enlace premium añadido
3. `E:\Appstracta\Web\css\main.css` - Estilos del enlace premium
4. `functions/src/index.ts` - Backend Stripe (añadir el código)
