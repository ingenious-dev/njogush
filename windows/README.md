```
CAUTION:    
As of 2024.05.29 the solution proposed here are yet to be tested successfully. It has however been left here for reference and troubleshooting purposes. If you are successful please consider sharing feedback through `ingeniousdevke@gmail.com`.
```

# SC & “true” Windows Service Application

Using `sc.exe create njogush start=auto binPath="[PATH_TO_NJOGUSH_CODE]\daphne.bat"` presents the following issues:

- The service cannot be controlled from the Windows services list
![alt text](./screenshots/Screenshot%202024-05-29%20024506.png)
![alt text](./screenshots/Screenshot%202024-05-29%20024538.png)

- Despite not being able to control the service as stated above, It seems to run when tested from the browser on `http://127.0.0.1:6564`. While this is commendable it immediately prevents the issue of how to stop or restart the service when needed since as already indicated it cannot be controlled from the relevant interfaces. You would have to restart the computer.

## Solution
A solution for this is proposed here: https://www.coretechnologies.com/blog/windows-services/sc-service-fails-to-start/. See the section `Use a “Service Wrapper” to install a regular program as a Windows Service`

### Steps
1. At an MS-DOS command prompt(running CMD.EXE), type the following command:

    ```[PATH_TO_NJOGUSH_CODE]\windows\instsrv.exe njogush [PATH_TO_NJOGUSH_CODE]\windows\srvany.exe```

    For example:    
    `C:\moko\njogush\windows\instsrv.exe njogush C:\moko\njogush\windows\srvany.exe`

2. Run Registry Editor (Regedt32.exe) and locate the following subkey:

    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\njogush

3. From the **Edit** menu, select **Add Key**. Type the following entries, and select **OK**:

- Key Name: Parameters
- Class: \<leave blank>

4. Select the **Parameters** key.

5. From the **Edit** menu, select **Add Value**. Type the following entries, and select **OK**:

- Value Name: **Application**
- Data Type: REG_SZ
- String: [PATH_TO_NJOGUSH_CODE]\daphne.bat     
where [PATH_TO_NJOGUSH_CODE]\daphne.bat is the drive and full path to the application executable including the extension (for example, C:\WinNT\Notepad.exe)

6. Close Registry Editor.
![alt text](./screenshots/Screenshot%202024-05-29%20031342.png)
![alt text](./screenshots/Screenshot%202024-05-29%20034857.png)

## More links
What is Srvany?     
https://www.coretechnologies.com/WindowsServices/FAQ.html#WhatIsSrvany

Download instsrv.exe & srvany.exe   
https://www.verydoc.com/others/service_under_nt.htm

Using instsrv.exe & srvany.exe  
https://learn.microsoft.com/en-US/troubleshoot/windows-client/setup-upgrade-and-drivers/create-user-defined-service

Alternative source of srvany    
https://github.com/birkett/srvany-ng

How to access Windows Services  
https://kb.blackbaud.com/knowledgebase/articles/Article/49839

Fix `g:\ntrk\source\instsrv\instsrv.c: Error 1072 from CreateService on line 138`       
https://gateway.sdl.com/apex/communityknowledge?articleName=000011970

