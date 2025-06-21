from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.build import check_min_cppstd
from conan.tools.system.package_manager import Apt, Apk, Brew, Dnf


class HDLC(ConanFile):
    name = "hdlc framing"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    options = {
        "debug_modem": [True, False],
    }
    default_options = {
        "debug_modem": True,
        # "libcurl/*:shared": True,
        #"cpp-httplib/*:with_zlib": False, # ?
    }

    def requirements(self):
        self.requires("fmt/11.2.0") # was: fmt/5.2.1, latest: fmt/11.2.0, oldest: 7.1.3
        self.requires("spdlog/1.15.3") # was: spdlog/1.2.1, latest: spdlog/1.15.3, oldest: 1.8.5
        self.requires("catch2/3.8.1") # was: catch2/2.4.1, latest catch2/3.8.1, oldest: catch2/2.11.3
        self.requires("boost/1.88.0") # was: boost/1.68.0, latest: boost/1.88.0, oldest: boost/1.78.0

    def configure(self):
        check_min_cppstd(self, 11)

    def build_requirements(self):
        self.build_requires("cmake/[>=3.31.1 <5]")
        self.build_requires("ninja/[>=1.12.1 <2]")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["NATF_MDM_DEBUG"] = self.options.debug_modem
        # if self.options.debug_modem:
        #     tc.preprocessor_definitions["MDM_DEBUG"] = 1
        #
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        #{"LEVELMETER_PLATFORM": "linux", "LEVELMETER_APP": "nana-testing"})
        cmake.build()
        if not self.conf.get("tools.build:skip_test", default=False):
            self.run("tests/unit_tests")