import os
def execute_expect():
    print os.getcwd()
    program_path=os.getcwd()
    os.system(os.getcwd()+'/config/execute_expect.sh')