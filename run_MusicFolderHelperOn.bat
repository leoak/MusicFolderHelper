@echo off

set INSTALL_DIR=Z:\MusicFolderHelper

echo Parent Directory: "%~1"

set hasSubdirectories=0

for /D %%D in ("%~1\*") do (
  if exist "%%~D" (
    set hasSubdirectories=1
    py "%INSTALL_DIR%\main.py" "%%~D"
    ) else (
    echo Directory does not exist: "%%~D"
  )
)

if %hasSubdirectories%==0 (
  py "%INSTALL_DIR%\main.py" "%~1"
)
