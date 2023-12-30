cmake_minimum_required(VERSION 3.18)
project(Final_SystemC CXX)

#to find Torch and fetch
find_package(SystemCLanguage CONFIG REQUIRED)
find_package(Torch REQUIRED)
find_package(OpenCV REQUIRED)




include_directories( ${OpenCV_INCLUDE_DIRS} ${Torch_INCLUDE_DIRS} ${SystemCLanguage_INCLUDE_DIRS} )


# Add your source files
add_executable(Final_SystemC 
	Final_SystemC.cpp 
	Initiator.cpp
     InitiatorThread.cpp
)

set (CMAKE_CXX_STANDARD 17 ${SystemC_CXX_STANDARD} CACHE STRING
     "C++ standard to build all targets. Supported values are 98, 11, 14, and 17.")
set (CMAKE_CXX_STANDARD_REQUIRED ${SystemC_CXX_STANDARD_REQUIRED} CACHE BOOL
     "The with CMAKE_CXX_STANDARD selected C++ standard is a requirement.")

target_link_libraries(Final_SystemC 
PUBLIC ${OpenCV_LIBS} 
PUBLIC "${TORCH_LIBRARIES}" 
${SystemC_LIBRARIES}
PRIVATE SystemC::systemc

)





if (MSVC)
  file(GLOB TORCH_DLLS "${TORCH_INSTALL_PREFIX}/lib/*.dll")
  add_custom_command(TARGET Final_SystemC
                     POST_BUILD
                     COMMAND ${CMAKE_COMMAND} -E copy_if_different
                     ${TORCH_DLLS}
                     $<TARGET_FILE_DIR:Final_SystemC>)
endif (MSVC)
