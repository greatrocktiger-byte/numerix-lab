---
name: Cybernetic Telemetry
colors:
  surface: '#0e1321'
  surface-dim: '#0e1321'
  surface-bright: '#343948'
  surface-container-lowest: '#090e1c'
  surface-container-low: '#161b2a'
  surface-container: '#1a1f2e'
  surface-container-high: '#252a39'
  surface-container-highest: '#303444'
  on-surface: '#dee2f6'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dee2f6'
  inverse-on-surface: '#2b303f'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#adc6ff'
  on-secondary: '#002e6a'
  secondary-container: '#0566d9'
  on-secondary-container: '#e6ecff'
  tertiary: '#fff4f1'
  on-tertiary: '#5f1500'
  tertiary-container: '#ffcfc2'
  on-tertiary-container: '#b12f00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#ffdbd1'
  tertiary-fixed-dim: '#ffb5a0'
  on-tertiary-fixed: '#3b0900'
  on-tertiary-fixed-variant: '#862200'
  background: '#0e1321'
  on-background: '#dee2f6'
  surface-variant: '#303444'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  label-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 14px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-sm: 0.75rem
  gutter-lg: 1.5rem
  margin: 1.5rem
  margin-sm: 1rem
  margin-lg: 2.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

The design system is engineered for advanced scientific computing, high-performance simulation platforms, and dynamic graph/network analytics tools (such as thermal field dynamics and eigenvector centrality analyzers). It targets computational scientists, thermal engineers, data system architects, and technical researchers who require dense, high-frequency telemetry, accurate simulation feedback, and immediate visual hierarchy.

The aesthetic fuses **Glassmorphic Precision** with **Cybernetic Neon High-Contrast**. Built over an abyss of deep midnight navy and obsidian tones, the visual language utilizes luminous accents: cryogenic cyan, electric flux blue, thermal gradient embers (deep amber and thermodynamic orange-red), and kinetic emerald. Glassmorphic containers with ultra-fine frosted specular borders create spatial stratification without visual clutter, allowing real-time heat maps, numerical convergence gauges, and node-link graphs to dominate the canvas with electric luminosity. The atmosphere evokes mission control, real-time supercomputing terminals, and bleeding-edge scientific instrumentation.

## Colors

The color palette is calibrated specifically for luminous contrast against optical black and deep oceanic space, preserving eye stamina under long analytical sessions while making mission-critical thresholds instantaneous to spot.

### Palette Architecture
- **Primary (`#00F0FF` - Cryo Cyan):** Signifies primary interaction vectors, active telemetry hooks, focused states, and current runtime indicators.
- **Secondary (`#3B82F6` - Electric Blue):** Drives primary CTA fills, structural selection frames, progress rails, and baseline computational pathways.
- **Tertiary & Thermal Accents:**
  - **Thermodynamic Hotspot (`#FF5722`):** Hotspots, maximum heat limits, primary critical warnings, high-voltage indicators.
  - **Thermal Flux Amber (`#FF9800`):** Mid-high thermal dispersion, warning thresholds, intermediate iterations.
  - **Kinetic Green (`#10B981`):** Mathematical convergence, verified states, optimal efficiency, low thermal delta.
- **Neutrals & Dark Surfaces:**
  - **Deep Base Canvas (`#0A0F1D`):** The foundational substrate of all viewports.
  - **Elevated Canvas (`#0D1527`):** Base structural pane, header regions, and canvas backdrops.
  - **Surface Container Base (`#131D35` at 60-80% opacity):** Primary glass panels and interactive cards.
  - **High-Contrast Text (`#F8FAFC`):** Primary data readouts, scalar parameters, and titles.
  - **Muted Data Text (`#94A3B8`):** Dimension units, mathematical notation, inactive states, secondary keys.
  - **Specular Stroke (`rgba(255, 255, 255, 0.08)`): Delimiting vector boundaries across dark panels.

## Typography

The typography architecture reinforces computational rigor and telemetry legibility:

- **Display & Section Headers (`Space Grotesk`):** Technical geometry, distinctive terminal angles, and authoritative presence for module naming, simulation headlines, and computational status banners.
- **Interface & Operational Copy (`Inter`):** Systematic neutral grotesque rendering ensures friction-free scanning across nested panels, configuration rows, and narrative analytical reports.
- **Telemetry, Numerical Matrix & Code (`JetBrains Mono`):** Fixed-width tabular figures for dynamic metrics (iterations, runtime errors, temperatures, vector coordinates, and matrix outputs), preventing layout shifts during continuous solver recalculations.

## Layout & Spacing

The layout model is anchored around a responsive, high-density 12-column grid configured for high-information-density telemetry and visualization workflows.

