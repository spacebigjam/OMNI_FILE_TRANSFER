import sys
import logging

import paramiko
from ftplib import FTP

class FileTransfer:

	SUPPORTED_PROTOCOLS = ["SFTP", "FTP"]

	def __init__(self, protocol, host, user, password=None, timeout=60):
		self._proto = protocol
		self._host = host
		self._user = user
		self._pass = password
		self._tout = timeout

		remote_hdlr = self.__initialize_cx()
		if(remote_hdlr is not None):
			self.remote_cx = __open_cx(remote_hdlr)
		else:
			self.remote_cx = None

	def __initialize_cx(self):
		if upper(self.__proto) == "SFTP":
			try:
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				return ssh
			except:
				return None
		elif upper(self.__proto) == "FTP":
			return None
		else:
			return None

	def __open_cx(self, ssh_obj):
		ssh_obj.connect(host, username=self._user, password=self._pass, timeout=self._tout)
		return ssh_obj.open_sftp()

	def __close_cx(self):
		self.remote_cx.close()

	def get_file(self, ori_file, ori_dir, dest_file=None, dest_dir):
		