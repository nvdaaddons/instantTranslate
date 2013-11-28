# तुरून्तै अनुवाद (instantTranslate) #

* Authors: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  and other nvda contributors.
* Download [version 3.0-dev][1]

यो थप-साधन चयनीत र क्लीपपाठिमा भएका पाठहरूलाई एउटा भाषाबाट अर्को भाषामा
अनुवाद गर्न प्रयो गरिन्छ । यो गुगल अनुवाद सेवाको प्रयोग गरि गरिन्छ ।

## भाषाहरूको अभियोजन ##
To configure source, target and in case swap language, from NVDA menu, go to
Preferences, then go to Instant Translate Settings.  There are three combo
boxes labeled "translate from", "translate into" and "Language for swapping"
(if you selected auto option from source languages).

If you selected the auto option from source languages, there is also a
checkbox about the auto-swap: if you activate it, then the addon tries to
commute automatically from your source and target configuration to a
configuration where target becomes the source language, and language
selected in "Language for swapping" combo is the new target language;
extremely useful if the source language of the text you want translate is
the target language.

However, this is a temporary configuration, if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below.

## यो थप साधन कसरी प्रयोग गर्ने? ##
यो थप-साधनको प्रयोग गर्ने दुई वटा तरीकाहरू छन् ।

1. Select some text using selection commands (shift with arrow keys, for
   example). Then press Shift+NVDA+T to translate the selected text. Then
   the translated string will be read, providing that the synthesizer you
   are using supports the target language.
2. Copy some text to clipboard. Then press Shift+NVDA+Y to translate the
   text in the clipboard to the target language.

## Other useful commands ##
* NVDA+shift+r: pressed once, announce current configuration; pressed twice,
  swap source and target languages.

## Changes for 3.0 ##
* Implemented swapping languages.
* Changed configuration format, now we can change instant translate settings
  if we are in readonly pane, but remember that this will work before first
  restart of nvda.
* Removed limit on amount of text that can be translated.
* तुरुन्तै अनुवादको अनुकूलता मेनुमा  द्रुत कुञ्जी t थपियो ।
* The auto option is now in first position in source combo, and absent in
  target combo.
* अनुदीत नतिजा प्रतिलिपीका लागि चेक बाकस थपियो ।
* अभियोजन फाइल अनुकूलता थैलीको मार्गमा नै बचत गरिन्छ । 
* नयाँ भाषाहरू: अर्गानिज, अरबी, ब्राजेलियन पुर्तगाली, क्रोएसियन, डच, जापानी,
  नेपाली, पोल्याणडेली, फिनिस, फ्रान्सेली, ग्यालिसियन, जर्मनी, हङ्गेरियाली,
  इटाली, कोरियाली, स्लोभाक, स्पेनी, तामिल, तुर्कि  स्लोभेनियन ।

## २.१ मा गरीएका परिवर्तन हरू ##
* अब यो थप-साधनले नेत्रवाणी +shift+y कुञ्जी दबाउँदा क्लीपपाटीका पाठहरूलाई
  अनुवाद गर्ने छ ।

## २.० मा गरीएका परिवर्तन हरू ##
* श्रोत र लक्षित भाषा छान्नका लागी भनेर छुट्टै पाटीको व्यबस्था गरियो ।
* प्राथमिकता मेनु भित्र थप-साधन मेनु थपियो ।
* अनुकूलतालाई अब छूट्टै अभियोजन फाइलमा लेखिन्छ ।
* भविष्यमा हेरफेर गर्नका लागि  अनुदीत नतिजा स्वतः क्लिपपाटीमा उतारिन्छ ।

## १.० मा गरीएका परिवर्तन हरू ##
* सुरुको संस्करण

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it-dev
