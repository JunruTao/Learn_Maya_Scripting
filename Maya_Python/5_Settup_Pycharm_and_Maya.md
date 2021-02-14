# Setting up PyCharm for Maya
1. install Pycharm, make sure version as 2.7
2. Open PyCharm go to `configure` &rarr; `settings`
  * `default setting` window &darr;
    * `Project Interpreter` tab &rarr; click '⚙️' icon
      * `C:/Program Files/Autodesk/Maya2019/bin/`&rarr;`mayapy.exe`
    * go back click on '⚙️' icon again &rarr; `more`
      *  `Project Interpreters` window &darr;
        * select `mayapy.exe`'s path then&rarr; click on icon '✏️'to edit panel &darr;
        * Rename it as `Maya 2019 Python` for clearer

3. In oder to have auto complete in Pycharm for maya, you need to download maya's devkit for that version, from Autodesk appstore -> `Maya 2019 Developer Kit`
  * then Extract all the files in the zip file to `C:/Program Files/Autodesk/Maya2019`.
  * go back to pycharm's `Project Interpreters` window, click on '🗒️' list icon, the one below '✏️' &darr;
    * `Interpreter path` editor window, click on '➕' icon, to add a new director: &darr;
      * `C:/Program Files/Autodesk/Maya2019/devkit/other/pymel/extras/completion/py` directory
4. Click okay, okay, apply ...;

5. Open up maya's script folder: `C:/Users/${UserName}/Documents/maya/2019/scripts/`

6. Now basically you can write all your scripts into here


### Update:(2021/2/14)
Setting up the auto complete which was not covered in the tutorial:
https://medium.com/@cerinatahir/pycharm-maya-843bb5e783ef

After adding the path in `Porject Interpreter`, you need to go to the `Project Structure` -> `Add Content Root` ➕ button and select:
```
C:\Program Files\Autodesk\Maya2018\devkit\other\pymel\extras\completion\py
```

Also mark this director as source folder by clicking on `[source]` button on the top