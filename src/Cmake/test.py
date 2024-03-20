import subprocess


def main():
    # subprocess.run(["cmake","-S",r"E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/examples/SystemC_Ctorch","-B",r"E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/examples/SystemC_Ctorch/build2"])
    subprocess.run(["cmake","--build",r"E:\Github\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\examples\SystemC_Ctorch\build2","--clean-first"])
    t=subprocess.run(["Final_SystemC.exe"],shell=True,cwd=r"E:\Github\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\examples\SystemC_Ctorch\build2\Debug\ ")
    print("ahmed")
    print(t)
    # subprocess.run("Final_SystemC.exe")

main()
# print("\n ahmed")
# print(r"\n ahmed")
