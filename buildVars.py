# Build customizations
# Change this file instead of sconstruct, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon-name" : "instantTranslate",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on informaiton.
	"addon-summary" : _("Instant Translate - Translates given text using the Google Translate service."),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("This addon translates selected or clipboard text using the Google Translate service and presents it. Press NVDA+Shift+T to translate selected text. Press NVDA+Shift+Y to translate clipboard text."),
	# version
	"addon-version" : "3.0-dev",
	# Author(s)
	"addon-author" : "Alexy Sadovoy aka Lex <lex@progger.su>, ruslan <ru2020slan@yandex.ru>, beqa <beqaprogger@gmail.com>, Mesar Hameed <mhameed@src.gnome.org> and other nvda contributors",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org/"
}

import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "instantTranslate", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
