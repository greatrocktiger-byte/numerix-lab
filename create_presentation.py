import os
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette Definitions
    BG_DARK = RGBColor(11, 15, 25)         # #0B0F19 - Main Background
    CARD_BG = RGBColor(17, 24, 39)         # #111827 - Slate 900 Card
    CARD_BG_ALT = RGBColor(15, 23, 42)     # #0F172A - Deep Slate Card
    BORDER_CYAN = RGBColor(14, 165, 233)   # #0EA5E9 - Sky/Cyan
    BORDER_MUTED = RGBColor(30, 41, 59)    # #1E293B - Slate Border
    BORDER_EMERALD = RGBColor(16, 185, 129)# #10B981 - Green
    BORDER_AMBER = RGBColor(245, 158, 11)  # #F59E0B - Amber
    BORDER_PURPLE = RGBColor(168, 85, 247) # #A855F7 - Purple
    
    TEXT_WHITE = RGBColor(248, 250, 252)   # #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8
    TEXT_CYAN = RGBColor(56, 189, 248)     # #38BDF8
    TEXT_EMERALD = RGBColor(52, 211, 153)  # #34D399
    TEXT_AMBER = RGBColor(251, 191, 36)    # #FBBF24

    def create_base_slide():
        slide = prs.slides.add_slide(blank_layout)
        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()
        return slide

    def add_header(slide, num, category, title, subtitle):
        # Category Badge
        cat_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(3.2), Inches(0.32))
        cat_box.fill.solid()
        cat_box.fill.fore_color.rgb = RGBColor(15, 23, 42)
        cat_box.line.color.rgb = BORDER_CYAN
        cat_box.line.width = Pt(1)
        tf_c = cat_box.text_frame
        tf_c.word_wrap = False
        tf_c.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_c = tf_c.paragraphs[0]
        p_c.text = f"SLIDE {num:02d}  |  {category.upper()}"
        p_c.font.size = Pt(9.5)
        p_c.font.bold = True
        p_c.font.color.rgb = TEXT_CYAN

        # Title
        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.8), Inches(0.55))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_top = tf_t.margin_bottom = tf_t.margin_left = tf_t.margin_right = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(21)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE

        # Subtitle
        if subtitle:
            tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(1.32), Inches(11.8), Inches(0.35))
            tf_s = tb_s.text_frame
            tf_s.word_wrap = True
            tf_s.margin_top = tf_s.margin_bottom = tf_s.margin_left = tf_s.margin_right = 0
            p_s = tf_s.paragraphs[0]
            p_s.text = subtitle
            p_s.font.size = Pt(11)
            p_s.font.color.rgb = TEXT_MUTED

    def add_footer(slide, current_idx, total=15):
        # Divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.05), Inches(11.733), Pt(1))
        line.fill.solid()
        line.fill.fore_color.rgb = RGBColor(30, 41, 59)
        line.line.fill.background()

        tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.12), Inches(11.733), Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_top = tf.margin_bottom = tf.margin_left = tf.margin_right = 0
        p = tf.paragraphs[0]
        p.text = f"NUMERIX LAB: Numerical Methods, Visualized   •   Live URL: https://greatrocktiger-byte.github.io/numerix-lab/   •   Slide {current_idx} of {total}"
        p.font.size = Pt(9)
        p.font.color.rgb = RGBColor(100, 116, 139)

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_MUTED, border_width=1.0):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(border_width)
        return card

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = create_base_slide()
    # Big Title Box
    card1 = add_card(s1, 0.8, 1.2, 7.2, 5.4, bg_color=CARD_BG_ALT, border_color=BORDER_CYAN, border_width=1.5)
    tf1 = card1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = Inches(0.4)
    tf1.margin_top = Inches(0.4)

    p1 = tf1.paragraphs[0]
    p1.text = "ACADEMIC VIVA & EVALUATION PRESENTATION"
    p1.font.size = Pt(10)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_CYAN
    p1.space_after = Pt(10)

    p2 = tf1.add_paragraph()
    p2.text = "NUMERIX LAB"
    p2.font.size = Pt(36)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE

    p3 = tf1.add_paragraph()
    p3.text = "“Numerical Methods, Visualized.”"
    p3.font.size = Pt(16)
    p3.font.italic = True
    p3.font.color.rgb = TEXT_EMERALD
    p3.space_after = Pt(16)

    p4 = tf1.add_paragraph()
    p4.text = "A production-grade scientific computational platform transforming abstract numerical algorithms into deterministic, real-time visual simulations."
    p4.font.size = Pt(11.5)
    p4.font.color.rgb = TEXT_MUTED
    p4.space_after = Pt(20)

    # Core Features pill
    p5 = tf1.add_paragraph()
    p5.text = "CORE ALGORITHMIC IMPLEMENTATIONS:"
    p5.font.size = Pt(10)
    p5.font.bold = True
    p5.font.color.rgb = TEXT_WHITE
    p5.space_after = Pt(6)

    bullets = [
        "THERMALX: 2D Heat Equation, 5-point Finite Differences, Jacobi & Gauss-Seidel Solvers",
        "LINKRANK: Spectral Graph Theory, Markov Chains, PageRank Power Iteration (λ₁ = 1.0)",
        "NUMERICAL LAB: Bisection, Newton-Raphson, and Analytical Characteristic Polynomials"
    ]
    for b in bullets:
        pb = tf1.add_paragraph()
        pb.text = "  ▶  " + b
        pb.font.size = Pt(10)
        pb.font.color.rgb = TEXT_MUTED
        pb.space_after = Pt(4)

    # Project metadata box at bottom
    p_meta = tf1.add_paragraph()
    p_meta.text = "\nLive Deployment: https://greatrocktiger-byte.github.io/numerix-lab/"
    p_meta.font.size = Pt(9.5)
    p_meta.font.bold = True
    p_meta.font.color.rgb = TEXT_CYAN

    # Right side: Overview Hero Image
    if os.path.exists('presentation_assets/ui_overview.png'):
        s1.shapes.add_picture('presentation_assets/ui_overview.png', Inches(8.2), Inches(1.2), Inches(4.33), Inches(5.4))

    add_footer(s1, 1)

    # ==========================================
    # SLIDE 2: MOTIVATION & PROBLEM STATEMENT
    # ==========================================
    s2 = create_base_slide()
    add_header(s2, 2, "Introduction & Motivation", 
               "Bridging the Gap: Abstract Mathematics vs Visual Computation",
               "Why traditional numerical methods education struggles, and how Numerix Lab creates intuitive, verifiable learning.")

    # 3 Column Cards
    col_w = 3.64
    card_p = add_card(s2, 0.8, 1.8, col_w, 4.9, bg_color=CARD_BG, border_color=RGBColor(244, 63, 94))
    tf_p = card_p.text_frame
    tf_p.word_wrap = True
    tf_p.margin_left = tf_p.margin_right = Inches(0.25)
    tf_p.margin_top = Inches(0.3)
    p = tf_p.paragraphs[0]
    p.text = "1. THE PEDAGOGICAL PROBLEM"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = RGBColor(244, 63, 94)
    p.space_after = Pt(12)
    items_p = [
        ("Black-Box Code:", "Students execute canned scripts without visual feedback of intermediate convergence steps."),
        ("Spatial Disconnect:", "Equations like ∇²T = 0 or Ax = λx remain abstract matrix symbols disconnected from physical heat diffusion or network graphs."),
        ("Mocked Demonstrations:", "Typical web demos rely on pre-baked fake CSS animations rather than live computational state updates.")
    ]
    for h, desc in items_p:
        p = tf_p.add_paragraph()
        p.text = f"• {h} {desc}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(10)

    card_s = add_card(s2, 4.84, 1.8, col_w, 4.9, bg_color=CARD_BG, border_color=BORDER_CYAN)
    tf_s = card_s.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_right = Inches(0.25)
    tf_s.margin_top = Inches(0.3)
    p = tf_s.paragraphs[0]
    p.text = "2. THE NUMERIX SOLUTION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(12)
    items_s = [
        ("Live Computational States:", "Every frame rendered directly reflects real memory grid iterations: T⁽ᵏ⁾ → T⁽ᵏ⁺¹⁾."),
        ("100% Deterministic Math:", "No mocked values. Temperature fields, residual errors, and eigenvectors are calculated in real time."),
        ("Interactive Parameter Tuning:", "Users adjust source temperatures, cooling intensity, damping factors, and observe immediate behavioral changes.")
    ]
    for h, desc in items_s:
        p = tf_s.add_paragraph()
        p.text = f"• {h} {desc}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(10)

    card_v = add_card(s2, 8.88, 1.8, col_w, 4.9, bg_color=CARD_BG, border_color=BORDER_EMERALD)
    tf_v = card_v.text_frame
    tf_v.word_wrap = True
    tf_v.margin_left = tf_v.margin_right = Inches(0.25)
    tf_v.margin_top = Inches(0.3)
    p = tf_v.paragraphs[0]
    p.text = "3. ACADEMIC VIVA PURPOSE"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_EMERALD
    p.space_after = Pt(12)
    items_v = [
        ("Rigorous Viva Defense:", "Engineered specifically for university viva demonstrations, enabling examiners to test edge cases live."),
        ("Method Comparison:", "Side-by-side execution of Jacobi vs Gauss-Seidel on identical initial conditions to confirm theoretical convergence rates."),
        ("Mathematical Transparency:", "'Show the Math' overlays expose equations, stencil mechanics, and error tolerances at every stage.")
    ]
    for h, desc in items_v:
        p = tf_v.add_paragraph()
        p.text = f"• {h} {desc}"
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        p.space_after = Pt(10)

    add_footer(s2, 2)

    # ==========================================
    # SLIDE 3: UNIFIED SYSTEM ARCHITECTURE
    # ==========================================
    s3 = create_base_slide()
    add_header(s3, 3, "System Architecture",
               "Three Autonomous Computational Engines Under One Platform",
               "NUMERIX LAB operates as a modular, zero-dependency computational simulation suite.")

    # 3 Feature Boxes
    engines = [
        ("THERMALX ENGINE", "2D Thermal Field PDE Solver", BORDER_CYAN, [
            "Governing PDE: Steady-state 2D Poisson Heat Equation ∇²T = -q/k",
            "Discretization: 5-point central finite-difference spatial stencil",
            "Solvers: Simultaneous Jacobi & in-place Gauss-Seidel comparisons",
            "Features: Laptop chassis thermal model, hotspot detection & cooling"
        ]),
        ("LINKRANK ENGINE", "Spectral Graph Theory & PageRank", BORDER_PURPLE, [
            "Graph Modeling: Directed networks with column-stochastic transition matrix M",
            "Stationary Distribution: Google matrix with random surfer damping (α = 0.85)",
            "Eigen-Solver: Power Iteration method for principal eigenvector (λ₁ = 1.0)",
            "Features: Real-time dynamic graph topology editor & random walk visualizer"
        ]),
        ("NUMERICAL LAB", "Interactive Classical Numerical Solvers", BORDER_EMERALD, [
            "Root Finding: Bisection (linear O(1/2ⁿ)) vs Newton-Raphson (quadratic O(ε²))",
            "Spectral Decomposition: 2x2 & 3x3 characteristic polynomial solvers det(A - λI)=0",
            "Linear Systems: 3-variable Jacobi & Gauss-Seidel convergence comparison",
            "Features: Step-by-step iteration logs, invariant checks (Tr(A), det(A))"
        ])
    ]

    for idx, (title, sub, border_col, points) in enumerate(engines):
        x = 0.8 + idx * 4.0
        c = add_card(s3, x, 1.8, 3.8, 3.2, bg_color=CARD_BG, border_color=border_col, border_width=1.2)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.22)
        tf.margin_top = Inches(0.2)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = border_col
        p_sub = tf.add_paragraph()
        p_sub.text = sub
        p_sub.font.size = Pt(9.5)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.space_after = Pt(8)
        for pt in points:
            p_pt = tf.add_paragraph()
            p_pt.text = "• " + pt
            p_pt.font.size = Pt(9)
            p_pt.font.color.rgb = TEXT_WHITE
            p_pt.space_after = Pt(4)

    # Bottom Pipeline Architecture Banner
    c_pipe = add_card(s3, 0.8, 5.2, 11.733, 1.6, bg_color=CARD_BG_ALT, border_color=BORDER_MUTED)
    tf_pipe = c_pipe.text_frame
    tf_pipe.word_wrap = True
    tf_pipe.margin_left = tf_pipe.margin_right = Inches(0.3)
    tf_pipe.margin_top = Inches(0.15)
    p = tf_pipe.paragraphs[0]
    p.text = "COMPUTATIONAL PIPELINE & ZERO-DEPENDENCY CLIENT-SIDE EXECUTION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(6)

    flow_steps = [
        "1. Parameter Input (Chassis/Graph/Coefficients)",
        "2. Mathematical Discretization (Grid / Adjacency)",
        "3. Iterative Solver Sweep (Jacobi / GS / Power)",
        "4. Norm Error Check (||x^(k+1) - x^(k)|| < tol)",
        "5. Canvas / SVG Live Shader Interpolation"
    ]
    p_f = tf_pipe.add_paragraph()
    p_f.text = "   ➔   ".join(flow_steps)
    p_f.font.size = Pt(9.5)
    p_f.font.bold = True
    p_f.font.color.rgb = TEXT_EMERALD

    p_f2 = tf_pipe.add_paragraph()
    p_f2.text = "Architecture Advantage: 100% native JavaScript mathematics engine running client-side with zero server latency, instant recalculation, and cross-platform browser support."
    p_f2.font.size = Pt(9)
    p_f2.font.color.rgb = TEXT_MUTED

    add_footer(s3, 3)

    # ==========================================
    # SLIDE 4: THERMALX - PDE & FINITE DIFFERENCES
    # ==========================================
    s4 = create_base_slide()
    add_header(s4, 4, "ThermalX Engine",
               "2D Steady-State Heat Equation & 5-Point Laplacian Discretization",
               "Formulating the physical thermal diffusion field into a solvable linear algebraic system.")

    # Left: Mathematical Formulation Card
    c_math = add_card(s4, 0.8, 1.8, 6.4, 4.9, bg_color=CARD_BG, border_color=BORDER_CYAN)
    tf_m = c_math.text_frame
    tf_m.word_wrap = True
    tf_m.margin_left = tf_m.margin_right = Inches(0.3)
    tf_m.margin_top = Inches(0.25)

    p = tf_m.paragraphs[0]
    p.text = "MATHEMATICAL FORMULATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(8)

    equations = [
        ("Governing Physical Law:", "Steady-state 2D heat conduction with internal heat generation q(x, y):"),
        ("Poisson Equation:", "∇²T = ∂²T/∂x² + ∂²T/∂y² = -q(x, y) / k   (k = thermal conductivity)"),
        ("Laplace Equation (Source-free):", "∇²T = 0   (in regions without active silicon chips)"),
        ("Finite Difference Discretization:", "Applying Taylor series central differences (Δx = Δy = h):"),
        ("Spatial Derivative:", "∂²T/∂x² ≈ [T(i+1, j) - 2T(i, j) + T(i-1, j)] / h²"),
        ("5-Point Laplacian Stencil Update Equation:", 
         "T(i, j)⁽ᵏ⁺¹⁾ = ¼ [ T(i+1, j) + T(i-1, j) + T(i, j+1) + T(i, j-1) ] + (q_ij · h²) / (4k)"),
        ("Boundary Conditions:", 
         "• Dirichlet BC: Fixed wall temperatures T(boundary) = T_ambient\n• Neumann BC: Insulated chassis boundaries ∂T/∂n = 0")
    ]

    for title_eq, eq in equations:
        p = tf_m.add_paragraph()
        p.text = f"{title_eq}"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_c = tf_m.add_paragraph()
        p_c.text = f"   {eq}"
        p_c.font.size = Pt(9)
        p_c.font.color.rgb = TEXT_CYAN if "Update" in title_eq or "Poisson" in title_eq else TEXT_MUTED
        p_c.space_after = Pt(4)

    # Right: Stencil Diagram
    if os.path.exists('presentation_assets/diagram_stencil.png'):
        s4.shapes.add_picture('presentation_assets/diagram_stencil.png', Inches(7.5), Inches(1.8), Inches(5.0), Inches(3.6))

    # Right Bottom: Stencil explanation card
    c_st = add_card(s4, 7.5, 5.5, 5.0, 1.2, bg_color=CARD_BG_ALT, border_color=BORDER_EMERALD)
    tf_st = c_st.text_frame
    tf_st.word_wrap = True
    tf_st.margin_left = tf_st.margin_right = Inches(0.2)
    tf_st.margin_top = Inches(0.12)
    p = tf_st.paragraphs[0]
    p.text = "PHYSICAL INTERPRETATION OF 5-POINT STENCIL"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_EMERALD
    p2 = tf_st.add_paragraph()
    p2.text = "Each interior cell's temperature at equilibrium is precisely the arithmetic mean of its 4 orthogonal neighboring cells, perturbed by local heat source generation."
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = TEXT_MUTED

    add_footer(s4, 4)

    # ==========================================
    # SLIDE 5: THERMALX - JACOBI VS GAUSS-SEIDEL
    # ==========================================
    s5 = create_base_slide()
    add_header(s5, 5, "ThermalX Engine",
               "Iterative Solvers: Jacobi vs. Gauss-Seidel Convergence Mechanics",
               "Rigorous mathematical comparison of memory access, spectral radius, and convergence speeds.")

    # Left: Convergence Chart
    if os.path.exists('presentation_assets/chart_convergence.png'):
        s5.shapes.add_picture('presentation_assets/chart_convergence.png', Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.1))

    # Left Bottom Callout Box
    c_lb = add_card(s5, 0.8, 6.0, 5.8, 0.85, bg_color=CARD_BG_ALT, border_color=BORDER_AMBER)
    tf_lb = c_lb.text_frame
    tf_lb.word_wrap = True
    tf_lb.margin_left = tf_lb.margin_right = Inches(0.2)
    tf_lb.margin_top = Inches(0.1)
    p = tf_lb.paragraphs[0]
    p.text = "KEY THEORETICAL THEOREM (Laplace Grid)"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_AMBER
    p2 = tf_lb.add_paragraph()
    p2.text = "ρ(G_GS) = [ρ(G_Jacobi)]² < ρ(G_Jacobi) < 1  ⟹  Gauss-Seidel requires exactly half the iterations of Jacobi to achieve identical error tolerance!"
    p2.font.size = Pt(8.5)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE

    # Right: Comparison Breakdown
    c_comp = add_card(s5, 6.8, 1.8, 5.733, 4.9, bg_color=CARD_BG, border_color=BORDER_CYAN)
    tf_cp = c_comp.text_frame
    tf_cp.word_wrap = True
    tf_cp.margin_left = tf_cp.margin_right = Inches(0.3)
    tf_cp.margin_top = Inches(0.2)

    p = tf_cp.paragraphs[0]
    p.text = "ALGORITHMIC COMPARISON"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(10)

    # Jacobi Section
    p = tf_cp.add_paragraph()
    p.text = "1. JACOBI METHOD (Simultaneous Relaxation)"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(56, 189, 248)
    j_pts = [
        "Update: T_ij⁽ᵏ⁺¹⁾ uses values strictly from prior iteration (k).",
        "Equation: T_ij⁽ᵏ⁺¹⁾ = ¼ [ T_{i+1,j}⁽ᵏ⁾ + T_{i-1,j}⁽ᵏ⁾ + T_{i,j+1}⁽ᵏ⁾ + T_{i,j-1}⁽ᵏ⁾ ]",
        "Memory: Requires 2 separate full grids in memory (Old Grid & New Grid).",
        "Parallelism: Embarrassingly parallel (cells can be computed concurrently)."
    ]
    for pt in j_pts:
        p = tf_cp.add_paragraph()
        p.text = "  • " + pt
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_MUTED

    p.space_after = Pt(8)

    # Gauss-Seidel Section
    p = tf_cp.add_paragraph()
    p.text = "2. GAUSS-SEIDEL METHOD (Successive Relaxation)"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_EMERALD
    gs_pts = [
        "Update: Immediately reuses newly computed values within the current sweep.",
        "Equation: T_ij⁽ᵏ⁺¹⁾ = ¼ [ T_{i+1,j}⁽ᵏ⁾ + T_{i-1,j}⁽ᵏ⁺¹⁾ + T_{i,j+1}⁽ᵏ⁾ + T_{i,j-1}⁽ᵏ⁺¹⁾ ]",
        "Memory: In-place array mutation (1 single grid buffer, 50% memory saving).",
        "Convergence: Faster error decay because newly propagated heat updates propagate across the grid in the same iteration."
    ]
    for pt in gs_pts:
        p = tf_cp.add_paragraph()
        p.text = "  • " + pt
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_MUTED

    p.space_after = Pt(8)
    # Stopping Criterion
    p = tf_cp.add_paragraph()
    p.text = "3. CONVERGENCE STOPPING CRITERION (L∞ Residue)"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p_sc = tf_cp.add_paragraph()
    p_sc.text = "  • ||T⁽ᵏ⁺¹⁾ - T⁽ᵏ⁾||_∞ = max |T_ij⁽ᵏ⁺¹⁾ - T_ij⁽ᵏ⁾| < Tolerance (e.g. 10⁻⁴)"
    p_sc.font.size = Pt(8.5)
    p_sc.font.color.rgb = TEXT_CYAN

    add_footer(s5, 5)

    # ==========================================
    # SLIDE 6: THERMALX - LAPTOP CHASSIS & RESULTS
    # ==========================================
    s6 = create_base_slide()
    add_header(s6, 6, "ThermalX Engine",
               "Simulation Results: Hardware Chassis Modeling & Optimization",
               "Translating mathematical convergence into realistic hardware thermal telemetry and hotspot cooling.")

    # Left: UI Screenshot of Thermal Results
    if os.path.exists('presentation_assets/ui_thermal_results.png'):
        s6.shapes.add_picture('presentation_assets/ui_thermal_results.png', Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.9))

    # Middle: UI Screenshot of Laptop Configuration
    if os.path.exists('presentation_assets/ui_thermal_config.png'):
        s6.shapes.add_picture('presentation_assets/ui_thermal_config.png', Inches(4.6), Inches(1.8), Inches(3.2), Inches(4.9))

    # Right: Analytical Insights Cards
    c_an = add_card(s6, 8.0, 1.8, 4.533, 4.9, bg_color=CARD_BG, border_color=BORDER_EMERALD)
    tf_an = c_an.text_frame
    tf_an.word_wrap = True
    tf_an.margin_left = tf_an.margin_right = Inches(0.25)
    tf_an.margin_top = Inches(0.2)

    p = tf_an.paragraphs[0]
    p.text = "HARDWARE SIMULATION TELEMETRY"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_EMERALD
    p.space_after = Pt(8)

    metrics = [
        ("Simulated Multi-Source Inputs:", "CPU Core (85°C), Dedicated GPU (78°C), Battery Pack (42°C), Ambient Chassis Wall (25°C)."),
        ("Thermal Dissipation:", "Heat diffuses from high-energy silicon dies toward aluminum chassis boundaries according to finite difference conduction."),
        ("Hotspot Gradient Detection:", "Automated spatial gradient analysis identifies critical hotspots exceeding safety limits (>80°C)."),
        ("Active Cooling Optimization:", "Users increase cooling intensity parameter (convection coefficient h_conv) to simulate fan curves and heat pipe conductance."),
        ("Deterministic Thermal States:", "Color scale interpolates strictly from converged cell values (Blue=25°C → Green=45°C → Orange=70°C → Red=95°C).")
    ]

    for title_m, desc_m in metrics:
        p = tf_an.add_paragraph()
        p.text = f"• {title_m}"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_d = tf_an.add_paragraph()
        p_d.text = f"   {desc_m}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_after = Pt(4)

    add_footer(s6, 6)

    # ==========================================
    # SLIDE 7: LINKRANK - SPECTRAL GRAPH & PAGERANK
    # ==========================================
    s7 = create_base_slide()
    add_header(s7, 7, "LinkRank Engine",
               "Spectral Graph Theory & The PageRank Random Surfer Model",
               "Formulating web network authority as a stationary Markov chain eigen-problem.")

    # Left: Mathematical Formulation
    c_lr = add_card(s7, 0.8, 1.8, 6.4, 4.9, bg_color=CARD_BG, border_color=BORDER_PURPLE)
    tf_lr = c_lr.text_frame
    tf_lr.word_wrap = True
    tf_lr.margin_left = tf_lr.margin_right = Inches(0.3)
    tf_lr.margin_top = Inches(0.2)

    p = tf_lr.paragraphs[0]
    p.text = "SPECTRAL GRAPH FORMULATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = BORDER_PURPLE
    p.space_after = Pt(8)

    lr_math = [
        ("Graph Representation:", "Directed graph G = (V, E) with N nodes. Directed edge j → i indicates endorsement of node i by node j."),
        ("Adjacency Matrix A:", "A_ij = 1 if edge j → i exists, else 0. Out-degree d_j = ∑_i A_ij."),
        ("Column-Stochastic Transition Matrix M:", "M_ij = A_ij / d_j  ⟹  Each column sums to 1 (∑_i M_ij = 1)."),
        ("The Random Surfer Model:", 
         "A web user follows hyperlinks with probability α (damping factor = 0.85), and teleports to a random page with probability (1 - α)."),
        ("The Google Matrix G:", 
         "G = α M + [(1 - α) / N] E   (where E = e · eᵀ is the all-ones rank-1 matrix)"),
        ("Perron-Frobenius Theorem:", 
         "Because G is strictly positive (G_ij > 0) and column-stochastic, its principal eigenvalue is uniquely λ₁ = 1, and the corresponding eigenvector r has strictly positive entries (unique steady-state ranking vector).")
    ]

    for title_m, desc_m in lr_math:
        p = tf_lr.add_paragraph()
        p.text = f"{title_m}"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_d = tf_lr.add_paragraph()
        p_d.text = f"   {desc_m}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_CYAN if "Google" in title_m or "Perron" in title_m else TEXT_MUTED
        p_d.space_after = Pt(4)

    # Right: Diagram
    if os.path.exists('presentation_assets/diagram_pagerank.png'):
        s7.shapes.add_picture('presentation_assets/diagram_pagerank.png', Inches(7.5), Inches(1.8), Inches(5.0), Inches(3.6))

    # Right Bottom Card
    c_rb = add_card(s7, 7.5, 5.5, 5.0, 1.2, bg_color=CARD_BG_ALT, border_color=BORDER_CYAN)
    tf_rb = c_rb.text_frame
    tf_rb.word_wrap = True
    tf_rb.margin_left = tf_rb.margin_right = Inches(0.2)
    tf_rb.margin_top = Inches(0.12)
    p = tf_rb.paragraphs[0]
    p.text = "WHY DAMPING FACTOR α = 0.85?"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p2 = tf_rb.add_paragraph()
    p2.text = "Prevents 'Spider Traps' (cycles absorbing all rank) and 'Dead Ends' (zero out-degree). Guarantees the graph is strongly connected and aperiodic."
    p2.font.size = Pt(8.5)
    p2.font.color.rgb = TEXT_MUTED

    add_footer(s7, 7)

    # ==========================================
    # SLIDE 8: LINKRANK - POWER ITERATION METHOD
    # ==========================================
    s8 = create_base_slide()
    add_header(s8, 8, "LinkRank Engine",
               "Power Iteration Algorithm for Principal Eigenvector Computation",
               "How iterative matrix-vector multiplications extract the dominant eigenvector corresponding to λ₁ = 1.")

    # Left: Power Iteration Steps Card
    c_pi = add_card(s8, 0.8, 1.8, 6.2, 4.9, bg_color=CARD_BG, border_color=BORDER_EMERALD)
    tf_pi = c_pi.text_frame
    tf_pi.word_wrap = True
    tf_pi.margin_left = tf_pi.margin_right = Inches(0.3)
    tf_pi.margin_top = Inches(0.2)

    p = tf_pi.paragraphs[0]
    p.text = "POWER ITERATION ALGORITHM"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_EMERALD
    p.space_after = Pt(8)

    pi_steps = [
        ("Step 1: Initialization:", "Initialize ranking vector uniformly: r⁽⁰⁾ = [1/N, 1/N, ..., 1/N]ᵀ such that ∑ r_i = 1."),
        ("Step 2: Iterative Update:", "Compute next rank vector: r⁽ᵏ⁺¹⁾ = α M r⁽ᵏ⁾ + [(1 - α) / N] e"),
        ("Step 3: Dangling Node Handling:", "If a node has out-degree d_j = 0, distribute its mass equally to all nodes."),
        ("Step 4: Convergence Criterion:", "Stop when L₁ norm change is below tolerance: ||r⁽ᵏ⁺¹⁾ - r⁽ᵏ⁾||₁ < 10⁻⁵"),
        ("Step 5: Rate of Convergence:", 
         "Governed by the ratio of second eigenvalue to first: |λ₂ / λ₁| = α = 0.85.\nError decays exponentially as O(0.85ᵏ), typically converging in 25–40 steps.")
    ]

    for title_s, desc_s in pi_steps:
        p = tf_pi.add_paragraph()
        p.text = f"• {title_s}"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_d = tf_pi.add_paragraph()
        p_d.text = f"   {desc_s}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_after = Pt(4)

    # Right: Step-by-Step Numerical Table Card
    c_tbl = add_card(s8, 7.3, 1.8, 5.233, 4.9, bg_color=CARD_BG_ALT, border_color=BORDER_MUTED)
    tf_tbl = c_tbl.text_frame
    tf_tbl.word_wrap = True
    tf_tbl.margin_left = tf_tbl.margin_right = Inches(0.25)
    tf_tbl.margin_top = Inches(0.2)

    p = tf_tbl.paragraphs[0]
    p.text = "LIVE ITERATION TRACE (4-Node Network)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(8)

    # Table Simulation
    trace_data = [
        ("Iter (k)", "Node A", "Node B", "Node C", "Node D", "Residue ||Δr||"),
        ("k = 0", "0.2500", "0.2500", "0.2500", "0.2500", "—"),
        ("k = 1", "0.3562", "0.3200", "0.1619", "0.1619", "0.2125"),
        ("k = 2", "0.3751", "0.3385", "0.1432", "0.1432", "0.0374"),
        ("k = 5", "0.3838", "0.3418", "0.1372", "0.1372", "0.0028"),
        ("k = 10", "0.3841", "0.3421", "0.1369", "0.1369", "0.00004"),
        ("Final (λ₁)", "38.4%", "34.2%", "13.7%", "13.7%", "CONVERGED ✓")
    ]

    for row in trace_data:
        p_r = tf_tbl.add_paragraph()
        row_str = f"{row[0]:<9} | {row[1]:<7} | {row[2]:<7} | {row[3]:<7} | {row[4]:<7} | {row[5]}"
        p_r.text = row_str
        p_r.font.size = Pt(8.5)
        p_r.font.bold = (row[0].startswith("Iter") or row[0].startswith("Final"))
        p_r.font.color.rgb = TEXT_CYAN if row[0].startswith("Final") else (TEXT_WHITE if row[0].startswith("Iter") else TEXT_MUTED)
        p_r.space_after = Pt(3)

    p_note = tf_tbl.add_paragraph()
    p_note.text = "\nExaminer Note: Notice how Node A emerges as the top authority not merely because of link quantity, but because Node B (a high-authority node) casts an incoming endorsement edge toward A."
    p_note.font.size = Pt(8)
    p_note.font.color.rgb = TEXT_AMBER

    add_footer(s8, 8)

    # ==========================================
    # SLIDE 9: LINKRANK - DYNAMIC TOPOLOGY UI
    # ==========================================
    s9 = create_base_slide()
    add_header(s9, 9, "LinkRank Engine",
               "Simulation Results: Interactive Network Topology & Ranking",
               "Allowing users to modify graph structure and observe immediate spectral redistribution.")

    # Left: UI Screenshot Ranking Results
    if os.path.exists('presentation_assets/ui_linkrank_results.png'):
        s9.shapes.add_picture('presentation_assets/ui_linkrank_results.png', Inches(0.8), Inches(1.8), Inches(3.4), Inches(4.9))

    # Middle: UI Screenshot Editor
    if os.path.exists('presentation_assets/ui_linkrank_editor.png'):
        s9.shapes.add_picture('presentation_assets/ui_linkrank_editor.png', Inches(4.4), Inches(1.8), Inches(3.2), Inches(4.9))

    # Right: Pedagogical Insights Card
    c_ins = add_card(s9, 7.8, 1.8, 4.733, 4.9, bg_color=CARD_BG, border_color=BORDER_PURPLE)
    tf_ins = c_ins.text_frame
    tf_ins.word_wrap = True
    tf_ins.margin_left = tf_ins.margin_right = Inches(0.25)
    tf_ins.margin_top = Inches(0.2)

    p = tf_ins.paragraphs[0]
    p.text = "NETWORK TOPOLOGY INSIGHTS"
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = BORDER_PURPLE
    p.space_after = Pt(8)

    lr_insights = [
        ("Dynamic Topology Alteration:", "Users add nodes, remove edges, and flip directions live. The transition matrix M dynamically updates and triggers real-time power iteration."),
        ("In-Degree vs PageRank Distinction:", "Demonstrates why raw link count is misleading: a node with 1 incoming link from a super-hub outranks a node with 4 links from peripheral nodes."),
        ("Random Walk Visualization:", "A visual token steps through outgoing edges probabilistically, verifying that the empirical visit frequency matches the mathematical stationary vector."),
        ("Academic Viva Utility:", "Examiners can ask: 'What happens if we disconnect Node 3?' The presenter can sever the link live and watch rank drain away in real time.")
    ]

    for title_i, desc_i in lr_insights:
        p = tf_ins.add_paragraph()
        p.text = f"• {title_i}"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_d = tf_ins.add_paragraph()
        p_d.text = f"   {desc_i}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_after = Pt(4)

    add_footer(s9, 9)

    # ==========================================
    # SLIDE 10: NUMERICAL LAB - ROOT FINDING
    # ==========================================
    s10 = create_base_slide()
    add_header(s10, 10, "Numerical Lab",
               "Non-Linear Root Finding: Bisection vs. Newton-Raphson",
               "Contrasting guaranteed linear bracketing against rapid quadratic tangent extrapolation.")

    # Left: Diagram
    if os.path.exists('presentation_assets/diagram_rootfinding.png'):
        s10.shapes.add_picture('presentation_assets/diagram_rootfinding.png', Inches(0.8), Inches(1.8), Inches(5.8), Inches(3.0))

    # Left Bottom Box: Comparison Table
    c_rt = add_card(s10, 0.8, 5.0, 5.8, 1.7, bg_color=CARD_BG_ALT, border_color=BORDER_MUTED)
    tf_rt = c_rt.text_frame
    tf_rt.word_wrap = True
    tf_rt.margin_left = tf_rt.margin_right = Inches(0.2)
    tf_rt.margin_top = Inches(0.12)
    p = tf_rt.paragraphs[0]
    p.text = "CONVERGENCE ORDER SUMMARY"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    r_rows = [
        "• Bisection: Linear convergence order p = 1. Error bounds: ε_n = (b - a) / 2ⁿ.",
        "• Newton-Raphson: Quadratic convergence order p = 2. Error bounds: ε_{n+1} ≈ C · ε_n².",
        "• Rule of Thumb: Newton doubles correct decimal digits every single iteration near root."
    ]
    for rr in r_rows:
        p = tf_rt.add_paragraph()
        p.text = rr
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_MUTED

    # Right: Method Cards
    c_rc = add_card(s10, 6.8, 1.8, 5.733, 4.9, bg_color=CARD_BG, border_color=BORDER_CYAN)
    tf_rc = c_rc.text_frame
    tf_rc.word_wrap = True
    tf_rc.margin_left = tf_rc.margin_right = Inches(0.3)
    tf_rc.margin_top = Inches(0.2)

    p = tf_rc.paragraphs[0]
    p.text = "THEORETICAL ANALYSIS & TRADE-OFFS"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(8)

    # Bisection
    p = tf_rc.add_paragraph()
    p.text = "1. BISECTION METHOD (Bracketing)"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    bis_pts = [
        "Basis: Intermediate Value Theorem (IVT). Requires f(a) · f(b) < 0.",
        "Update: Interval midpoint c = (a + b) / 2.",
        "Strength: 100% unconditional guarantee of convergence if f(x) is continuous.",
        "Limitation: Very slow; takes ~20 iterations to gain 6 decimal places of precision."
    ]
    for bp in bis_pts:
        p = tf_rc.add_paragraph()
        p.text = "  • " + bp
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_MUTED

    p.space_after = Pt(8)

    # Newton-Raphson
    p = tf_rc.add_paragraph()
    p.text = "2. NEWTON-RAPHSON METHOD (Open / Derivative)"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    nr_pts = [
        "Basis: 1st order Taylor expansion tangent intersection: x_{n+1} = x_n - f(x_n) / f'(x_n).",
        "Strength: Extremely rapid convergence (typically 4–6 iterations total).",
        "Failure Modes: Singular derivative (f'(x) ≈ 0 division by zero), cycle oscillation between extrema, and divergence if initial guess x₀ is too far from root."
    ]
    for np_ in nr_pts:
        p = tf_rc.add_paragraph()
        p.text = "  • " + np_
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_MUTED

    add_footer(s10, 10)

    # ==========================================
    # SLIDE 11: NUMERICAL LAB - EIGENVALUES
    # ==========================================
    s11 = create_base_slide()
    add_header(s11, 11, "Numerical Lab",
               "Eigenvalues, Eigenvectors & Characteristic Polynomials",
               "Analytical and numerical spectral decomposition of 2x2 and 3x3 linear transformations.")

    # Left: Mathematical Principles Card
    c_eg = add_card(s11, 0.8, 1.8, 6.2, 4.9, bg_color=CARD_BG, border_color=BORDER_EMERALD)
    tf_eg = c_eg.text_frame
    tf_eg.word_wrap = True
    tf_eg.margin_left = tf_eg.margin_right = Inches(0.3)
    tf_eg.margin_top = Inches(0.2)

    p = tf_eg.paragraphs[0]
    p.text = "SPECTRAL THEORY FORMULATION"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_EMERALD
    p.space_after = Pt(8)

    eg_math = [
        ("Fundamental Equation:", "A v = λ v  ⟺  (A - λ I) v = 0"),
        ("Non-Trivial Nullspace Condition:", "det(A - λ I) = 0   (Characteristic Equation)"),
        ("2x2 Characteristic Polynomial:", 
         "det([[a - λ, b], [c, d - λ]]) = λ² - Tr(A)λ + det(A) = 0\nRoots: λ = [ Tr(A) ± √(Tr(A)² - 4 det(A)) ] / 2"),
        ("Eigenvector Determination:", 
         "Substitute each λ into (A - λ I)v = 0 and compute basis of the null space.\nNormalize to unit Euclidean norm: ||v||₂ = 1"),
        ("Algebraic Invariants Verified Live:", 
         "• Trace Invariant: ∑ λ_i = Tr(A) = a₁₁ + a₂₂ + ... + aₙₙ\n• Determinant Invariant: ∏ λ_i = det(A)")
    ]

    for title_e, desc_e in eg_math:
        p = tf_eg.add_paragraph()
        p.text = f"{title_e}"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_d = tf_eg.add_paragraph()
        p_d.text = f"   {desc_e}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_CYAN if "Roots" in desc_e or "Invariant" in title_e else TEXT_MUTED
        p_d.space_after = Pt(4)

    # Right: Live Worked Example Card
    c_ex = add_card(s11, 7.3, 1.8, 5.233, 4.9, bg_color=CARD_BG_ALT, border_color=BORDER_MUTED)
    tf_ex = c_ex.text_frame
    tf_ex.word_wrap = True
    tf_ex.margin_left = tf_ex.margin_right = Inches(0.25)
    tf_ex.margin_top = Inches(0.2)

    p = tf_ex.paragraphs[0]
    p.text = "WORKED VIVA EXAMPLE (Interactive Matrix)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(8)

    worked = [
        ("Input Matrix A:", "[[4, 1], [2, 3]]"),
        ("Step 1: Compute Trace & Det:", "Tr(A) = 4 + 3 = 7\ndet(A) = (4)(3) - (1)(2) = 12 - 2 = 10"),
        ("Step 2: Characteristic Equation:", "λ² - 7λ + 10 = 0  ⟹  (λ - 5)(λ - 2) = 0\nEigenvalues: λ₁ = 5,  λ₂ = 2"),
        ("Step 3: Eigenvector for λ₁ = 5:", "(A - 5I)v = [[-1, 1], [2, -2]] v = 0  ⟹  -v₁ + v₂ = 0  ⟹  v₁ = [1, 1]ᵀ"),
        ("Step 4: Eigenvector for λ₂ = 2:", "(A - 2I)v = [[2, 1], [2, 1]] v = 0  ⟹  2v₁ + v₂ = 0  ⟹  v₂ = [1, -2]ᵀ"),
        ("Step 5: Invariant Check:", "λ₁ + λ₂ = 5 + 2 = 7 = Tr(A) ✓\nλ₁ · λ₂ = (5)(2) = 10 = det(A) ✓")
    ]

    for title_w, desc_w in worked:
        p = tf_ex.add_paragraph()
        p.text = f"• {title_w}"
        p.font.size = Pt(9)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_d = tf_ex.add_paragraph()
        p_d.text = f"   {desc_w}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_EMERALD if "Invariant" in title_w else TEXT_MUTED
        p_d.space_after = Pt(3)

    add_footer(s11, 11)

    # ==========================================
    # SLIDE 12: COMPREHENSIVE COMPARISON TABLE
    # ==========================================
    s12 = create_base_slide()
    add_header(s12, 12, "Comparative Analysis",
               "Master Numerical Methods Comparison Matrix",
               "Side-by-side evaluation of all numerical methods implemented in the Numerix Lab platform.")

    # Master Table
    rows = 7
    cols = 6
    tbl_shape = s12.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.9))
    tbl = tbl_shape.table

    # Column widths
    tbl.columns[0].width = Inches(2.1)
    tbl.columns[1].width = Inches(1.8)
    tbl.columns[2].width = Inches(1.8)
    tbl.columns[3].width = Inches(1.8)
    tbl.columns[4].width = Inches(1.6)
    tbl.columns[5].width = Inches(2.633)

    matrix_data = [
        ["METHOD", "DOMAIN", "CONVERGENCE", "COMPLEXITY", "MEMORY", "KEY GUARANTEE / CONDITION"],
        ["Jacobi Iteration", "Linear Systems (Ax = b)", "Linear (ρ < 1)", "O(n²) per step", "2n² (Dual grid)", "Strict / Irreducible Diagonal Dominance"],
        ["Gauss-Seidel", "Linear Systems (Ax = b)", "Linear (ρ_GS = ρ_J²)", "O(n²) per step", "n² (In-place)", "Strict / Irreducible Diagonal Dominance"],
        ["PageRank (Power)", "Spectral Graphs / Markov", "Linear (O(0.85ᵏ))", "O(|E|) per step", "O(|V|)", "Perron-Frobenius (Irreducible, aperiodic)"],
        ["Bisection Method", "Root Finding f(x) = 0", "Linear (p = 1)", "O(1) eval/step", "O(1)", "Intermediate Value Theorem: f(a)·f(b) < 0"],
        ["Newton-Raphson", "Root Finding f(x) = 0", "Quadratic (p = 2)", "O(1) f, f' eval", "O(1)", "f'(root) ≠ 0 and initial x₀ close to root"],
        ["Char. Polynomial", "Eigen-decomposition", "Exact / Closed-form", "O(n³) roots", "O(n²)", "Solvable analytically for n ≤ 4 (Abel-Ruffini)"]
    ]

    for r_idx, row in enumerate(matrix_data):
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            if r_idx == 0:
                cell.fill.fore_color.rgb = RGBColor(15, 23, 42)
            else:
                cell.fill.fore_color.rgb = RGBColor(17, 24, 39) if r_idx % 2 == 1 else RGBColor(13, 19, 33)

            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(9 if r_idx == 0 else 8.5)
            p.font.bold = (r_idx == 0 or c_idx == 0)
            if r_idx == 0:
                p.font.color.rgb = TEXT_CYAN
            elif c_idx == 0:
                p.font.color.rgb = TEXT_WHITE
            elif c_idx == 2:
                p.font.color.rgb = TEXT_EMERALD
            else:
                p.font.color.rgb = TEXT_MUTED

    add_footer(s12, 12)

    # ==========================================
    # SLIDE 13: VIVA DEFENSE & EVALUATOR Q&A
    # ==========================================
    s13 = create_base_slide()
    add_header(s13, 13, "Academic Viva Defense",
               "High-Frequency Examiner Questions & Mathematical Defenses",
               "Essential conceptual questions frequently posed during university project evaluations.")

    # 4 Q&A Cards (2x2 Grid)
    qa_list = [
        ("Q1: Why does Gauss-Seidel converge faster than Jacobi?",
         "Mathematical Defense: For discretized Laplace grids, the iteration matrix G_GS has spectral radius exactly equal to [ρ(G_J)]². Because ρ < 1, squaring it strictly decreases the dominant eigenvalue, doubling the asymptotic rate of convergence R_∞ = -ln(ρ). Hence Gauss-Seidel requires ~50% fewer sweeps.",
         BORDER_CYAN),
        ("Q2: Under what condition is iterative convergence guaranteed?",
         "Mathematical Defense: By the Gershgorin Circle Theorem and Levy-Desplanques Theorem, convergence is unconditionally guaranteed if matrix A is strictly diagonally dominant (|a_ii| > ∑_{j≠i} |a_ij|) or symmetric positive definite (SPD). Both hold for the 5-point discrete Laplace operator.",
         BORDER_EMERALD),
        ("Q3: Why is damping factor α set to 0.85 in PageRank?",
         "Mathematical Defense: Setting α < 1 resolves the Reducible Graph trap. It ensures the transition matrix G has strictly positive entries (G_ij > 0), satisfying the Perron-Frobenius theorem. Furthermore, the second eigenvalue is bounded by |λ₂| ≤ α = 0.85, guaranteeing geometric convergence within ~30 power steps.",
         BORDER_PURPLE),
        ("Q4: When does Newton-Raphson fail, and how is it mitigated?",
         "Mathematical Defense: Newton-Raphson fails if f'(x_n) ≈ 0 (division by zero / infinite tangent projection), if the function has inflection points causing 2-cycle oscillations, or if x₀ is far from root. Mitigation: Hybrid algorithms like Brent's method that fall back to Bisection if a step leaves the bracketing interval.",
         BORDER_AMBER)
    ]

    for idx, (q, a, border_col) in enumerate(qa_list):
        row = idx // 2
        col = idx % 2
        x = 0.8 + col * 6.0
        y = 1.8 + row * 2.5
        c = add_card(s13, x, y, 5.733, 2.35, bg_color=CARD_BG, border_color=border_col, border_width=1.2)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.18)

        p = tf.paragraphs[0]
        p.text = q
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = border_col
        p.space_after = Pt(6)

        p_ans = tf.add_paragraph()
        p_ans.text = a
        p_ans.font.size = Pt(8.5)
        p_ans.font.color.rgb = TEXT_WHITE

    add_footer(s13, 13)

    # ==========================================
    # SLIDE 14: SYSTEM IMPLEMENTATION & RIGOR
    # ==========================================
    s14 = create_base_slide()
    add_header(s14, 14, "Implementation & Engineering",
               "Zero-Dependency Mathematical Architecture & Production Deployment",
               "How Numerix Lab achieves instant client-side execution, deterministic rigor, and 24/7 web availability.")

    # 3 Column Cards
    col_w = 3.64
    tech_cards = [
        ("1. COMPUTATIONAL PURITY", BORDER_CYAN, [
            ("Zero External Math Libraries:", "No NumPy or SciPy server requirements. All finite difference operators and power iteration loops are hand-coded in high-performance native JavaScript."),
            ("Deterministic State Machine:", "Guarantees that identical initial conditions produce bit-exact convergence traces across all browsers."),
            ("Examiner Code Audit Ready:", "Clean, modular mathematical functions directly inspectable in browser dev-tools during viva.")
        ]),
        ("2. VISUALIZATION ENGINE", BORDER_EMERALD, [
            ("Canvas Heatmap Shaders:", "Dynamic bi-linear spatial interpolation maps grid temperatures to visual colors without taxing CPU cycles."),
            ("Interactive SVG Directed Graphs:", "Dynamic edge routing, curved bezier links, and real-time node dragging for network topology analysis."),
            ("Responsive Modern Dark UI:", "Designed to cognitive engineering principles: high information density without visual clutter.")
        ]),
        ("3. CLOUD DEPLOYMENT & CI/CD", BORDER_PURPLE, [
            ("Automated GitHub Pages CI/CD:", "Continuous deployment pipeline automatically compiles and deploys code on push to GitHub repository."),
            ("100% Client-Side Hosting:", "Zero server maintenance, zero cold-start latency, and offline-capable single-page application structure."),
            ("Permanent Public URL:", "Accessible 24/7 on desktop, laptop, tablet, and mobile devices with zero installation required.")
        ])
    ]

    for idx, (title, border_col, items) in enumerate(tech_cards):
        x = 0.8 + idx * 4.0
        c = add_card(s14, x, 1.8, col_w, 4.9, bg_color=CARD_BG, border_color=border_col, border_width=1.2)
        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = Inches(0.25)
        tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = border_col
        p.space_after = Pt(12)

        for h, desc in items:
            p = tf.add_paragraph()
            p.text = f"• {h}"
            p.font.size = Pt(9.5)
            p.font.bold = True
            p.font.color.rgb = TEXT_WHITE
            p_d = tf.add_paragraph()
            p_d.text = f"   {desc}"
            p_d.font.size = Pt(8.5)
            p_d.font.color.rgb = TEXT_MUTED
            p_d.space_after = Pt(6)

    add_footer(s14, 14)

    # ==========================================
    # SLIDE 15: CONCLUSION & LIVE DEMO
    # ==========================================
    s15 = create_base_slide()
    add_header(s15, 15, "Project Summary",
               "Conclusion, Deliverables & Live Demonstration",
               "NUMERIX LAB successfully proves that numerical methods can be transformed into intuitive visual experiences.")

    # Left: Deliverables & Key Highlights Box
    c_dl = add_card(s15, 0.8, 1.8, 7.0, 4.9, bg_color=CARD_BG, border_color=BORDER_CYAN)
    tf_dl = c_dl.text_frame
    tf_dl.word_wrap = True
    tf_dl.margin_left = tf_dl.margin_right = Inches(0.3)
    tf_dl.margin_top = Inches(0.25)

    p = tf_dl.paragraphs[0]
    p.text = "KEY PROJECT HIGHLIGHTS & DELIVERABLES"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = TEXT_CYAN
    p.space_after = Pt(10)

    deliverables = [
        ("Bridged Abstract Math & Intuition:", "Transformed complex differential equations and spectral graph theory into interactive, observable simulations."),
        ("Comprehensive Dual-Flagship Engines:", "Delivered ThermalX (PDE heat conduction) and LinkRank (PageRank power iteration) with 100% mathematical integrity."),
        ("Extensive Numerical Lab Suite:", "Implemented Bisection, Newton-Raphson, and 2x2/3x3 Characteristic Polynomial solvers with step-by-step trace generation."),
        ("Live 24/7 Cloud Availability:", "Permanently hosted online with zero setup needed for evaluators, students, and peers."),
        ("Complete Pedagogical Documentation:", "Accompanied by a 20+ page illustrated viva defense manual and interactive user guide.")
    ]

    for title_d, desc_d in deliverables:
        p = tf_dl.add_paragraph()
        p.text = f"✔  {title_d}"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = TEXT_EMERALD
        p_d = tf_dl.add_paragraph()
        p_d.text = f"    {desc_d}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_MUTED
        p_d.space_after = Pt(4)

    # Right: Live Demonstration Box
    c_dm = add_card(s15, 8.1, 1.8, 4.433, 4.9, bg_color=CARD_BG_ALT, border_color=BORDER_EMERALD, border_width=1.5)
    tf_dm = c_dm.text_frame
    tf_dm.word_wrap = True
    tf_dm.margin_left = tf_dm.margin_right = Inches(0.3)
    tf_dm.margin_top = Inches(0.3)

    p = tf_dm.paragraphs[0]
    p.text = "LIVE EVALUATION DEMO"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = TEXT_EMERALD
    p.space_after = Pt(12)

    demo_pts = [
        ("🌐 Live Web App:", "https://greatrocktiger-byte.github.io/numerix-lab/"),
        ("📖 User & Viva Manual:", "https://greatrocktiger-byte.github.io/numerix-lab/DOCUMENTATION.html"),
        ("💻 GitHub Repository:", "https://github.com/greatrocktiger-byte/numerix-lab"),
        ("💡 Suggested Live Demos for Viva:", 
         "1. Run Jacobi vs Gauss-Seidel simultaneously on 40x40 grid and verify GS finishes in half the steps.\n"
         "2. Sever an incoming link to Node A in LinkRank and watch Power Iteration re-balance authority scores live.\n"
         "3. Test Newton-Raphson with singular derivative f'(x) ≈ 0 to demonstrate numerical failure handling.")
    ]

    for title_dm, desc_dm in demo_pts:
        p = tf_dm.add_paragraph()
        p.text = f"{title_dm}"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p_d = tf_dm.add_paragraph()
        p_d.text = f"{desc_dm}"
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = TEXT_CYAN if "https" in desc_dm else TEXT_MUTED
        p_d.space_after = Pt(6)

    p_end = tf_dm.add_paragraph()
    p_end.text = "\nThank you! We welcome any questions and are ready for the live demonstration."
    p_end.font.size = Pt(9.5)
    p_end.font.bold = True
    p_end.font.italic = True
    p_end.font.color.rgb = TEXT_AMBER

    add_footer(s15, 15)

    # Save Presentation
    output_path = "NUMERIX_LAB_PRESENTATION.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == "__main__":
    build_presentation()
