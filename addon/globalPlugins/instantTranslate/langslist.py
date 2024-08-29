#langslist.py
# Copyright (C) 2012-2016 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from languageHandler import getLanguageDescription
import addonHandler
addonHandler.initTranslation()

def g(code, short=False):
	"""Return an NVDA language description for code, if one is available. Otherwise, return the one from needed_codes. If that fails, return the code.
	If short is True, returns a more compact description for the "auto" special code.
	"""
	if short and code == "auto":
		# Translators: A short description for "Automatically detect language" language choice, reported when
		# the user requests or swaps the current configuration.
		return _("Automatic")
	res = getLanguageDescription(code)
	if res is not None: return res
	if code in needed_codes:
		return needed_codes[code]
	return code

needed_codes = {
	# Translators: An option to automatically detect source language for translation.
	"auto":_("Automatically detect language"),
	# Translators: The name of a language supported by this add-on.
	"ceb":_("Cebuano"),
	# Translators: The name of a language supported by this add-on.
	"eo":_("Esperanto"),
	# Translators: The name of a language supported by this add-on.
	"haw":_("Hawaiian"),
	# Translators: The name of a language supported by this add-on.
	"hmn":_("Hmong"),
	# Translators: The name of a language supported by this add-on.
	"ht":_("Creole Haiti"),
	# Translators: The name of a language supported by this add-on.
	"jv":_("Javanese"),
	# Translators: The name of a language supported by this add-on.
	"ku":_("Kurdish"),
	# Translators: The name of a language supported by this add-on.
	"la":_("Latin"),
	# Translators: The name of a language supported by this add-on.
	"mg":_("Malagasy"),
	# Translators: The name of a language supported by this add-on.
	"my":_("Myanmar (Burmese)"),
	# Translators: The name of a language supported by this add-on.
	"ny":_("Chichewa"),
	# Translators: The name of a language supported by this add-on.
	"sd":_("Sindhi"),
	# Translators: The name of a language supported by this add-on.
	"sm":_("Samoan"),
	# Translators: The name of a language supported by this add-on.
	"sn":_("Shona"),
	# Translators: The name of a language supported by this add-on.
	"so":_("Somali"),
	# Translators: The name of a language supported by this add-on.
	"st":_("Sesotho"),
	# Translators: The name of a language supported by this add-on.
	"su":_("Sundanese"),
	# Translators: The name of a language supported by this add-on.
	"tl":_("Tagalog"),
	# Translators: The name of a language supported by this add-on.
	"yi":_("Yiddish"),
}

langcodes = [
	"auto",
	"af",
	"am",
	"ar",
	"az",
	"be",
	"bg",
	"bn",
	"bs",
	"ca",
	"ceb",
	"co",
	"cs",
	"cy",
	"da",
	"de",
	"el",
	"en",
	"eo",
	"es",
	"et",
	"eu",
	"fa",
	"fi",
	"fr",
	"fy",
	"ga",
	"gd",
	"gl",
	"gu",
	"ha",
	"haw",
	"he",
	"hi",
	"hmn",
	"hr",
	"ht",
	"hu",
	"hy",
	"id",
	"ig",
	"is",
	"it",
	"ja",
	"jv",
	"ka",
	"kk",
	"km",
	"kn",
	"ko",
	"ku",
	"ky",
	"la",
	"lb",
	"lo",
	"lt",
	"lv",
	"mg",
	"mi",
	"mk",
	"ml",
	"mn",
	"mr",
	"ms",
	"mt",
	"my",
	"ne",
	"nl",
	"no",
	"ny",
	"or",
	"pa",
	"pl",
	"ps",
	"pt",
	"ro",
	"ru",
	"rw",
	"sd",
	"si",
	"sk",
	"sl",
	"sm",
	"sn",
	"so",
	"sq",
	"sr",
	"st",
	"su",
	"sv",
	"sw",
	"ta",
	"te",
	"tg",
	"th",
	"tk",
	"tl",
	"tr",
	"tt",
	"ug",
	"uk",
	"ur",
	"uz",
	"vi",
	"xh",
	"yi",
	"yo",
	"zh-CN",
	"zh-TW",
	"zu",
]

langslist = {}
for code in langcodes:
	langslist[g(code)] = code
