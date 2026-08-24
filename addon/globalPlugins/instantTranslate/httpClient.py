# Copyright (C) 2026 Beka Gozalishvili <beqaprogger@gmail.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import json
import socket
import threading
from urllib.parse import urlencode
import urllib.request as urllibRequest

USER_AGENT = "Mozilla/5.0"
DEFAULT_TIMEOUT = 30


class Cancelled(Exception):
	pass


class SessionClosed(Cancelled):
	pass


class RequestAborted(Cancelled):
	pass


def buildUrl(url, params=None):
	if not params:
		return url
	return "%s?%s" % (url, urlencode(params))


class Response:
	def __init__(self, raw, onClose=None):
		self._raw = raw
		self._onClose = onClose
		self._aborted = False

	@property
	def status(self):
		return self._raw.status

	@property
	def headers(self):
		return self._raw.headers

	def read(self):
		try:
			with self:
				return self._raw.read()
		except Exception:
			if self._aborted:
				raise RequestAborted("The request was aborted") from None
			raise

	def text(self, encoding="utf-8"):
		return self.read().decode(encoding)

	def json(self):
		return json.loads(self.text())

	def close(self):
		try:
			self._raw.close()
		finally:
			onClose, self._onClose = self._onClose, None
			if onClose is not None:
				onClose(self)

	def abort(self):
		self._aborted = True
		rawSocket = getattr(getattr(self._raw, "fp", None), "raw", None)
		rawSocket = getattr(rawSocket, "_sock", None)
		if rawSocket is not None:
			try:
				rawSocket.shutdown(socket.SHUT_RDWR)
			except OSError:
				pass
		self.close()

	def __enter__(self):
		return self

	def __exit__(self, *excInfo):
		self.close()


class Session:
	def __init__(self, headers=None, timeout=DEFAULT_TIMEOUT):
		self.headers = {"User-agent": USER_AGENT}
		if headers:
			self.headers.update(headers)
		self.timeout = timeout
		self._lock = threading.Lock()
		self._response = None
		self._closed = False

	@property
	def closed(self):
		with self._lock:
			return self._closed

	def get(self, url, params=None, headers=None, timeout=None):
		allHeaders = dict(self.headers)
		if headers:
			allHeaders.update(headers)
		request = urllibRequest.Request(buildUrl(url, params), headers=allHeaders)
		self._raiseIfClosed()
		raw = urllibRequest.urlopen(request, timeout=self.timeout if timeout is None else timeout)
		response = Response(raw, onClose=self._forget)
		with self._lock:
			if not self._closed:
				self._response = response
				return response
		response.abort()
		raise SessionClosed("The session was closed while the request was in flight")

	def close(self):
		with self._lock:
			if self._closed:
				return
			self._closed = True
			response = self._response
			self._response = None
		if response is not None:
			response.abort()

	def _raiseIfClosed(self):
		with self._lock:
			if self._closed:
				raise SessionClosed("The session is closed")

	def _forget(self, response):
		with self._lock:
			if self._response is response:
				self._response = None

	def __enter__(self):
		return self

	def __exit__(self, *excInfo):
		self.close()


def get(url, params=None, headers=None, timeout=DEFAULT_TIMEOUT):
	return Session(timeout=timeout).get(url, params=params, headers=headers)
