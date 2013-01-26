#langslist.py
# Copyright (C) 2012-2013 Aleksey Sadovoy AKA Lex <lex@progger.ru>,
#ruslan <ru2020slan@yandex.ru>,
#beqa <beqaprogger@gmail.com>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

from languageHandler import getLanguageDescription
def g(code):
	"""Return an NVDA language description for code, if one is available. Otherwise, return the one from needed_codes. If that fails, return the code."""
	res = getLanguageDescription(code)
	if res is not None: return res
	if res in needed_codes:
		return needed_codes[res]
	return code

needed_codes = {
	"auto":_("Automatically detect language"),
	"ht":_("Creole Haiti"),
	"la":_("Latin"),
	"tl":_("Tagalog"),
	"cy":_("ci"),
	"yi":_("Yiddish"),
	"eo":_("Esperanto"),
	"gu":_("Gujarati"),
	"sw":_("Kiswahili"),
	"ar":_("Arabic"),
	"hy":_("Armenian"),
	"bn":_("Bangla"),
	"zh-TW":_("Chinese (Traditional)"),
	"no":_(u'Norwegian (Bokm\xe5l)'),
	'zh-CN':_('Chinese (Simplified)'),
	"sr":_("Serbian (Latin)"),
}

langcodes = [
	"auto",
	"af",
	"sq",
	"ar",
	"hy",
	"az",
	"eu",
	"be",
	"bn",
	"bg",
	"kn",
	"ca",
	"cs",
	"zh-CN",
	"zh-TW",
	"ht",
	"hr",
	"da",
	"nl",
	"en",
	"et",
	"fi",
	"fr",
	"gl",
	"ka",
	"de",
	"el",
	"gu",
	"he",
	"hi",
	"hu",
	"id",
	"ga",
	"is",
	"it",
	"ja",
	"ko",
	"la",
	"lv",
	"lt",
	"mk",
	"ms",
	"mt",
	"no",
	"fa",
	"pl",
	"pt",
	"ro",
	"ru",
	"sr",
	"sk",
	"sl",
	"es",
	"sw",
	"sv",
	"tl",
	"ta",
	"te",
	"th",
	"tr",
	"uk",
	"ur",
	"vi",
	"cy",
	"yi",
	"eo",
]
langslist = {}
for code in langcodes:
 langslist[g(code)] = code
 print langslist