# Notes on Maya API 01
* Date: 2020/8/1

**Making Maya `.mll` plug-ins**
By folowing the turial [here at CG Circuit](https://www.cgcircuit.com/tutorial/introduction-to-the-maya-api)

|Tasks:|
|---|
|* Using Visual Studio |
|* Using Cmake |


**For building Maya plug-in on windows using CMake**
* using cmake: the command line should be something like this, which works on my machine:

|`cmake -G "Visual Studio 16 2019" ../src` | `(cmakelist is under the same directory with source files)` |
|:---|---|
|if want to build a different version of Maya plug-in, the cmd lines should be like this, adding an extra flag `-D` to override the maya versions: | |
| **`cmake -G "Visual Studio 16 2019" -D MAYA_VERSION:string=2018 ../src`**| |
