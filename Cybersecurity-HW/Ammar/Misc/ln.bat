@echo off
setlocal
set "FILE_TO_PROCESS=%~f1"
set /a LINE_NUMBER=%~2
set /a trim=LINE_NUMBER-1

break>"%temp%\empty"&&fc "%temp%\empty" "%FILE_TO_PROCESS%" /lb  %LINE_NUMBER% /t |more +4 | findstr /B /E /V "*****"|more +%trim%
endlocal
