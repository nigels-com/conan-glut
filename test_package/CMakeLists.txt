project(test_package)
cmake_minimum_required(VERSION 2.8.11)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(GLUT REQUIRED)
find_package(OpenGL REQUIRED)

add_executable(${PROJECT_NAME} test_package.c)
target_include_directories(${PROJECT_NAME} PUBLIC ${OPENGL_INCLUDE_DIR} ${GLUT_INCLUDE_DIR})
target_link_libraries(${PROJECT_NAME} PUBLIC ${GLUT_LIBRARIES} ${OPENGL_LIBRARIES})
