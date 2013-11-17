#langslist.py
# Copyright (C) 2012-2013 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from languageHandler import getLanguageDescription
import addonHandler
addonHandler.initTranslation()

def g(code):
	"""Return an NVDA language description for code, if one is available. Otherwise, return the one from needed_codes. If that fails, return the code."""
	res = getLanguageDescription(code)
	if res is not None: return res
	if code in needed_codes:
		return needed_codes[code]
	return code

needed_codes = {
	# Translators: An option to automatically detect source language for translation.
	"auto":_("Automatically detect language"),
	# Translators: The name of a language supported by this add-on.
	"ar":_("Arabic"),
	# Translators: The name of a language supported by this add-on.
	"bn":_("Bangla"),
	# Translators: The name of a language supported by this add-on.
	"cy":_("Welsh"),
	# Translators: The name of a language supported by this add-on.
	"eo":_("Esperanto"),
	# Translators: The name of a language supported by this add-on.
	"gu":_("Gujarati"),
	# Translators: The name of a language supported by this add-on.
	"ht":_("Creole Haiti"),
	# Translators: The name of a language supported by this add-on.
	"hy":_("Armenian"),
	# Translators: The name of a language supported by this add-on.
	"la":_("Latin"),
	# Translators: The name of a language supported by this add-on.
	"no":_(u'Norwegian'),
	# Translators: The name of a language supported by this add-on.
	"sr":_("Serbian (Latin)"),
	# Translators: The name of a language supported by this add-on.
	"sw":_("Swahili"),
	# Translators: The name of a language supported by this add-on.
	"tl":_("Tagalog"),
	# Translators: The name of a language supported by this add-on.
	"yi":_("Yiddish"),
	# Translators: The name of a language supported by this add-on.
	'zh-CN':_('Chinese (Simplified)'),
	# Translators: The name of a language supported by this add-on.
	"zh-TW":_("Chinese (Traditional)"),
}

langcodes = [
	"auto",
	"af",
	"ar",
	"az",
	"sq",
	"eu",
	"be",
	"bn",
	"bg",
	"ca",
	"cs",
	"cy",
	"da",
	"de",
	"el",
	"en",
	"eo",
	"es",
	"et",
	"fa",
	"fi",
	"fr",
	"ga",
	"gl",
	"gu",
	"he",
	"hi",
	"hr",
	"ht",
	"hu",
	"hy",
	"id",
	"is",
	"it",
	"ja",
	"ka",
	"ko",
	"kn",
	"la",
	"lv",
	"lt",
	"mk",
	"ms",
	"mt",
	"no",
	"nl",
	"pl",
	"pt",
	"ro",
	"ru",
	"sk",
	"sl",
	"sr",
	"sv",
	"sw",
	"ta",
	"te",
	"th",
	"tl",
	"tr",
	"uk",
	"ur",
	"vi",
	"yi",
	"zh-CN",
	"zh-TW",
]

langslist = {}
for code in langcodes:
	langslist[g(code)] = code
