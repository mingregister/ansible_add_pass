
import paramiko, json, sys, logging
default_log_handler = logging.StreamHandler(sys.stdout)
__logger = logging.getLogger('ssh_host')
__logger.addHandler(default_log_handler)
__logger.log(10, 'Starting logging')

class SSH(object):

    def __init__(self, host, username, password, log_level=logging.INFO):
        self._setuplogging()
        self.set_log_level(log_level)
        self.debug(logging.INFO)
        self.host = host
        self.username = username
        self.password = password
        self.connect = self._connect()

    def _setuplogging(self):
        default_log_handler = logging.StreamHandler(sys.stdout)
        self.logger = logging.getLogger('SSH.%s' % self.__class__.__name__)
        self.logger.addHandler(default_log_handler)

    def set_log_level(self, level):
        self.debug(logging.INFO, 'Set logging level to %d' % level)
        self.logger.setLevel(level)

    def debug(self, level, msg=None):
        strval = str(level) + ': '
        if msg:
            strval = strval + str(msg)
        self.logger.log(level, strval)

    def _connect(self):
        """this is use the paramiko connect the host, return conn"""
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.host, username=self.username, password=self.password, allow_agent=True)
            self.debug(logging.INFO, 'Success to connect host %s !!!' % self.host)
            return ssh
        except:
            self.debug(logging.WARNING, 'Connect to host %s failed!!!' % self.host)
            return

        return

    def exec_commands(self, command):
        """this is use the conn to excute the cmd and return the results of excute the command"""
        stdin, stdout, stderr = self.connect.exec_command(command, timeout=10)
        results_temp = stdout.read().decode('utf-8')
        results = json.dumps(results_temp)
        return results


if __name__ == '__main__':
    ssh = SSH('192.168.253.134', 'mingregester', 'admin123')
    results = ssh.exec_commands('/tmp', '/usr/bin/ls -al')
    print results
