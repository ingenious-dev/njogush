#!/usr/bin/env bash
# <<<<<<<>>>>>>
# OPTION 1 - Not working for systemd
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# ● daphne_inapp.service - Daphne-Inapp Service                                                             =
#      Loaded: loaded (/etc/systemd/system/daphne_inapp.service; disabled; vendor preset: enabled)          =
#      Active: activating (auto-restart) (Result: exit-code) since Sat 2024-04-27 20:43:40 UTC; 725ms ago   =
#     Process: 201267 ExecStart=/bin/bash /var/www/inapp_ecosystem/daphne.bash (code=exited, status=127)    =
#    Main PID: 201267 (code=exited, status=127)                                                             =
#         CPU: 8ms                                                                                          =
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# # https://channels.readthedocs.io/en/stable/deploying.html#run-protocol-servers
# cd /var/www/inapp_ecosystem
# poetry shell
# daphne -p 8007 inapp_ecosystem.asgi:application
# <<<<<<<>>>>>>

# <<<<<<<>>>>>>
# OPTION 2
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR
# ar=($(find $SCRIPT_DIR -executable -type f -name daphne))
# $ar -b 0.0.0.0 -p 6564 njogush.asgi:application
# ar=($(find $SCRIPT_DIR/venv -name python)) # Error: /home/[user]/njogush/venv/njogush-GPBWZ7bx-py3.8/lib/python3.8/site-packages/twisted/python: Is a directory
ar=($(find $SCRIPT_DIR/venv -name python3))
$ar manage.py runserver 0.0.0.0:6564
# + https://stackoverflow.com/questions/59895/how-do-i-get-the-directory-where-a-bash-script-is-located-from-within-the-script
# + https://www.baeldung.com/linux/get-absolute-path#using-the-find-command
# + https://unix.stackexchange.com/questions/479349/find-files-in-specific-directories/735707#735707
# + https://superuser.com/questions/38981/how-can-i-find-only-the-executable-files-under-a-certain-directory-in-linux

# + https://stackoverflow.com/questions/2087001/how-can-i-process-the-results-of-find-in-a-bash-script/5285406#5285406
# + https://stackoverflow.com/questions/6594085/remove-first-character-of-a-string-in-bash/46699430#46699430
# + https://www.linode.com/docs/guides/start-service-at-boot/
# + https://unix.stackexchange.com/questions/422213/how-to-see-the-latest-x-lines-from-systemctl-service-log
# + https://superuser.com/questions/1602999/ubuntu-systemctl-service-fails-with-main-process-exited-code-exited-status-1
# <<<<<<<>>>>>>