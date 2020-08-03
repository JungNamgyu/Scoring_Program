import os
import subprocess

def execute(cmd, testcase):

    print("testcase " + testcase + "\n")
    
    fd = subprocess.Popen(cmd, shell=True,
                          stdin = subprocess.PIPE,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE)
    
    result = fd.communicate(testcase.encode())[0].decode()

    return fd.stderr, result
        
def compile(cmd):
    
    fd = subprocess.Popen(cmd, shell=True,
                          stdin = subprocess.PIPE,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE)
    
    fd.communicate()
    
    return fd.stdout, fd.stderr

##################################################################
    
path = "C:/Users/Namgyu/Desktop/Data/Projects/Scoring_Program"
problem_num = '1'

for root, dirs, files in os.walk(path):
    
    rootpath = os.path.join(os.path.abspath(path), root)
    
    for file in files:
    
        try:
            
            filepath = os.path.join(rootpath, file)
            fname, ext = os.path.splitext(filepath)
            
            if(ext==".c"):
                cmd = "gcc -std=c++11 -o test " + path + "/" + file
                
            elif(ext==".cpp"):
                cmd = "g++ -std=c++11 -o test " + path + "/" + file

            else:
                continue

            compile(cmd)

            input_file = open(path + "/" + problem_num + "/input.txt", "r")
            output_file = open(path + "/" + problem_num + "/output.txt", "r")

            input_case = ""
            for line in input_file.readlines():
                input_case = input_case + line

            output_case = ""
            for line in output_file.readlines():
                output_case = output_case + line

            stderr, result = execute(fname, input_case)
            
            print("output : " + output_case)
            print("result : " + result)

            if(output_case == result):
                print("성공")
            
        except RuntimeError:
            print("RunTime Error")
        except TypeError:
            print("Type Error")
        except ValueError:
            print("Value Error")
