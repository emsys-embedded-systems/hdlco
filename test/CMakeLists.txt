add_executable(hdlc_test hdlc_test.cpp)
add_test(NAME hdlc_test COMMAND hdlc_test)

target_include_directories(hdlc_test
    PUBLIC
        $<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

target_link_libraries(hdlc_test
  ${PROJECT_NAME}
  spdlog::spdlog
  Catch2::Catch2WithMain
)

set_target_properties(hdlc_test
  PROPERTIES
    CXX_STANDARD 14
)
