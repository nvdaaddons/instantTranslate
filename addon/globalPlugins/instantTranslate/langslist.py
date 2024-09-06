#langslist.py
# Copyright (C) 2012-2016 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#other nvda contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from languageHandler import getLanguageDescription
from logHandler import log
import addonHandler
addonHandler.initTranslation()

def g(code, short=False):
	"""Return a description for the language code passed as parameter. The first found code is returned.
	The check order is the following:
	- the code in the forced codes list, i.e. codes for which NVDA/Windows do not return a satisfactory description
	- the code is in NVDA/Windows language description
	- the code in the list of needed codes, i.e. codes not available in some versions of Windows
	If all these checks fail, return the code.
	If short is True, returns a more compact description for the "auto" special code.
	"""
	if short and code == "auto":
		# Translators: A short description for "Automatically detect language" language choice, reported when
		# the user requests or swaps the current configuration.
		return _("Automatic")
	if code in forced_codes:
		return forced_codes[code]
	res = getLanguageDescription(code)
	if res is not None: return res
	if code in needed_codes:
		return needed_codes[code]
	return code

forced_codes = {
	# Translators: The name of a language supported by this add-on.
	"ckb": _("Kurdish (Sorani)"),
}

needed_codes = {
	# Translators: An option to automatically detect source language for translation.
	"auto":_("Automatically detect language"),
	# Translators: The name of a language supported by this add-on.
	"ak": _("Twi (Akan)"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"ay": _("Aymara"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"bho": _("Bhojpuri"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"bm":_("Bambara"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"ceb":_("Cebuano"),
	# Translators: The name of a language supported by this add-on.
	"doi": _("Dogri"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"ee": _("Ewe"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"eo":_("Esperanto"),
	# Translators: The name of a language supported by this add-on.
	"gom": _("Konkani"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"haw":_("Hawaiian"),
	# Translators: The name of a language supported by this add-on.
	"hmn":_("Hmong"),
	# Translators: The name of a language supported by this add-on.
	"ht":_("Creole Haiti"),
	# Translators: The name of a language supported by this add-on.
	"ilo": _("Ilocano"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"jv":_("Javanese"),
	# Translators: The name of a language supported by this add-on.
	"kri": _("Krio"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"ku":_("Kurdish"),
	# Translators: The name of a language supported by this add-on.
	"la":_("Latin"),
	# Translators: The name of a language supported by this add-on.
	"lg":  _("Luganda"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"ln": _("Lingala"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"lus": _("Mizo"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"mai": _("Maithili"),  # Missing, tested on Windows 10 22H2
	# Translators: The name of a language supported by this add-on.
	"mg":_("Malagasy"),
	# Translators: The name of a language supported by this add-on.
	"mni-Mtei": _("Meiteilon (Manipuri)"),  # Missing, tested on Windows 10 22H2
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
	"ak",
	"am",
	"ar",
	"as",
	"ay",
	"az",
	"be",
	"bg",
	"bho",
	"bm",
	"bn",
	"bs",
	"ca",
	"ceb",
	"ckb",
	"co",
	"cs",
	"cy",
	"da",
	"de",
	"doi",
	"dv",
	"ee",
	"el",
	"en",
	"eo",
	"es",
	"et",
	"eu",
	"fa",
	"fi",
	"fil",
	"fr",
	"fy",
	"ga",
	"gd",
	"gl",
	"gn",
	"gom",
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
	"ilo",
	"is",
	"it",
	"ja",
	"jv",
	"ka",
	"kk",
	"km",
	"kn",
	"ko",
	"kri",
	"ku",
	"ky",
	"la",
	"lb",
	"lg",
	"ln",
	"lo",
	"lt",
	"lus",
	"lv",
	"mai",
	"mg",
	"mi",
	"mk",
	"ml",
	"mn",
	"mni-Mtei",
	"mr",
	"ms",
	"mt",
	"my",
	"ne",
	"nl",
	"no",
	"nso",
	"ny",
	"om",
	"or",
	"pa",
	"pl",
	"ps",
	"pt",
	"qu",
	"ro",
	"ru",
	"rw",
	"sa",
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
	"ti",
	"tk",
	"tl",
	"tr",
	"ts",
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
	name = g(code)
	try:
		oldName = langslist[name]
		log.error(f'Unable to add "{name}" (code "{code}"): this language name already exists for code "{oldName}".')
	except KeyError:
		langslist[name] = code
