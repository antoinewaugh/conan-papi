from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class PapiConan(ConanFile):
    name = "Papi"
    version = "5.7.0"
    license = "MIT"
    url = "https://github.com/antoinewaugh/conan-papi"
    description = "The Performance Application Programming Interface (PAPI) provides tool designers and application engineers with a consistent interface and methodology for the use of low-level performance counter hardware"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"

    def source(self):
        self.run("git clone https://bitbucket.org/icl/papi.git")

    def build(self):
        os.chdir("papi/src")
        autotools = AutoToolsBuildEnvironment(self)
        if self.options.shared:
            autotools.configure(args=["--with-shared-lib=yes"])
        else:
            autotools.configure(args=["--with-shared-lib=no"])
        autotools.make()

    def package(self):
        self.copy("*.h", dst="include", src="papi/src")
        if self.options.shared:
            self.copy("*.so", dst="lib", src="papi/src", keep_path=False)
        else:
            self.copy("*.a", dst="lib", src="papi/src", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["papi"]
