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
                    installer.install("libgl1-mesa-dev:i386")
                    installer.install("libgl1-mesa-glx:i386")
                else:
                    installer.install("libgl1-mesa-dev")
                    installer.install("libgl1-mesa-glx")
            elif tools.os_info.with_yum:
                installer = tools.SystemPackageTool()
                if self.settings.arch == "x86" and tools.detected_architecture() == "x86_64":
                    installer.install("libGL-devel.i686")
                    installer.install("glibmm24.i686")
                    installer.install("glibc-devel.i686")
                else:
                    installer.install("libGL-devel")
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
