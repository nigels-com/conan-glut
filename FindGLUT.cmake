if(NOT APPLE)
  find_path(GLUT_INCLUDE_DIR NAMES GL/glut.h PATHS {CONAN_INCLUDE_DIRS_GLUT} NO_CMAKE_FIND_ROOT_PATH)
  find_library(GLUT_LIBRARY NAMES ${CONAN_LIBS_GLUT} PATHS ${CONAN_LIB_DIRS_GLUT} NO_CMAKE_FIND_ROOT_PATH)
endif()

if(MSVC)
  set(GLUT_LIBRARY ${GLUT_LIBRARY} glu32 opengl32 gdi32 winmm user32)
endif()
if(APPLE)
  set(GLUT_LIBRARY "-framework GLUT" "-framework OpenGL")
  set(GLUT_INCLUDE_DIR)
endif()
if(UNIX AND NOT APPLE)
  set(GLUT_LIBRARY ${GLUT_LIBRARY} -lGLU -lGL -lXi -lXext -lXxf86vm -lX11 -lm)
endif()

set(GLUT_FOUND TRUE)
set(GLUT_INCLUDE_DIRS ${GLUT_INCLUDE_DIR})
set(GLUT_LIBRARIES ${GLUT_LIBRARY})

message(STATUS "** GLUT FOUND BY CONAN!")
message(STATUS "** FOUND GLUT LIRBARY: ${GLUT_LIBRARY}")
message(STATUS "** FOUND GLUT INCLUDE: ${GLUT_INCLUDE_DIR}")

mark_as_advanced(GLUT_LIBRARY GLUT_INCLUDE_DIR)
