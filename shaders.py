from OpenGL.GL import *

def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not result:
        error = glGetShaderInfoLog(shader)
        raise RuntimeError(f"Shader compile error: {error}")
    return shader

def create_shader_program(vertex_src, fragment_src):
    vertex_shader = compile_shader(vertex_src, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_src, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)
    result = glGetProgramiv(program, GL_LINK_STATUS)
    if not result:
        error = glGetProgramInfoLog(program)
        raise RuntimeError(f"Program link error: {error}")
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)
    return program


vertex_solid_shader_source = """
#version 330 core

layout (location = 0) in vec2 aPos;

void main() {
    gl_Position = vec4(aPos, 0.0, 1.0);
}
"""

vertex_textured_shader_source = """
#version 330 core

layout(location = 0) in vec2 aPos;
layout(location = 1) in vec2 aTex;

out vec2 TexCoord;

void main(){
    gl_Position = vec4(aPos, 0.0, 1.0);
    TexCoord = aTex;
}
"""

fragment_solid_shader_source = """
#version 330 core

out vec4 FragColor;

void main() {
    FragColor = vec4(0.2, 0.8, 0.3, 1.0); // any color you want
}
"""

fragment_textured_shader_source = """
#version 330 core

in vec2 TexCoord;
out vec4 FragColor;

uniform sampler2D tex;

void main()
{
    FragColor = texture(tex, TexCoord);
}
"""
