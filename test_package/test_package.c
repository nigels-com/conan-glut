#if __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#include <GL/freeglut_ext.h> /* GLUT_VERSION support */
#endif

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[])
{
#if __APPLE__
    glutInit(&argc, argv);
    printf("Bincrafters MacOS GLUT\n");
    return EXIT_SUCCESS;
#elif WIN32
    glutInit(&argc, argv);
    printf("Bincrafters FreeGLUT %d\n", glutGet(GLUT_VERSION));
    return EXIT_SUCCESS;
#else
    /* Need X11 display to init GLUT */
    if (getenv("DISPLAY")!=NULL)
    {
        glutInit(&argc, argv);
        printf("Bincrafters FreeGLUT %d\n", glutGet(GLUT_VERSION));
    }
    else
    {
        printf("Bincrafters FreeGLUT\n");
    }
    return EXIT_SUCCESS;
#endif
}
