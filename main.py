#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'zmhuang'
# 2018年1月29日15:11:34

import paramiko
import json
import sys
from config import Config
#from config import read_config, write_config
from ssh_host import SSH
from get_rsa_pub import read_file,get_authorized_keys_path,get_write_rsa_command
# from get_rsa_pub import get_write_rsa_command

config_file_path = 'config.ini'
configger = Config(config_file_path)
username = str(configger.get('wei','username'))
password = str(configger.get('wei','password'))
ip = str(configger.get('wei','ip'))
port = str(configger.get('wei','port'))
agent_path = str(configger.get('wei','agent_path'))
agent_name = str(configger.get('wei','agent_name'))
command = str(configger.get('wei','command'))


rsa = str(read_file().ReadFile()[0].strip('\n'))
authorized_keys_path = get_authorized_keys_path(username)
write_rsa_command = get_write_rsa_command(rsa,authorized_keys_path)
# write_rsa_command = get_write_rsa_command(username).write_rsa_command()

ssh = SSH(ip,username,password)

#results = ssh.exec_commands(command)
ssh.exec_commands(write_rsa_command)
#print results
