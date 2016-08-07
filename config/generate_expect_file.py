import os





ssh_expect_file_content='''
#! /usr/bin/expect -f
## All possible interactive messages:
# Are you sure you want to continue connecting (yes/no)?
# password:
# Enter passphrase for key
## Main
# Delete self for secret, will not affect the following code
file delete $argv0
# Setup variables
set timeout 10
set user "%s"
set server "%s"
set password "%s"
set port "22"
# set extopt "<<EXTOPT>>"
set ssh_cmd "ssh"
set ssh_opt "$user@$server -p $port"
# set ssh_opt "$ssh_opt $extopt"

# Spawn and expect
eval spawn $ssh_cmd $ssh_opt
if {[string length $password]} {
    expect {
        timeout {send_user "ssh connection time out, please operate manually\n"}
        -nocase "(yes/no)\\?" {send "yes\r"; exp_continue}
        -nocase -re "password:|enter passphrase for key" {
            send "$password\r"
        }
    }
}
interact
''' %('asd','asd','asd')


