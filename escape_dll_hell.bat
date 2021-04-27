
@echo off

pushd "%~dp0"
echo %cd%

rem rd /s /q "Assets\Plugins\LibsSymlinks"
rem mkdir "Assets\Plugins\LibsSymlinks"
rem mkdir "Assets\Plugins\LibsSymlinks\Editor"

rem BODY_START
mklink /d "Assets\Plugins\LibsSymlinks\lib" "..\..\..\lib"

rem BODY_END


echo.&pause&goto:eof

popd