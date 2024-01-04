poetry run python manage.py collectstatic --noinput

rmdir /s /q build
rmdir /s /q dist

@REM ? <<<<<<<<>>>>>>>>>>
@REM OPTION 1 - hardcoding location of daphne
pyinstaller myscript.py --distpath dist\windows --name njogush --icon build.png
@REM ! Stopped the embedding of daphne (see myscript.py)
@REM copy venv\njogush-JHqgHMML-py3.8\Scripts\daphne.exe dist\windows\njogush
@REM ! <<<<<<<<>>>>>>>>>>
@REM copy dist\windows\njogush\daphne\management\commands\runserver.py dist\windows\njogush\django\core\management\commands\runserver.py

@REM ? <<<<<<<<>>>>>>>>>>
@REM ! SUSPENDED - Not working as expected 2023.01.01
@REM ! Not needed anymore since daphne is nolonger being embeded (see myscript.py) 2023.01.02
@REM OPTION 2 - dynamically locating daphne
@REM https://stackoverflow.com/questions/9143628/bat-function-to-find-a-file-in-folder-and-subfolders-and-do-something-with-it/9144149#9144149 [for /R %f in (daphne.exe) do @echo "%f"]
@REM https://ss64.com/nt/for.html [FOR /R [[drive:]path] %%parameter IN (set) DO command]
@REM https://stackoverflow.com/questions/4419868/what-is-the-current-directory-in-a-batch-file [%cd%]
@REM https://stackoverflow.com/questions/13876771/find-file-and-return-full-path-using-a-batch-file/13876918#13876918
@REM for /r "%cd%\venv\njogush-*" %%a in ("Scripts\daphne.exe") do if "%%~nxa"=="daphne.exe" set p=%%~dpnxa
@REM if defined p (
@REM echo %p%
@REM ) else (
@REM echo File not found
@REM )
@REM pyinstaller myscript.py --add-binary "%p%";. --distpath dist\windows --name njogush --icon build.png
@REM copy "%p%" dist\windows\njogush
@REM ! <<<<<<<<>>>>>>>>>>

@REM All these actions should probably be included in a PyInstaller hook
@REM they have been however been included only because the steps are more obvious here
@REM and do not require the developer to have a deeper understaning into the
@REM workings of PyInstaller
@REM The advantage of using hooks is that files are embedded and this becomes a useful
@REM feature especially when --onefile switch is used
xcopy static dist\windows\njogush\static /s /e /h
copy build.png dist\windows\njogush
@REM TODO https://stackoverflow.com/questions/947954/how-to-have-the-cp-command-create-any-necessary-folders-for-copying-a-file-to-a/14085147#14085147
mkdir dist\windows\njogush\build_tool\templates\build_tool_vue
xcopy build_tool\templates\build_tool_vue\dist dist\windows\njogush\build_tool\templates\build_tool_vue\dist /s /e /h


@REM MORE REFERENCES
@REM https://stackoverflow.com/questions/25794369/batch-file-wildcard-in-folderpath-no-idea-what-the-wildcard-can-be/25794897#25794897
@REM https://stackoverflow.com/questions/7005951/batch-file-find-if-substring-is-in-string-not-in-a-file
@REM https://stackoverflow.com/questions/18668947/how-do-i-set-sys-argv-so-i-can-unit-test-it
@REM https://stackoverflow.com/questions/77123444/create-an-exe-file-from-a-django-project-with-pyinstaller
@REM https://github.com/pyinstaller/pyinstaller/issues/2332
@REM https://superuser.com/questions/206036/commmand-line-command-to-copy-entire-directory-including-directory-folder-to-a/206038#206038
@REM https://stackoverflow.com/questions/97875/rm-rf-equivalent-for-windows