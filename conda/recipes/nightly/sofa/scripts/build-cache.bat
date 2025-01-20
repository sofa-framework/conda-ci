setlocal EnableDelayedExpansion
@echo on

rmdir /S /Q build

mkdir build
cd build

:: Configure
cmake %CMAKE_ARGS% ^
  -B . ^
  -S %SRC_DIR% ^
  -G Ninja ^
  -DCMAKE_BUILD_TYPE:STRING=MinSizeRel ^
  -DSOFA_USE_DEPENDENCY_PACK=OFF ^
  -DSOFA_ENABLE_LEGACY_HEADERS:BOOL=OFF ^
  -DAPPLICATION_SOFAPHYSICSAPI=OFF ^
  -DSOFA_BUILD_SCENECREATOR=OFF ^
  -DSOFA_BUILD_TESTS=OFF ^
  -DSOFA_FLOATING_POINT_TYPE=double ^
  -DPLUGIN_CIMGPLUGIN=OFF ^
  -DPLUGIN_SOFAMATRIX=OFF ^
  -DPLUGIN_SOFAVALIDATION=OFF ^
  -DPLUGIN_SOFA_GUI_QT=OFF ^
  -DSOFA_NO_OPENGL=ON ^
  -DSOFA_WITH_OPENGL=OFF ^
  -DPLUGIN_MULTITHREADING=ON ^
  -DAPPLICATION_RUNSOFA=OFF ^
  -DPLUGIN_ARTICULATEDSYSTEMPLUGIN=OFF ^
  -DSOFA_ALLOW_FETCH_DEPENDENCIES=OFF
if errorlevel 1 exit 1

:: Build.
cmake --build . --parallel "%CPU_COUNT%"
if errorlevel 1 exit 1

:: Install.
cmake --build . --parallel "%CPU_COUNT%" --target install
if errorlevel 1 exit 1

:: For Windows build, as we don't have rpath like in Unix systems to store
:: paths to internal Sofa plugins dynamic libraries and as each plugin is stored
:: into a separated folder, we have to copy all plugins libaries into the main
:: Sofa binary folder. This should change in Sofa in future releases and will enable
:: to avoid this.
:: for /D %%f in ("%LIBRARY_PREFIX%\plugins\*") do copy "%%f\bin\*.dll" "%LIBRARY_BIN%"
for /D %%f in ("%LIBRARY_PREFIX%\plugins\*") do echo "%%f"
for /D %%f in ("%LIBRARY_PREFIX%\plugins\*") do copy "%%f\bin\*.dll" "%LIBRARY_BIN%"

@echo off
