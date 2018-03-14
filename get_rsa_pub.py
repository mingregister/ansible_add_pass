#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'zmhuang'
# 2018年1月30日11:34:56

class read_file(object):

    # def __init__(self, filepath):
    def __init__(self,filepath = '/root/.ssh/id_rsa.pub'):
        self.filepath = filepath

    def ReadFile(self):
        with open(self.filepath, 'ro') as (f):
            self.content = f.readlines()
        return self.content

class get_write_rsa_command(read_file):
    '''
    this class can not be used now, a lot of BUG need to be handled.
    '''
    def __init__(self,username,*args, **kwargs):
        #super(get_write_rsa_command, self).__init__()
        self.username = username
        self.keys_path = ''
        # self.content = ''
        self.filepath = self._rsa_path()

    def path_prefix(self):
        if self.username != 'root':
            self.keys_path = '/home/' + self.username + '/.ssh/'
        else:
            self.keys_path = '/root/.ssh/'
        return self.keys_path

    def _rsa_path(self):
        return self.keys_path + 'id_rsa.pub'

    def authorized_keys_path(self):
        self.authorized_keys_path = self.path_prefix(self.username) + 'authorized_keys'
        return self.authorized_keys_path

    def write_rsa_command(self):
        Write_rsa_command = '/usr/bin/echo "' + self.content + '"' + ' >> ' + self.authorized_keys_path
        return Write_rsa_command

def get_authorized_keys_path(username):
    if username != 'root':
        keys_path = '/home/' + username + '/.ssh/' + 'authorized_keys'
    else:
        keys_path = '/root/.ssh/authorized_keys'
    return keys_path

def get_write_rsa_command(content,authorized_keys_path):
    write_rsa_command = '/usr/bin/echo "' + content + '"' + ' >> ' + authorized_keys_path
    return write_rsa_command


if __name__ == '__main__':
    content = read_file().ReadFile()
    # print content[0]


