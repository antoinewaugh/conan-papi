from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class PapiConan(ConanFile):
    name = "Papi"
    license = "MIT"
    url = ""
    description = "The Performance Application Programming Interface (PAPI) provides tool designers and application engineers with a consistent interface and methodology for the use of low-level performance counter hardware"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone https://bitbucket.org/icl/papi.git")

    def build(self):
        os.chdir("papi/src")
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure() 
        autotools.make()

    def package(self):
        self.copy("*.h", dst="include", src="papi/src")
        self.copy("*.so", dst="lib", src="papi/src", keep_path=False)
        self.copy("*.a", dst="lib", src="papi/src", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["papi"]