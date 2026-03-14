# Guía para subir el APK al servidor

## Ubicación de los archivos

- **Página web**: `E:\Appstracta\Web\mi-jornada\`
- **APK destino**: `E:\Appstracta\Web\apk\mi-jornada-1.5.3.apk`

---

## Paso 1: Generar el APK de release

```bash
# Desde la raíz del proyecto Android
cd D:\AndroidStudioProjects\ControldeSalario

# Limpiar build anterior
./gradlew clean

# Generar APK de release
./gradlew assembleRelease
```

El APK se generará en:
`D:\AndroidStudioProjects\ControldeSalario\app\build\outputs\apk\release\app-release.apk`

---

## Paso 2: Renombrar el APK

El APK generado se llama `app-release.apk`. Renómbralo a `mi-jornada-1.5.3.apk`:

```bash
# Windows (PowerShell)
Copy-Item "D:\AndroidStudioProjects\ControldeSalario\app\build\outputs\apk\release\app-release.apk" "E:\Appstracta\Web\apk\mi-jornada-1.5.3.apk"

# O manualmente:
# 1. Copia el archivo desde la carpeta build
# 2. Pégalo en E:\Appstracta\Web\apk\
# 3. Renómbralo a mi-jornada-1.5.3.apk
```

---

## Paso 3: Subir al servidor

### Opción A: Si usas FTP (FileZilla, etc.)

1. Abre tu cliente FTP
2. Conecta a tu servidor
3. Navega a `/public_html/apk/` o la ruta de tu web
4. Sube el archivo `mi-jornada-1.5.3.apk`

### Opción B: Si usas SSH/SFTP

```bash
# Desde Windows PowerShell o CMD
sftp usuario@tu-servidor.com

# Una vez conectado:
put E:\Appstracta\Web\apk\mi-jornada-1.5.3.apk /var/www/html/apk/mi-jornada-1.5.3.apk
```

### Opción C: Si usas Git para tu web

```bash
# Copia el APK a la carpeta del repo
cd E:\Appstracta
cp "D:\AndroidStudioProjects\ControldeSalario\app\build\outputs\apk\release\app-release.apk" Web/apk/mi-jornada-1.5.3.apk

# Commit y push
cd Web
git add apk/mi-jornada-1.5.3.apk
git commit -m "Add Mi Jornada APK v1.5.3"
git push
```

---

## Paso 4: Verificar que el APK es accesible

Abre el navegador y ve a:
```
https://appstracta.app/apk/mi-jornada-1.5.3.apk
```

Debería empezar a descargar el archivo automáticamente.

---

## Paso 5: Actualizar la página con cada nueva versión

Cuando generes una nueva versión:

1. **Incrementa la versión** en `build.gradle.kts`:
   ```kotlin
   versionCode = 38  // Incrementar
   versionName = "1.5.4"  // Nueva versión
   ```

2. **Genera el nuevo APK**

3. **Copia con el nuevo nombre**:
   ```
   mi-jornada-1.5.4.apk
   ```

4. **Actualiza los enlaces** en `index.html`:
   ```html
   <!-- Cambiar -->
   <a href="../apk/mi-jornada-1.5.4.apk" class="btn btn-download" download>
   ```

5. **Actualiza el documento de Firestore** `appConfig/latestVersion`:
   ```json
   {
     "versionCode": 38,
     "versionName": "1.5.4",
     "apkUrl": "https://appstracta.app/apk/mi-jornada-1.5.4.apk"
   }
   ```

---

## Estructura final de archivos

```
E:\Appstracta\Web\
├── apk\
│   └── mi-jornada-1.5.3.apk  ← El APK que subes al servidor
└── mi-jornada\
    ├── index.html
    └── style.css
```

En el servidor:
```
/public_html/
├── apk/
│   └── mi-jornada-1.5.3.apk  ← Accesible en https://appstracta.app/apk/mi-jornada-1.5.3.apk
└── mi-jornada/
    ├── index.html
    └── style.css
```

---

## Script automatizado (opcional)

Crea `E:\Appstracta\Web\deploy-apk.bat`:

```batch
@echo off
echo Generando APK...
cd D:\AndroidStudioProjects\ControldeSalario
call gradlew.bat assembleRelease

echo Copiando APK...
copy "app\build\outputs\apk\release\app-release.apk" "E:\Appstracta\Web\apk\mi-jornada-1.5.3.apk"

echo APK listo en: E:\Appstracta\Web\apk\mi-jornada-1.5.3.apk
echo Ahora súblelo al servidor manualmente.
pause
```

O para Linux/Mac:
```bash
#!/bin/bash
cd /d/AndroidStudioProjects/ControldeSalario
./gradlew assembleRelease
cp app/build/outputs/apk/release/app-release.apk /e/Appstracta/Web/apk/mi-jornada-1.5.3.apk
echo "APK listo en: /e/Appstracta/Web/apk/mi-jornada-1.5.3.apk"
```

---

## Notas importantes

1. **El APK debe ser firmado** con el keystore de release
2. **Mantén el mismo keystore** para todas las versiones (para que las actualizaciones funcionen)
3. **El tamaño del APK** es aproximadamente 8-10 MB
4. **Verifica la descarga** después de subir al servidor
