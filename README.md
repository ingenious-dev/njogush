# njugush

_Powered by https://ingenious.or.ke_ [![N|Solid](https://ingenious.or.ke/static//img/ingenious%20logo%20-%20cropped.png)](https://ingenious.or.ke/) 

[![Build Status](https://img.shields.io/badge/build-passing-green)](https://github.com/ingenious-dev/njogush)

# Running the application
## Windows:    
INSTALLATION    
Start the setup on `Output\NjogushSetup.exe`    
Launch `Njogush DX Build Tool`  
Open the browser and visit the url [`http:127.0.0.1:6564`](http:127.0.0.1:6564/install)

NO INSTALLATION     
Start the executable on `dist\windows\njogush\njogush.exe`  
Open the browser and visit the url [`http:127.0.0.1:6564`](http:127.0.0.1:6564/install)

## Linux:  
Run `./dist/linux/njogush/njogush`  
Open the browser and visit the url [`http:127.0.0.1:6564`](http:127.0.0.1:6564/install)

# Optional Features
## Forgot Password
Copy `.env.exammple` and rename it to `.env`.   
Replace the dummy email settings with working alternative.  
If the settings provided are correct the forgot password feature should now be working.

## Systemd service
You can run njogush as a service and enable it to start at reboot. Here is how to do it with `systemd`

```sh
cp daphne_njogush.service /etc/systemd/system
sudo systemctl start daphne_njogush.service
sudo systemctl enable daphne_njogush.service
```

# Development setup
To setup a dev environment for coding, clone the repository and then run `make dev-setup` to setup a virtual environment with the needed dependencies.

Now you can run the program either using:

```
poetry run python3 manage.py runserver 0.0.0.0:6564
```

Or by entering the virtualenv and then running the program.
```
poetry shell

python3 manage.py runserver 0.0.0.0:6564
```

# Creating executable
## Windows
```sh
> compile.bat
```

Test Windows Environment
```sh
OS Version:                10.0.22000 N/A Build 22000
OS Build Type:             Multiprocessor Free
```


## Linux
```sh
$ bash compile.sh
```

Test Linux Environment
```sh
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.2 LTS
Release:        22.04
Codename:       jammy
```

# Running njogush as a service
## Windows (from the python code)
See `windows/README.md` for known issues with this method.

Run the following from an elevated command line terminal
```sh
sc.exe create njogush start=auto binPath="[PATH_TO_NJOGUSH_CODE]\daphne.bat"
```

for example
```sh
sc.exe create njogush start=auto binPath="C:\moko\njogush\\daphne.bat"
```
For more on `sc.exe` see `https://learn.microsoft.com/en-US/windows-server/administration/windows-commands/sc-create`

To remove service run
```sh
sc.exe delete njogush
```

## Linux (from the python code)
```sh
cp daphne_njogush.service /etc/systemd/system/
systemctl enable daphne_njogush.service
systemctl restart daphne_njogush.service
```

To remove service run
```sh
systemctl disable daphne_njogush.service
rm  /etc/systemd/system/daphne_njogush.service
```

# Technologies used in njogush
| NAME | DESCRIPTION |
| --- | --- |
| Poetry | Dependency manager |
| Django | Web framework |
| Django Rest Framework | Creating Rest API |
| Python Decouple | Configure using environment variables |
| Corsheader | Handle CORS  |
| PyInstaller | Bundle application  |
| Batch | Creating compile script for windows  |
| Bash | Creating compile script for linux  |
| VueJS | Building the UI/SPA  |

# Warnings
The setting `REMOTE_MODE = False` prevents the build tool from running projects when accessed remotely. Projects can therefore only be run if the build tool is accessed locally (`127.0.0.1` and `localhost`)

This build tool can run arbitrary commands. While this allows the developer greater control which is limited by other build tools, it is the responsibilty of the developer to ascertain the safety of the executed commands.

# Known Issues
## `cd` command
`cd` command will not change the working directory when run directly. To overcome this, create a bash script and place the command with `cd` inside the script then run it.

## nvm limitations
when running njogush as a systemd service the following nodejs/npm related error has been noticed   
`nvm command not found`, `npx command not found`, `nvm is not a direcory`   
These errors are typically experienced when nodejs has been installed through nvm.

The solution is to install a default/system nodejs version using the system package mananger (apt). Njogush will then use this default nodejs version to run your command.

To run your command using nvm versions of nodejs run njogush from a terminal.
The above known issue has only been observed when njogush is run as a service at reboot.

Here is a link that might help with installing a default upto date version of nodejs:
https://joshtronic.com/2023/04/23/how-to-install-nodejs-20-on-ubuntu-2004-lts/

## fvm
```sh
fvm: command not found
```
The solution is to Call fvm from absolute path for example, `/home/linuxbrew/.linuxbrew/bin/fvm flutter build apk`

## detected dubious ownership in repository
On windows, this log is seen when running njogush as an automated service (service that start when windows boots up).
```
C:\njogush>cd /d "C:\my_flutter_project" & git restore "C:\my_flutter_project\android\app\src"  
fatal: detected dubious ownership in repository at 'C:/my_flutter_project'
'C:/my_flutter_project' is owned by:
    DESKTOP-S6LQ7U5/ADMIN (S-1-5-21-3685671753-1490390355-2425391035-1002)
but the current user is:
    NT AUTHORITY/SYSTEM (S-1-5-18)
To add an exception for this directory, call:

    git config --global --add safe.directory C:/my_flutter_project
```

The solution in to set njogush service to autostart with the user account that has the required permissions as shown in the scre
![screen shot of services](./Screenshot%202024-08-19%20210648.png)

# Considerations & Recommendation
Using django-eventstream
Providing a export/import functionality & format e.g JSON

# Credits
https://www.flaticon.com/free-icon/build_8297314

# References
Node Version Manager - https://github.com/nvm-sh/nvm    
Simple Flutter Version Management -  https://fvm.app/   
