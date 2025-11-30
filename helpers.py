import math

#----------------- Geometric Transformations -----------------

def make_circle_vertices(cx, cy, radius, segments=40):
    vertices = []

    for i in range(segments):
        angle1 = (2 * math.pi / segments) * i
        angle2 = (2 * math.pi / segments) * (i + 1)

        # center
        vertices.append(cx)
        vertices.append(cy)

        # first point on edge
        vertices.append(cx + radius * math.cos(angle1))
        vertices.append(cy + radius * math.sin(angle1))

        # second point on edge
        vertices.append(cx + radius * math.cos(angle2))
        vertices.append(cy + radius * math.sin(angle2))

    return vertices

def rotate_and_translate(vertices, cx, cy, angle):
    out = []
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)

    for i in range(0, len(vertices), 2):
        x = vertices[i]
        y = vertices[i+1]

        # Rotate around origin
        xr = x * cos_a - y * sin_a
        yr = x * sin_a + y * cos_a

        # Move (translate) to rotor center
        out.append(xr + cx)
        out.append(yr + cy)

    return out

def scale_translate_x_vertices(vertices, cx, cy, scale):
    out = []
    for i in range(0, len(vertices), 2):
        x = vertices[i]
        y = vertices[i+1]

        # Scale around cx and move to cx
        new_x = x * scale + cx

        # Move to cy
        new_y = y + cy

        out.append(new_x)
        out.append(new_y)

    return out

