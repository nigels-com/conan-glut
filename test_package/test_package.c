#include <GL/glut.h>
#include <GL/freeglut_ext.h> /* GLUT_VERSION support */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[])
{
	/* Need X11 display to actually run at all */
#if 0
	glutInit(argc, argv);
    printf("Bincrafters FreeGLUT %d\n", glutGet(GLUT_VERSION));
#else
    printf("Bincrafters FreeGLUT\n");
#endif
    return EXIT_SUCCESS;
}
