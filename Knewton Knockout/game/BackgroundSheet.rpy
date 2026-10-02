# 1. Pulsing Solar Glow + Slow Ken Burns Camera Movement
image bg_sun_animated:
    "images/backgrounds/sun_background01.png"
    subpixel True
    xalign 0.5 yalign 0.5 zoom 1.0
    
    # Layer 1: Pulse the warm yellow tint & brightness (simulates sun beating down)
    parallel:
        easein_quad 3.5 matrixcolor TintMatrix("#fffaed") * BrightnessMatrix(0.04)
        easeout_quad 3.5 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
        repeat

    # Layer 2: Extremely slow, subtle pan/zoom toward the sun
    parallel:
        easein_quad 10.0 zoom 1.05 yalign 0.42
        easeout_quad 10.0 zoom 1.0 yalign 0.5
        repeat

# 2. Golden Sun-Mote Particle Overlay
image sun_particles = SnowBlossom(
    "images/particles/sun_mote.png", # A tiny soft yellow dot PNG
    count=40,
    border=50,
    xspeed=(-15, 15),
    yspeed=(-25, -8),
    start=0.0
)