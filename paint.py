from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

rot = 0

Width = 1600
Height = 1080


def keyPressed(*args):
    if args[0] == ESCAPE:
        sys.exit()


def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)


def ReSizeGLScene(Width, Height):
    if Height == 0: Height = 1
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    global rot
    rot = (rot + 1) % 360  # увеличиваем угол поворота

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # очищаем экран
    glLoadIdentity()  # восстанавливаем мировые координаты

    glTranslatef(0.0, 0.0, -10.0)

    glRotatef(rot, 1.0, 0.0, 0.0)
    glRotatef(rot, 0.0, 1.0, 0.0)
    glRotatef(rot, 0.0, 0.0, 1.0)

    glColor4f(0.0, 0.7, 0.1, 1)
    glutSolidCube(3)

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(Width, Height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Cards game")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(Width, Height)
    glutMainLoop()
