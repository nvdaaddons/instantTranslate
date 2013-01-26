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
	if code in needed_codes:
		return needed_codes[code]
	return code

needed_codes = {
	"auto":_("Automatically detect language"),
	"ar":_("Arabic"),
	"bn":_("Bangla"),
	"cy":_("Welsh"),
	"eo":_("Esperanto"),
	"gu":_("Gujarati"),
	"ht":_("Creole Haiti"),
	"hy":_("Armenian"),
	"la":_("Latin"),
	"no":_(u'Norwegian'),
	"sr":_("Serbian (Latin)"),
	"sw":_("Swahili"),
	"tl":_("Tagalog"),
	"yi":_("Yiddish"),
	'zh-CN':_('Chinese (Simplified)'),
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
