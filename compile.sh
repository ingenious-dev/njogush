poetry run python manage.py collectstatic --noinput

rm -rf build
rm -rf dist

# ? <<<<<<<<>>>>>>>>>>
# cp venv/njogush-JHqgHMML-py3.8/Lib/site-packages/daphne/management/commands/runserver.py 
# OPTION 1 - hardcoding location of daphne
pyinstaller myscript.py --distpath dist/linux --name njogush --icon build.png
# ! Stopped the embedding of daphne (see myscript.py)
# cp venv/njogush-JHqgHMML-py3.8/Scripts/daphne.exe dist/linux/njogush
# ! <<<<<<<<>>>>>>>>>>
# cp dist/linux/njogush/daphne/management/commands/runserver.py dist/linux/njogush/django/core/management/commands/runserver.py

# All these actions should probably be included in a PyInstaller hook
# they have been however been included only because the steps are more obvious here
# and do not require the developer to have a deeper understaning into the
# workings of PyInstaller
# The advantage of using hooks is that files are embedded and this becomes a useful
# feature especially when --onefile switch is used
cp -r static dist/linux/njogush
cp build.png dist/linux/njogush
# TODO https://stackoverflow.com/questions/947954/how-to-have-the-cp-command-create-any-necessary-folders-for-copying-a-file-to-a/14085147#14085147
mkdir dist/linux/njogush/build_tool/templates/build_tool_vue
cp -r build_tool/templates/build_tool_vue/dist dist/linux/njogush/build_tool/templates/build_tool_vue/dist



# MORE REFERENCES
# https://stackoverflow.com/questions/25794369/batch-file-wildcard-in-folderpath-no-idea-what-the-wildcard-can-be/25794897#25794897
# https://stackoverflow.com/questions/7005951/batch-file-find-if-substring-is-in-string-not-in-a-file
# https://stackoverflow.com/questions/18668947/how-do-i-set-sys-argv-so-i-can-unit-test-it
# https://stackoverflow.com/questions/77123444/create-an-exe-file-from-a-django-project-with-pyinstaller
# https://github.com/pyinstaller/pyinstaller/issues/2332