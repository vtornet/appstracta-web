# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Appstracta Web is a **static site** (no build process) showcasing personal projects including mobile apps, music videos (Appstracta Films), and TV formats (Appstracta Formats). The site is deployed via GitHub Pages with a custom domain (appstracta.app).

## Architecture

### Page Structure
- `index.html` - Main landing page (apps portfolio)
- `films.html` - Music video clips with embedded YouTube players
- `formats.html` - TV format "Una Sola Voz" documentation

### CSS Architecture (Unified - Marzo 2026)
CSS is organized in external files for better maintainability:

- `css/main.css` - **Common styles** shared across all pages (variables, reset, header, footer, buttons, sections)
- `css/films.css` - **Films-specific styles** (hero-films, video cards, music platforms)
- `css/formats.css` - **Formats-specific styles** (hero-formats, concept cards, specs)

Each HTML page includes:
```html
<link rel="stylesheet" href="css/main.css">
<link rel="stylesheet" href="css/[page].css">  <!-- films.css or formats.css -->
```

### Design System
CSS variables defined in `main.css`:
```css
:root {
    --primary: #2c3e50;     /* Dark blue-gray */
    --secondary: #3498db;   /* Blue (formats.html overrides to #9b59b6 purple) */
    --accent: #e74c3c;      /* Red */
    --light: #ecf0f1;
    --dark: #2c3e50;
    --text: #333;
    --gray: #95a5a6;
    --gradient: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    --shadow: 0 10px 30px rgba(0,0,0,0.1);
    --transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
```

### Responsive Breakpoints
- 1200px - Typography adjustments
- 992px - Footer layout, hide hero visual
- 768px - Mobile menu appears, grids collapse to 1 column
- 576px - Smaller typography

### Key Patterns

**Mobile Menu Toggle:**
```javascript
document.querySelector('.mobile-menu').addEventListener('click', function() {
    const nav = document.querySelector('nav ul');
    const isVisible = nav.style.display === 'flex';
    nav.style.display = isVisible ? 'none' : 'flex';
});
```

**Smooth Scroll:**
Internal anchor links use `targetElement.offsetTop - 80` to account for fixed header.

**Coming Soon Links:**
Links with `.coming-soon` class trigger an alert dialog - these are placeholder apps not yet released.

## File Organization

```
Web/
├── index.html          # Main landing page
├── films.html          # Music videos portfolio
├── formats.html        # TV format documentation
├── css/
│   ├── main.css        # Common styles (variables, reset, header, footer, buttons)
│   ├── films.css       # Films-specific styles (video cards, music platforms)
│   └── formats.css     # Formats-specific styles (concept cards, specs)
├── logos/              # App logo PNGs
└── images/             # Hero background, mockups
```

## Common Operations

### Testing locally
No build required. Open files directly in browser or use any static server:
```bash
# Python 3
python -m http.server 8000

# Node.js (npx)
npx serve
```

### Deploying
Push to `master` branch - GitHub Pages auto-deploys from root directory.

## Important Notes

- **No CSS nesting allowed** - Standard CSS only, no SCSS/SASS features
- **External CSS preferred** - Add common styles to `css/main.css`, page-specific styles to respective CSS files
- **No inline CSS** - Keep HTML clean; use existing CSS classes or add to CSS files
- **Consistent header** - All pages use the same fixed header structure (defined in main.css)
- **Contact email** - `contact@appstracta.app`

## Recent Changes (Marzo 2026)

### CSS Unification
- Migrated all inline CSS to external files (~1900 lines removed from HTML)
- Created `css/main.css` with shared styles across all pages
- Created `css/films.css` for films.html specific styles
- Created `css/formats.css` for formats.html specific styles
- Result: More maintainable codebase with better caching performance

### Content Updates
- Replaced "PiVerse" with "Agro Red" in apps and portfolio sections
- Added Agro Red logo (`logos/agro-red-logo.png`)
- Added video card IDs to films.html for footer anchor links
- Made formats.html accessible via hidden link (not visible in navigation)
