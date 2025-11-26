import glfw
from vertices import heli_vertices, rear_blade_vertices, main_prop_vertices
from geometric_transformations import *
from OpenGL.GL import *
from shaders import create_shader_program

vertex_shader_source = """
#version 330 core

layout (location = 0) in vec2 aPos;
layout (location = 1) in vec2 aTex;

out vec2 TexCoord;

void main() {
    gl_Position = vec4(aPos, 0.0, 1.0);
    TexCoord = aTex;
}
"""
fragment_shader_source = """
#version 330 core

in vec2 TexCoord;
out vec4 FragColor;

uniform sampler2D ourTexture;

void main()
{
    FragColor = texture(ourTexture, TexCoord);
}
"""

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
    shader = create_shader_program(vertex_shader_source, fragment_shader_source)

    vertices = heli_vertices + make_circle_vertices(-0.15, -0.038, 0.062, 40)
    vertices = (GLfloat * len(vertices))(*vertices)

    # Main static body setup
    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)

    glBindVertexArray(VAO)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, vertices, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
    glBindVertexArray(0)
    
    # Main propeller setup
    main_prop_cx = 0.04
    main_prop_cy = 0.13
    main_prop_VAO = glGenVertexArrays(1)
    main_prop_VBO = glGenBuffers(1)
    
    # Back propeller setup
    tail_cx = 0.65
    tail_cy = 0.13
    back_prop_angle = 0.0
    back_prop_VAO = glGenVertexArrays(1)
    back_prop_VBO = glGenBuffers(1)
    
    # Main loop
    while not glfw.window_should_close(window):
        glClearColor(0.3, 0.3, 0.3, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(shader)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLES, 0, len(vertices) // 2)
        
        # Back Propeller update
        back_prop_angle += 0.1  # speed — adjust as needed
        blade1 = rotate_and_translate(rear_blade_vertices, tail_cx, tail_cy, back_prop_angle)
        blade2 = rotate_and_translate(rear_blade_vertices, tail_cx, tail_cy, back_prop_angle + math.pi/2)

        back_prop_vertices = blade1 + blade2
        
        glBindVertexArray(back_prop_VAO)
        glBindBuffer(GL_ARRAY_BUFFER, back_prop_VBO)
        rotor_data = (GLfloat * len(back_prop_vertices))(*back_prop_vertices)
        glBufferData(GL_ARRAY_BUFFER, len(back_prop_vertices) * 4, rotor_data, GL_DYNAMIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
        glUseProgram(shader)
        glDrawArrays(GL_TRIANGLES, 0, len(back_prop_vertices)//2)
        
        # Main Propeller update
        scale = 0.1 + 0.9 * abs(math.sin(glfw.get_time() * 20.0))
        main_rotor_vertices = scale_translate_x_vertices(main_prop_vertices, main_prop_cx, main_prop_cy, scale)
        
        glBindVertexArray(main_prop_VAO)
        glBindBuffer(GL_ARRAY_BUFFER, main_prop_VBO)
        data = (GLfloat * len(main_rotor_vertices))(*main_rotor_vertices)
        glBufferData(GL_ARRAY_BUFFER, len(main_rotor_vertices) * 4, data, GL_DYNAMIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)

        glDrawArrays(GL_TRIANGLES, 0, len(main_rotor_vertices)//2)

        glfw.swap_buffers(window)
        glfw.poll_events()
        
    glfw.terminate()

if __name__ == "__main__":
    main()
