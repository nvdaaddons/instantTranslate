# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.
# Full getext (please don't change)
_ = lambda x : x
# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "instantTranslate",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Instant Translate"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("This addon translates selected or clipboard text using the Google Translate service and presents it."),
	# version
	"addon_version" : "4.5.3",
	# Author(s)
	"addon_author" : "Alexy Sadovoy aka Lex <lex@progger.su>, ruslan <ru2020slan@yandex.ru>, beqa <beqaprogger@gmail.com>, Mesar Hameed <mhameed@src.gnome.org>, Alberto Buffolino <a.buffolino@gmail.com>, and other NVDA contributors",
	# URL for the add-on documentation support
	"addon_url" : "https://addons.nvda-project.org/addons/instantTranslate",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported
	"addon_minimumNVDAVersion" : "2019.3",
	# Last NVDA version supported/tested
	"addon_lastTestedNVDAVersion" : "2023.1.0"
}

import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "instantTranslate", "*.py"), os.path.join("addon", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
