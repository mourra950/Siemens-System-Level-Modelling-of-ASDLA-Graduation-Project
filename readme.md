# Graduation Project Siemens

Hello World this is our project of Siemens System Level Modelling of ASDLA Graduation Project
## Setup
### GitHub Setup
1. Download git from the following link: \href{https://git-scm.com/downloads}{https://git-scm.com/downloads}
2. Open the environment variables and add the path \textbf{"C:/Program Files/Git/cmd"} to the user or system paths
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

\subsection{Torch C++ Setup}
\begin{enumerate}
    \item Download Libtorch debug version 2.2.2 with dependencies from the following link: \href{https://dev-discuss.pytorch.org/t/pytorch-release-2-2-2-final-rc-is-available/1957}{https://dev-discuss.pytorch.org/t/pytorch-release-2-2-2-final-rc-is-available/1957}

    \item Unzip the downloaded zip file in the desired directory

    \item Add the path to the Libtorch folder (e.g.\textbf{"D:/Downloads/libtorch"}) in the environment variables
\end{enumerate}


\subsection{CMake Setup}

\begin{enumerate}
    \item Download CMake as .zip file or .msi file from the following directory:
    \href{https://cmake.org/download/}{https://cmake.org/download/}

    \item Unzip the .zip file in the desired directory
    \newline \underline{OR} \newline
    Double click on the .msi file and proceed with the CMake installation steps

    \item Add the path to the CMake bin folder (e.g.\textbf{"D:/Downloads/cmake-3.29.2-windows-x86\_64/bin"}) in the user or system environment variables

    \item Check if CMake is installed correctly by opening any terminal and type the following command:
    \newline
    \textbf{\emph{[cmake \space\space- -version]}}
    \newline
    If the CMake version is displayed, then it has been installed correctly. If the cmake is not recognized as an internal or external command, then it has not been installed correctly.
\end{enumerate}


\subsection{SystemC Setup}
\begin{enumerate}
    \item Download SystemC as .zip file from the following link:\\ \href{https://accellera.org/downloads/standards/systemc}{https://accellera.org/downloads/standards/systemc}

    \item Unzip the SystemC .zip file in the desired directory

    \item Add the path to the SystemC folder (e.g.\textbf{"D:/Downloads/systemc-3.0.0"}) in the user or system environment variables

    \item Go to the SystemC folder and open a terminal

    \item Enter the following commands to the terminal one by one to compile and install SystemC libraries:
    \newline
    \textbf{\emph{[mkdir build]}}
    \newline
    \textbf{\emph{[cmake -B ./build/]}}
    \newline
    \textbf{\emph{[cmake --build ./build/]}}
\end{enumerate}


\subsection{OpenCV C++ Setup}
\begin{enumerate}
    \item Download OpenCV installer from the following link: \href{https://opencv.org/releases/}{OpenCV Download}

    \item Double click on the installer and proceed with the installation steps

    \item Add the paths of OpenCV bin folder (e.g.\textbf{"D:/Downloads/opencv/build/x64/vc16/bin"}) and lib folder (e.g.\textbf{"D:/Downloads/opencv/build/x64/vc16/lib"}) in the user or system environment variables
\end{enumerate}

\section{Tool Usage}
% For a comprehensive guide on utilizing the tool effectively after completing the library setup, please refer to the following professional video tutorial: \href{https://youtu.be/PsmQhhjzPxc}{Tool Usage Video Tutorial}.
For a comprehensive and professional overview of how to effectively utilize the tool after completing the library setups, please watch the following video tutorial:\newline \href{https://youtu.be/3cBZC2BTHNY}{Tool Usage Video Tutorial}.
