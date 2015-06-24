from cStringIO import StringIO
import os.path
import configobj
from validate import Validator
import globalVars
from logHandler import log
from locale import getdefaultlocale

INSTANTTRANSLATE_CONFIG_FILENAME = "instantTranslate.ini"
# get a language of the OS localization.
lo_lang = getdefaultlocale()
# get the first element of the tuplet.
s = lo_lang[0]
# get the default language which is translated into.
if s == "zh_HK":
	lo_lang = "zh-TW"
elif s.startswith("zh"):
	lo_lang = s.replace('_', '-')
else:
	lo_lang = s[0:s.find("_")]

instanttranslateConfig = None

_configSpec = """
[translation]
from = string(default=auto)
into = string(default={lo_lang})
swap = string(default=en)
[settings]
copytranslatedtext = boolean(default=true)
autoswap = boolean(default=true)
[temporary]
isautoswapped = boolean(default=false)
"""

def load():
	global instanttranslateConfig
	if instanttranslateConfig is None:
		path = os.path.join(globalVars.appArgs.configPath, INSTANTTRANSLATE_CONFIG_FILENAME)
		instanttranslateConfig = configobj.ConfigObj(path, configspec=StringIO(_configSpec.format(lo_lang=lo_lang)), encoding="utf-8")
		instanttranslateConfig.newlines = "\r\n"
		instanttranslateConfig.stringify = True
		val = Validator()
		ret = instanttranslateConfig.validate(val, preserve_errors=True, copy=True)
		if ret != True:
			log.warning("Instant Translate configuration is invalid: %s", ret)

def save():
	global instanttranslateConfig
	if instanttranslateConfig is None:
		raise RuntimeError("Instant Translate config is not loaded.")
	val = Validator()
	instanttranslateConfig.validate(val, copy=True)
	instanttranslateConfig.write()
