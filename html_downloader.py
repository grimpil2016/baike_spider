# coding:utf8

from urllib import request
import urllib

class HtmlDownloader(object):

	def download(self, url):
		if url is None:
			return None

		response = urllib.request.urlopen(url)

		if response.getcode() != 200:
			return None

		return response.read()