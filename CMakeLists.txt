cmake_minimum_required(VERSION 3.27)

project(hdlc
  VERSION 1.0.2
  LANGUAGES CXX
  )

set(LIBRARY_OUTPUT_PATH "${CMAKE_BINARY_DIR}/lib")
set(EXECUTABLE_OUTPUT_PATH "${CMAKE_BINARY_DIR}/bin")
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if (MSVC)
    #add_compile_options(/W1)
else()
    #add_compile_options(-Wall -Wextra -Werror $<$<CONFIG:RELEASE>:-O3>)
endif()

if (NOT CMAKE_BUILD_TYPE)
    message(STATUS "No build type selected, defaulting to Debug")
    set(CMAKE_BUILD_TYPE "Debug")
endif()
 
find_package(spdlog)
find_package(fmt)
find_package(Boost)
 
add_subdirectory(${PROJECT_NAME})
add_subdirectory(vendor/serial)   #serial lib required for the example code.
add_subdirectory(example)



message("BUILD_TESTING=${BUILD_TESTING}")
if (NOT BUILD_TESTING STREQUAL OFF)
    enable_testing()
    find_package(Catch2)
    
    add_subdirectory(test)
endif()