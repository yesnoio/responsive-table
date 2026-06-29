# Changelog

## [1.1.0] – 2026-06-29

### Fixed

- **CSS specificity bug — labels hidden in mobile view.**
  `td .label { display: none }` (specificity 0,2,2) was silently overriding
  `td span { display: block }` (specificity 0,1,3) inside the media query, so
  `.label` spans never appeared on narrow screens. Fixed by adding an explicit
  `display: block` to the `.label` rule inside the media query across all
  stacked-label variants (`demo.html`, `success.html` style-a, `basic.html`,
  `complex.html` table.stacked, `blank.html`).

### Changed

- **Mobile row grouping.** Each `tbody tr` is now rendered as a bordered card
  (`display: block`, `border`, `border-radius: 6px`, `margin-bottom: 1rem`) so
  rows are clearly separated when cells stack vertically.
- **Label and data padding.** Mobile cell headings (`.label`) use tighter
  vertical padding (`0.25rem 0.875rem`); cell values (`.data`) use roomier
  padding (`0.6rem 0.875rem`). Padding is now owned by the spans rather than
  the `td`, so label headings sit flush against the card edges.
- **Code examples updated** in `index.html` and `success.html` to reflect all
  of the above CSS changes.
- **Downloadable examples rebuilt** (`blank.html`, `basic.html`, `complex.html`,
  and the ZIP) with all CSS fixes applied.

### Added

- **`.github/workflows/deploy.yml`** — GitHub Actions workflow that deploys the
  `docs/` directory to GitHub Pages on every push to `master`.
- **`docs/responsive-table.js`** — optional client-side helper. Include it once
  and it reads each `table.responsive`'s `<thead>` to inject `.label`/`.data`
  spans at load time, so the responsive CSS works without hand-authoring the
  span markup. Idempotent.
- **`docs/transform-tables.py`** — build-time Python script (requires
  `beautifulsoup4`). Transforms every `<table>` in a given HTML file: adds
  `class="responsive"` where absent and injects `.label`/`.data` spans into
  each `<td>`. Designed for static-site pipelines and AI-assisted pre-commit
  workflows. Idempotent.