### Grid & Density Hierarchy
- **Canvas Margins:** Dynamic outer boundary transitioning from `1rem` on mobile (`<768px`) to `1.5rem` on tablet/laptop (`768px-1279px`), and expanding to `2.5rem` on ultra-wide scientific monitors (`≥1280px`).
- **Layout Modularity:**
  - **Tool/Configuration Rails:** Occupy a rigid 3 or 4 columns (min 320px) on desktop to host multi-parameter thermal or node configuration controls.
  - **Simulation & Viewport Canvases:** Span 8 to 9 columns on desktop to afford maximum surface area for GPU heat-maps, nodal graphs, and contour fields.
  - **Telemetry Docking:** Bottom drawer or auxiliary sidebar uses modular 4-column cards for secondary statistical readouts (Min/Max Temp, Hotspots, Iteration counters).
- **Responsive Stacking:**
  - Mobile drops the dual-pane arrangement into a strict vertical sequence: Visualizer Viewport pinned to top, followed by collapsible parameter accordions and execution action bars docked persistently at the viewport bottom.

## Elevation & Depth

Visual hierarchy does not rely on traditional drop shadows, but rather on **specular layering, dark translucency, and photonic glow radiance**.

### Tonal Stratification
1. **Layer 0 (Canvas Base):** Solid deep midnight backdrop (`#0A0F1D`) with subtle radial energetic gradients positioned beneath major visualizers.
2. **Layer 1 (Modular Work Surface):** Translucent glass panels (`rgba(13, 21, 39, 0.7)`) backed by `backdrop-filter: blur(16px)` and edged with a delicate 1px boundary stroke `rgba(255, 255, 255, 0.08)`.
3. **Layer 2 (Interactive Floating Cards & Inspector Panes):** Higher opacity (`rgba(19, 29, 53, 0.85)`), blur of `24px`, with top-edge specular illumination (`rgba(255, 255, 255, 0.15)`) simulating edge-lit glass.
4. **Layer 3 (Overlays, Tooltips, & Node Modals):** Dense glass (`#162344`), bounded by primary cyan or blue glow lines (`box-shadow: 0 0 20px rgba(0, 240, 255, 0.15)`).

### Photonic Emissive Glows
- **Critical Hotspots & Dynamic Focus:** When an element represents an active hotspot or focused node, it emits an ambient, non-directional atmospheric neon haze (`box-shadow: 0 0 16px rgba(255, 87, 34, 0.35)` for thermal thresholds; `0 0 16px rgba(0, 240, 255, 0.35)` for cybernetic/cyan states).

## Shapes

The design system maintains a balanced, contemporary technical curvature (`level 2` - Rounded), avoiding both harsh brutalist sharpness and excessively soft consumer roundness.

- **Component Containers & Viewports:** Styled with `rounded-lg` (16px / 1rem) to frame scientific grids, graphs, and simulation consoles with aerodynamic precision.
- **Controls, Input Sliders & Parameter Badges:** Formed with base `rounded` (8px / 0.5rem) for consistent, ergonomic targets.
- **Pill Badges & Telemetry Status Tags:** Selectively utilize full circular rounding (`rounded-full`) to contrast against rectangular spatial modules and immediately denote discrete system states (e.g., active convergence flags, hardware node badges).

## Components

### Buttons & Action Controls
- **Primary CTA:** Solid Electric Blue (`#3B82F6`) with white high-contrast text, transitioning on hover to Cryo Cyan radiance (`box-shadow: 0 0 16px rgba(0, 240, 255, 0.4)`).
- **Secondary / Ghost Scientific Buttons:** Transparent fill surrounded by `rgba(255, 255, 255, 0.1)` borders, displaying `Inter` medium weights and cyan text hover states.
- **Simulate / Execution Button:** Full-width or primary prominence, featuring continuous animated border gradient or cyan glow to denote executable computational states.

### Data Sliders & Parameter Steppers
- **Track:** 4px high track in muted navy (`rgba(255, 255, 255, 0.12)`). Active fill utilizes cyan-to-electric-blue linear gradient (`#00F0FF` to `#3B82F6`).
- **Thumb:** 18px circle with a cyan glow halo, containing a central white core. Displays current floating-point value overhead in `JetBrains Mono` label format during interaction.

### Telemetry Badges & Chips
- **Heat & Status Tags:** Pill-shaped elements with low-opacity colored backgrounds (e.g., `rgba(255, 87, 34, 0.15)` for thermal alert, `rgba(16, 185, 129, 0.15)` for solved iterations).
- **Iconography Integration:** Leading micro-dots or indicator pips that pulse during live calculation states.

### Heat Map & Graph Matrix Containers
- **Border Treatment:** High-precision bounding borders (`1px solid rgba(255, 255, 255, 0.08)`), equipped with coordinate axis markings rendered in `JetBrains Mono` at `label-sm`.
- **Thermal Spectrum Legend:** Vertical or horizontal color bar spanning 25°C (`#00F0FF`) through 50°C (`#10B981`), 75°C (`#FF9800`), to 100°C+ (`#FF5722`), accompanied by aligned temperature intervals.

### Form Inputs & Radio / Segmented Groups
- **Text & Numeric Inputs:** Recessed dark navy fields (`#0A0F1D`) with subtle 1px border. Values aligned right with monospace precision and affixed units (e.g., `°C`, `W/m²`, `iter`).
- **Segmented Mode Switchers:** Contained pill docks where active selection slides over an electric blue glow plate.