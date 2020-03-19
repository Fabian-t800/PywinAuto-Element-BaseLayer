import os
import subprocess
import glob


command = "C:\\Users\\fabian.tolgyi\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\robot.exe" \
          " -A argfile_pywinauto.txt D:\\QA_Automation_Benchmark_PywinAuto\\rf_pywinauto_tests\\Calculator_tests_pywin.robot"


def rerun_robot(number_of_reruns):
    for i in range(0, number_of_reruns):
        print(f"This is the {i+1} run.")
        subprocess.run(command, cwd="D:\\QA_Automation_Benchmark_Pywinauto\\")


def run_rebot(reports_dir):
    comp_file = open(f"compile_file.txt", "w+")
    os.chdir(reports_dir)
    for file in glob.glob("*.xml"):
        comp_file.write(file + "\n")
    pth = "D:\\QA_Automation_Benchmark_Appium\\reports_alpha_01\\compile_file.txt"
    command = f"C:\\Users\\fabian.tolgyi\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\rebot.exe  -A {pth}"
    subprocess.run(command, cwd="D:\\QA_Automation_Benchmark_Pywinauto\\")




rerun_robot(50)
# run_rebot("D:\\QA_Automation_Benchmark_Appium\\reports_alpha_01")