### Maintainer: flier[@techfak.uni-bielefeld.de] ###
cmake_minimum_required(VERSION 2.8)
PROJECT(pepper_morse_simcontroller)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX and -DMORSE_ROOT, defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

SET(MORSE_ROOT "" CACHE STRING "Please set the $MORSE_ROOT otherwise hard-coded defaults are used.")
IF (NOT MORSE_ROOT)
    SET(MORSE_ROOT "/usr/")
    MESSAGE("-- Setting MORSE_ROOT to: ${MORSE_ROOT}")
ENDIF (NOT MORSE_ROOT)

MESSAGE("-- Your MORSE_ROOT is: ${MORSE_ROOT}")

SET(TARGET_DIR ${PREFIX}/share/pepper_morse/bin)

file(GLOB PY
  "${CMAKE_CURRENT_SOURCE_DIR}/*.py"
)

INSTALL(FILES ${PY} DESTINATION ${TARGET_DIR})