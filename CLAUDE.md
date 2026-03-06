# CLAUDE.md

Este archivo proporciona guía a Claude Code (claude.ai/code) para trabajar con el código en este repositorio.

## Resumen del Proyecto

Appstracta Web es un **sitio estático** (sin proceso de build) que presenta proyectos personales incluyendo aplicaciones móviles, vídeos musicales (Appstracta Films) y formatos de televisión (Appstracta Formats). El sitio se despliega mediante GitHub Pages con dominio personalizado (appstracta.app).

## Arquitectura

### Estructura de Páginas
- `index.html` - Página principal (portfolio de aplicaciones)
- `films.html` - Videoclips musicales con reproductores YouTube integrados
- `formats.html` - Documentación del formato de TV "Una Sola Voz"

### Arquitectura CSS (Unificada - Marzo 2026)
El CSS está organizado en archivos externos para mejor mantenimiento:

- `css/main.css` - **Estilos comunes** compartidos entre todas las páginas (variables, reset, header, footer, botones, secciones)
- `css/films.css` - **Estilos específicos de films** (hero-films, tarjetas de vídeo, plataformas musicales)
- `css/formats.css` - **Estilos específicos de formats** (hero-formats, tarjetas de concepto, especificaciones)

Cada página HTML incluye:
```html
<link rel="stylesheet" href="css/main.css">
<link rel="stylesheet" href="css/[page].css">  <!-- films.css o formats.css -->
```

### Sistema de Diseño
Variables CSS definidas en `main.css`:
```css
:root {
    --primary: #2c3e50;     /* Azul grisáceo oscuro */
    --secondary: #3498db;   /* Azul (formats.html sobrescribe a #9b59b6 púrpura) */
    --accent: #e74c3c;      /* Rojo */
    --light: #ecf0f1;
    --dark: #2c3e50;
    --text: #333;
    --gray: #95a5a6;
    --gradient: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    --shadow: 0 10px 30px rgba(0,0,0,0.1);
    --transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
```

### Breakpoints Responsivos
- 1200px - Ajustes de tipografía
- 992px - Layout del footer, ocultar visual hero
- 768px - Menú móvil aparece, grids colapsan a 1 columna
- 576px - Tipografía más pequeña

### Patrones Clave

**Toggle de Menú Móvil:**
```javascript
document.querySelector('.mobile-menu').addEventListener('click', function() {
    const nav = document.querySelector('nav ul');
    const isVisible = nav.style.display === 'flex';
    nav.style.display = isVisible ? 'none' : 'flex';
});
```

**Smooth Scroll:**
Los enlaces ancla internos usan `targetElement.offsetTop - 80` para compensar el header fijo.

**Enlaces "Próximamente":**
Los enlaces con clase `.coming-soon` muestran un diálogo de alerta - son apps placeholder aún no lanzadas.

## Organización de Archivos

```
Web/
├── index.html          # Página principal
├── films.html          # Portfolio de videoclips
├── formats.html        # Documentación de formato TV
├── CLAUDE.md           # Este archivo
├── css/
│   ├── main.css        # Estilos comunes (variables, reset, header, footer, botones)
│   ├── films.css       # Estilos específicos de films (tarjetas de vídeo, plataformas)
│   └── formats.css     # Estilos específicos de formats (conceptos, especificaciones)
├── logos/              # Logotipos PNG de las apps
└── images/             # Fondo hero, mockups
```

## Operaciones Comunes

### Prueba local
No requiere build. Abrir archivos directamente en el navegador o usar cualquier servidor estático:
```bash
# Python 3
python -m http.server 8000

# Node.js (npx)
npx serve
```

### Despliegue
Hacer push a la rama `master` - GitHub Pages despliega automáticamente desde el directorio raíz.

## Notas Importantes

- **Sin anidamiento CSS** - CSS estándar solamente, sin características SCSS/SASS
- **CSS externo preferido** - Añadir estilos comunes a `css/main.css`, estilos específicos a sus archivos CSS respectivos
- **Sin CSS inline** - Mantener HTML limpio; usar clases CSS existentes o añadir a archivos CSS
- **Header consistente** - Todas las páginas usan la misma estructura de header fijo (definida en main.css)
- **Email de contacto** - `contact@appstracta.app`

## Cambios Recientes (Marzo 2026)

### Unificación de CSS ✅
- Migrado todo el CSS inline a archivos externos (~1900 líneas eliminadas del HTML)
- Creado `css/main.css` con estilos compartidos
- Creado `css/films.css` para estilos específicos de films.html
- Creado `css/formats.css` para estilos específicos de formats.html
- Resultado: Código más mantenible con mejor rendimiento de caché

### Actualizaciones de Contenido
- Reemplazado "PiVerse" por "Agro Red" en secciones de apps y portfolio
- Añadido logotipo de Agro Red (`logos/agro-red-logo.png`)
- Añadidos IDs a tarjetas de vídeo en films.html para anclas del footer
- formats.html accesible mediante enlace oculto (no visible en navegación)

## Mejoras Pendientes

Lista de mejoras sugeridas para el sitio web. Marcar con `[X]` cuando completado.

### ✅ Completadas
- [X] **#1**: Unificar estilos CSS en archivos externos (main.css, films.css, formats.css)
- [X] **#4**: Hacer funcional el carrusel del portfolio
  - Navegación con botones prev/next funcionando
  - Transiciones suaves con scroll snap
  - Indicadores visuales (dots) de posición
  - Responsive: 1 card móvil, 2 tablet, 3 desktop

### ⏭️ Saltados (decisión del usuario)
- ~~#2~~: Destacar Agro Red como proyecto principal (mantener aspecto de proyecto personal)
- ~~#3~~: Añadir estadísticas concretas (mantener aspecto de proyecto personal, no empresa)

### 🔍 SEO
- [X] **#5**: Mejorar SEO
  - Meta tags descriptivos en todas las páginas
  - Open Graph para Facebook/LinkedIn
  - Twitter Cards
  - Canonical URLs
  - Sitemap.xml creado
  - Robots.txt creado

### 🎨 Diseño
- [X] **#6**: Añadir favicon (favicon.ico añadido con links en todas las páginas)
- [ ] **#7**: Optimizar imágenes para web (WebP, compresión)
- [ ] **#8**: Añadir animaciones sutiles al hacer scroll

## Política de Enlaces Externos

**IMPORTANTE:** Todos los proyectos están en fase beta/desarrollo. No añadir enlaces externos reales hasta que los productos estén listos para el público.

- Enlaces a apps: usar `#` o `.coming-soon` para productos no lanzados
- Agro Red: https://agroredjob.com (único enlace real permitido por ahora)
- Enlaces sociales: verificados y funcionales
