import sys
import logging

import paramiko
from ftplib import FTP

class FileTransferCx:

	def __init__(self, protocol, host, user, password=None):
		self._proto = protocol
		self._host = host
		self._user = user
		self._pass = password

	def __initialize_cx(self):
		
