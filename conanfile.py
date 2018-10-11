#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibnameConan(ConanFile):
    name = "glut"
    version = "3.0.0"
    description = "FreeGLUT is a free-software/open-source alternative to the OpenGL Utility Toolkit (GLUT) library."
    homepage = "https://github.com/dcnieho/FreeGLUT"
    url = "http://freeglut.sourceforge.net/"
    author = "John F. Fay, John Tsiombikas and Diederick C. Niehorster"
    license = "X-Consortium"

    # Packages the license for the conanfile.py
    exports = ["freeglut/freeglut/COPYING"]

    # Remove following lines if the target lib does not use cmake.
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    # Options may need to change depending on the packaged library.
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    requires = ()

    def system_requirements(self):
        if tools.os_info.is_linux:
            if tools.os_info.with_apt:
                installer = tools.SystemPackageTool()
                if self.settings.arch == "x86" and tools.detected_architecture() == "x86_64":
                    installer.install("gcc-multilib")
                    installer.install("libglu1-mesa-dev:i386")
                    installer.install("libxi-dev:i386")
                else:
                    installer.install("libglu1-mesa-dev")
                    installer.install("libxi-dev")
            elif tools.os_info.with_yum:
                installer = tools.SystemPackageTool()
                if self.settings.arch == "x86" and tools.detected_architecture() == "x86_64":
                    installer.install("libGLU-devel.i686")
                    installer.install("libXi-devel.i686")
                else:
                    installer.install("libGLU-devel")
                    installer.install("libXi-devel")
            else:
                self.output.warn("Could not determine Linux package manager, skipping system requirements installation.")

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def source(self):
        zip_name = "freeglut-%s" % (self.version)
        zip_ext = ".tar.gz"
        tools.download("https://sourceforge.net/projects/freeglut/files/freeglut/%s/%s.tar.gz/download" % (self.version, zip_name), zip_name + zip_ext)
        tools.unzip(zip_name + zip_ext)
        os.unlink(zip_name + zip_ext)
        os.rename(zip_name, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["FREEGLUT_BUILD_DEMOS"] = False
        if self.options.shared:
            cmake.definitions["FREEGLUT_BUILD_SHARED_LIBS"] = True
            cmake.definitions["FREEGLUT_BUILD_STATIC_LIBS"] = False
        else:
            cmake.definitions["FREEGLUT_BUILD_SHARED_LIBS"] = False
            cmake.definitions["FREEGLUT_BUILD_STATIC_LIBS"] = True
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.os == "Windows":
            self.cpp_info.defines = ["FREEGLUT_LIB_PRAGMAS=0"]
            self.cpp_info.libs.append("glu32")
            self.cpp_info.libs.append("opengl32")
            self.cpp_info.libs.append("gdi32")
            self.cpp_info.libs.append("winmm")
            self.cpp_info.libs.append("user32")
            if not self.options.shared:
                self.cpp_info.libs[0] += "_static"
            if self.settings.build_type == "Debug":
                self.cpp_info.libs[0] += "d"
