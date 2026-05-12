transform slide_in_left:
    xalign -0.9
    yalign 1.0
    alpha 0.0
    zoom 0.9
    linear 0.5 xalign 0.1 alpha 1.0

transform slide_in_right:
    xalign 1.5
    yalign 1.0
    alpha 0.0
    zoom 0.9
    linear 0.5 xalign 0.9 alpha 1.0

transform gentle_sway:

    ease 0.5 yoffset 1 xoffset -10
    ease 0.5 yoffset -2 xoffset -20
    ease 0.5 yoffset 0 xoffset -15

    repeat