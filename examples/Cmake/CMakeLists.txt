cmake_minimum_required(VERSION 3.18)
project(SystemCExample CXX)


# Find the SystemC package
find_package(SystemCLanguage CONFIG REQUIRED)

set (CMAKE_CXX_STANDARD ${SystemC_CXX_STANDARD} CACHE STRING
     "C++ standard to build all targets. Supported values are 98, 11, 14, and 17.")

set (CMAKE_CXX_STANDARD_REQUIRED ${SystemC_CXX_STANDARD_REQUIRED} CACHE BOOL
     "The with CMAKE_CXX_STANDARD selected C++ standard is a requirement.")



# Create an executable for your SystemC project
add_executable(systemc_example main.cpp)

# Link the SystemC library with your project
target_link_libraries(systemc_example SystemC::systemc)