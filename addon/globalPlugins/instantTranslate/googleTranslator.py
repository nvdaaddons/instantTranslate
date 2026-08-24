# Copyright (C) 2013 - 2024 Mesar Hameed <mhameed@src.gnome.org>, Beka Gozalishvili <beqaprogger@gmail.com>
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import languageHandler

from . import httpClient
from .baseTranslator import BaseTranslator, LanguageCache, cachePath

API_KEY = "AIzaSyDLEeFI5OtFBwYBIoK_jj5m32rZK5CkCXA"
CLIENT_NAME = "gtx"
TRANSLATE_URL = "https://translate-pa.googleapis.com/v1/translate"
LANGUAGES_URL = "https://translate-pa.googleapis.com/v1/supportedLanguages"
DATA_TYPES = ("TRANSLATION", "SENTENCE_SPLITS")
HEADERS = {"Content-Type": "application/json+protobuf"}
LANGUAGES_TTL = 86400
LANGUAGES_FILE = "gt_langs.json"


class GoogleTranslator(BaseTranslator):
	backEndName = "Google Translate"
	maxChunkSize = 12000

	def translateChunk(self, chunk, langTo):
		params = [
			("params.client", CLIENT_NAME),
			("query.source_language", self.langFrom),
			("query.target_language", langTo),
			("query.display_language", displayLanguage()),
			("query.text", chunk),
			("key", API_KEY),
		]
		params += [("data_types", dataType) for dataType in DATA_TYPES]
		response = self.session.get(TRANSLATE_URL, params=params, headers=HEADERS).json()
		sentences = response[1] if len(response) > 1 else None
		if sentences:
			translation = "".join(sentence[0] for sentence in sentences if sentence and sentence[0])
		else:
			translation = response[0] or ""
		detected = response[5] if len(response) > 5 and response[5] else self.langFrom
		return translation, detected


def displayLanguage():
	return languageHandler.getLanguage().replace("_", "-")


def fetchLanguages():
	params = [
		("client", CLIENT_NAME),
		("display_language", displayLanguage()),
		("key", API_KEY),
	]
	response = httpClient.get(LANGUAGES_URL, params=params, headers=HEADERS).json()
	return {
		"source": _asLanguageDict(response[0]),
		"target": _asLanguageDict(response[1]),
	}


def _asLanguageDict(languages):
	return {
		BaseTranslator.legacyCodes.get(code, code): name
		for code, name in languages
		if code and name
	}


languageCache = LanguageCache(
	path=cachePath(LANGUAGES_FILE),
	ttl=LANGUAGES_TTL,
	fetch=fetchLanguages,
	getContext=displayLanguage,
)
