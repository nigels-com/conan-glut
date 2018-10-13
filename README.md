## Package Status

| Bintray | Windows | Linux |
|:--------:|:---------:|:-----------------:|
|[![Download](https://api.bintray.com/packages/nigels-com/conan/glut/images/download.svg) ](https://bintray.com/nigels-com/conan/glut/_latestVersion)|[![Build status](https://ci.appveyor.com/api/projects/status/8xeq7qmjuh59f776/branch/testing/3.0.0?svg=true)](https://ci.appveyor.com/project/nigels-com/conan-glut/branch/testing/3.0.0)|[![Build Status](https://travis-ci.org/nigels-com/conan-glut.svg?branch=testing%2F3.0.0)](https://travis-ci.org/nigels-com/conan-glut)|

This build of [FreeGLUT](http://freeglut.sourceforge.net/) using [Conan](https://conan.io/) and [Bincrafters tools](https://github.com/bincrafters) is under development.
Ubuntu 18.0 with gcc 7 works.
[Travis](https://travis-ci.org/) and [AppVeyor](https://www.appveyor.com/) builds for Linux and Windows are actively maintained.
Mac support is under consideration for X11/GLX. 

## User Guide

### Basic setup

    $ conan install glut/3.0.0@bincrafters/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    glut/3.0.0@bincrafters/testing

    [generators]
    cmake

    [options]
    glut:shared=False

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.
