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

# Technologies
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

# Considerations & Recommendation
Using django-eventstream

# Credits
https://www.flaticon.com/free-icon/build_8297314