import glfw
from vertices import heli_vertices, rear_blade_vertices, main_prop_vertices
from geometric_transformations import *
from OpenGL.GL import *
from shaders import *


# ----------------- Helper to create a single VAO/VBO pair -----------------
def create_buffer():
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)
    return {"vao": vao, "vbo": vbo}


def upload_vertices(buffer, data, usage=GL_STATIC_DRAW):
    glBindVertexArray(buffer["vao"])
    glBindBuffer(GL_ARRAY_BUFFER, buffer["vbo"])

    data_gl = (GLfloat * len(data))(*data)
    glBufferData(GL_ARRAY_BUFFER, len(data) * 4, data_gl, usage)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)


# -------------------------------------------------------------------------


def main():

    # Window creation
    if not glfw.init():
        raise Exception("GLFW could not be initialized")

    window = glfw.create_window(1200, 1200, "CG Helicopter", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Failed to create GLFW window")
    glfw.make_context_current(window)
    
    # Shaders
    shader = create_shader_program(vertex_solid_shader_source, fragment_solid_shader_source)

    # ------------------ STATIC HELICOPTER BODY ------------------
    body_vertices = heli_vertices + make_circle_vertices(-0.15, -0.038, 0.062, 40)

    body_buffer = create_buffer()
    upload_vertices(body_buffer, body_vertices, GL_STATIC_DRAW)

    # ------------------ MOVING PARTS BUFFERS --------------------
    main_prop_buffer  = create_buffer()   # only ONE var
    back_prop_buffer  = create_buffer()   # only ONE var

    # Centers
    main_prop_cx = 0.04
    main_prop_cy = 0.13
    tail_cx = 0.65
    tail_cy = 0.13

    back_prop_angle = 0.0

    # ----------------------------- MAIN LOOP -----------------------------
    while not glfw.window_should_close(window):
        glClearColor(0.1, 0.1, 0.1, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(shader)

        # Draw static body
        glBindVertexArray(body_buffer["vao"])
        glDrawArrays(GL_TRIANGLES, 0, len(body_vertices)//2)

        # ------------------ Back propeller animation ------------------
        back_prop_angle += 0.1

        blade1 = rotate_and_translate(rear_blade_vertices, tail_cx, tail_cy, back_prop_angle)
        blade2 = rotate_and_translate(rear_blade_vertices, tail_cx, tail_cy, back_prop_angle + math.pi/2)
        back_prop_vertices = blade1 + blade2

        upload_vertices(back_prop_buffer, back_prop_vertices, GL_DYNAMIC_DRAW)

        glBindVertexArray(back_prop_buffer["vao"])
        glDrawArrays(GL_TRIANGLES, 0, len(back_prop_vertices)//2)

        # ------------------ Main propeller animation ------------------
        scale = 0.1 + 0.9 * abs(math.sin(glfw.get_time() * 20.0))
        main_rotor_vertices = scale_translate_x_vertices(main_prop_vertices, main_prop_cx, main_prop_cy, scale)

        upload_vertices(main_prop_buffer, main_rotor_vertices, GL_DYNAMIC_DRAW)

        glBindVertexArray(main_prop_buffer["vao"])
        glDrawArrays(GL_TRIANGLES, 0, len(main_rotor_vertices)//2)

        # -----------------------------------------------------------------

        glfw.swap_buffers(window)
        glfw.poll_events()
        
    glfw.terminate()


if __name__ == "__main__":
    main()
