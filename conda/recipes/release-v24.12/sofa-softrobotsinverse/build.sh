#!/bin/sh

set -ex

if [[ $target_platform == osx* ]] ; then
    # Dealing with modern C++ for Darwin in embedded catch library.
    # See https://conda-forge.org/docs/maintainer/knowledge_base.html#newer-c-features-with-old-sdk
    CXXFLAGS="${CXXFLAGS} -D_LIBCPP_DISABLE_AVAILABILITY"
fi

mkdir build
cd build

cmake ${CMAKE_ARGS} \
  -B . \
  -S .. \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DPython_EXECUTABLE:PATH=${PREFIX}/bin/python \
  -DSOFTROBOTSINVERSE_ENABLE_PROXQP:BOOL=ON \
  -DSOFTROBOTSINVERSE_ENABLE_QPOASES:BOOL=OFF \
  -DSOFTROBOTSINVERSE_BUILD_TESTS:BOOL=OFF

# build
cmake --build . --parallel ${CPU_COUNT}

# install
cmake --build . --parallel ${CPU_COUNT} --target install