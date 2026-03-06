# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Appstracta Web is a **static site** (no build process) showcasing personal projects including mobile apps, music videos (Appstracta Films), and TV formats (Appstracta Formats). The site is deployed via GitHub Pages with a custom domain (appstracta.app).

## Architecture

### Page Structure
Each page is **self-contained** with embedded `<style>` blocks. CSS is not external (except `css/style.css` which contains only minimal overrides).

- `index.html` - Main landing page (apps portfolio)
- `films.html` - Music video clips with embedded YouTube players
- `formats.html` - TV format "Una Sola Voz" documentation

### Design System
CSS variables defined per-page (consistent across all files):
```css
:root {
    --primary: #2c3e50;     /* Dark blue-gray */
    --secondary: #3498db;   /* Blue (or #9b59b6 purple on formats.html) */
    --accent: #e74c3c;      /* Red */
    --light: #ecf0f1;
    --dark: #2c3e50;
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
│   └── style.css       # Minimal overrides (logo-img, app-mockup)
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
- **Inline CSS per page** - When adding styles, put them in the `<style>` block of the specific page, not in `css/style.css`
- **Consistent header** - All pages use the same fixed header structure
- **Contact email** - `contact@appstracta.app`
