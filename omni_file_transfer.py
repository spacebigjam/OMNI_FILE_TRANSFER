import sys
import logging

import paramiko
#from ftplib import FTP

class FileTransfer:

	SUPPORTED_PROTOCOLS = ["SFTP", "FTP"]

	def __init__(self, protocol, host, user, password=None, timeout=60):
		self._proto	= protocol
		self._host	= host
		self._user	= user
		self._pass	= password
		self._tout	= timeout

		remote_hdlr = self._initialize_cx()
		if(remote_hdlr is not None):
			self.remote_cx = self._open_cx(remote_hdlr)
		else:
			self.remote_cx = None


	def _initialize_cx(self):
		if str.upper(self._proto) == "SFTP":
			try:

				cx = paramiko.Transport((self._host, 22))
				cx.connect(username=self._user, password=self._pass)

				sftp = paramiko.SFTPClient.from_transport(transport)

				#ssh = paramiko.SSHClient()
				#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				return sftp
			except:
				return None
		elif str.upper(self._proto) == "FTP":
			return None
		else:
			return None


	def _open_cx(self, ssh_obj):
		ssh_obj.connect(self._host, username=self._user, password=self._pass, timeout=self._tout)
		return ssh_obj.open_sftp()


	def _close_cx(self):
		self.remote_cx.close()


	def put(self, ori_file, ori_dir, dest_file=None, dest_dir):
		self.remote_cx.put()

		self._close_cx()

	#def get(self, ori_file, ori_dir, dest_file=None, dest_dir):



if __name__ == "__main__":
	ftp_obj = FileTransfer("SFTP", "192.168.0.200", "jam", "password", 120)
	ftp_obj.put()

