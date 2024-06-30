# Graduation Project Siemens

Hello World this is our project of Siemens System Level Modelling of ASDLA Graduation Project
## Setup
### GitHub Setup
1. Download git from the following link: [Git Download Page](https://git-scm.com/downloads)
2. Open the environment variables and add the path **"C:/Program Files/Git/cmd"** to the user or system paths
3. Select your desired directory and open a terminal
4. Clone the project repository using the following command:
```bash
git clone https://github.com/mourra950/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project
```


### Python Setup
1. Download and install python from the following link: [Python Download Page](https://www.python.org/downloads/) **Note that** the code has been tested on Python versions 3.9, 3.10, 3.11
2. Check if Python is installed correctly by opening any terminal and type the following command:
    ```bash
    python --version
    #If the python version is displayed, then it has been installed correctly.
    #If the python is not recognized as an internal or external command, then it has not been installed correctly.
    ```
4. Open the folder containing the project and open a terminal
5. Install the Python dependencies using the following command:
```bash
pip install -r requirements.txt
```
### Torch C++ Setup
1. Download Libtorch debug version 2.2.2 with dependencies from the following link: [LibTorch](https://dev-discuss.pytorch.org/t/pytorch-release-2-2-2-final-rc-is-available/1957)
2. Unzip the downloaded zip file in the desired directory
3. Add the path to the Libtorch folder (e.g.**"D:/Downloads/libtorch"**) in the environment variables
### CMake Setup
1. Download CMake as .zip file or .msi file from [CMake Download Page](https://cmake.org/download/)
2. Unzip the .zip file in the desired directory
3. Double click on the .msi file and proceed with the CMake installation steps
4. Add the path to the CMake bin folder (e.g. **"D:/Downloads/cmake-3.29.2-windows-x86\_64/bin"**) in the user or system environment variables
5. Check if CMake is installed correctly by opening any terminal and type the following command:
    ```bash
    cmake --version
    ```
6.If the CMake version is displayed, then it has been installed correctly. If the cmake is not recognized as an internal or external command, then it has not been installed correctly.


### SystemC Setup
1. Download SystemC as .zip file from the following link:\\ \href{https://accellera.org/downloads/standards/systemc}{https://accellera.org/downloads/standards/systemc}
2. Unzip the SystemC .zip file in the desired directory
3. Add the path to the SystemC folder (e.g.\textbf{"D:/Downloads/systemc-3.0.0"}) in the user or system environment variables
4. Go to the SystemC folder and open a terminal
5. Enter the following commands to the terminal one by one to compile and install SystemC libraries:
    ```bash
    mkdir build
    cmake -B ./build/
    cmake --build ./build/
    ```

### OpenCV C++ Setup
1. Download OpenCV installer from the following link: [OpenCV Download]{https://opencv.org/releases/}
2. Double click on the installer and proceed with the installation steps
3. Add the paths of OpenCV bin folder (e.g. **"D:/Downloads/opencv/build/x64/vc16/bin"**) and lib folder (e.g. **"D:/Downloads/opencv/build/x64/vc16/lib"**) in the user or system environment variables

### Tool Usage
For a comprehensive and professional overview of how to effectively utilize the tool after completing the library setups, please watch the following video tutorial:
[Tool Usage Video Tutorial]{https://youtu.be/3cBZC2BTHNY}.
