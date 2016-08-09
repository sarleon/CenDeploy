import os
from config.execute_expect import execute_expect
from config.generate_expect_file import generate_expect

def run():
    print "****************************************************"
    print "welcome to CenDeploy moniter"
    print "CenDeploy, a light distribution tool "
    print "Version: 0.1 unstable"

if(__name__=='__main__'):
    run()
    user='root'
    server='121.42.160.10'
    password='charfield123+1s'
    local_dir='/home/sarleon/daily/scptest/'
    server_dir='/root/'
    generate_expect(user,server,password,local_dir,server_dir)
    execute_expect()

