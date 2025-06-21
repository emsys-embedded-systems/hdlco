# The unix example requires a serial library to work.
# find_package(serial 1.0 REQUIRED)


add_executable(example example.cpp )

target_include_directories(example
    PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

target_link_libraries(example
  ${PROJECT_NAME}
  spdlog::spdlog
  boost::boost
  Catch2::Catch2WithMain
  serial
)

set_target_properties(example
  PROPERTIES
    CXX_STANDARD 14
)
