# Pikakääntäjä #

* Tekijät: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  sekä muut NVDA-yhteisön jäsenet.
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

## Kielten määrittäminen ##
Määritä lähde-, kohde- ja vaihdettava kieli valitsemalla "Pikakääntäjä..."-vaihtoehto kohdasta NVDA-valikko -> Asetukset.

Valintaikkunassa on kaksi yhdistelmäruutua, jotka ovat "Lähdekieli" ja
"Kohdekieli", sekä valintaruutu, jolla voit valita, kopioidaanko käännös
leikepöydälle.

Lisäksi, jos valitsit "Lähdekieli"-yhdistelmäruudusta ensimmäisenä olevan
Tunnista automaattisesti -vaihtoehdon, käytössä on myös "Vaihdettava
kieli"-yhdistelmäruutu sekä valintaruutu, jolla automaattinen kielen
vaihtaminen voidaan ottaa käyttöön.

Kahden ensimmäisen yhdistelmäruudun ja kopiointivalintaruudun tarkoitus on
selvä, mutta muiden käytöstä on tarpeen kertoa jotain. Alla olevissa
selityksissä oletetaan, että Lähdekieli-yhdistelmäruudussa on valittuna
automaattinen tunnistus.

"Vaihdettava kieli" -yhdistelmäruudusta on hyötyä vaihtaessasi lähde- ja
kohdekieltä näppäinkomentoa avulla (katso alta). Kohdekielen määrittämisestä
automaattiseksi ei ole järkeä, joten lisäosa asettaa sen arvoksi saman kuin
yllä olevassa yhdistelmäruudussa.

Kuvittele seuraavanlainen tilanne: käännät tekstiä tavallisesti englanniksi,
joka on pääasiallinen kielesi, mutta toisinaan (esim. asiakirjaa
kirjoittaessasi) sinun täytyy kääntää italiaksi, joka on toinen
kielesi. Valitse "Vaihdettava kieli" -yhdistelmäruudusta italia, jotta voit
kääntää englannista italiaksi menemättä lisäosan asetuksiin. On selvää, että
tämän toiminnon hyödyllisyys riippuu siitä, miten usein sinulla on sille
käyttöä.

Nyt on vuorossa automaattisen kielen vaihtamisen valintaruutu: Se on
näkyvissä jos ja vain jos olet valinnut "Lähdekieli"-yhdistelmäruudusta
automaattisen tunnistuksen, ja se on suoraan yhteydessä "Vaihdettava kieli"
-yhdistelmäruutuun. Mikäli olet valinnut tämän valintaruudun, lisäosa
yrittää muuttaa lähde- ja kohdekielten asetukset sellaisiksi, joissa
kohdekielestä tulee lähdekieli ja "Vaihdettava kieli"-yhdistelmäruudussa
valitusta kielestä uusi kohdekieli. Tämä on äärimmäisen hyödyllistä, mikäli
kääntämäsi tekstin kieli on "Kohdekieli"-yhdistelmäruudussa määritettyä
kieltä.

Yksinkertainen esimerkki: Palauta mieleesi aiemmin kuviteltu tilanne. Jos
kääntämäsi tekstin kieli on jokin muu kuin englanti, ongelmia ei ole - saat
asianmukaisen englanninkielisen käännöksen. Mutta jos sinun täytyy kääntää
englanninkielistä tekstiä, saat normaalisti käännöksen englanniksi, joka on
täsmälleen sama kuin alkuperäinen teksti, mistä ei tietenkään ole mitään
hyötyä. Kiitos automaattisen kielenvaihtamistoiminnon, olettaen, että haluat
tietää, miltä tekstisi italiankielinen käännös kuulostaa, lisäosa voi
kuitenkin vaihtaa kohdekielen automaattisesti italiaksi, jolloin saat
asianmukaisen käännöksen.

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## Käyttö ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. Voit kääntää myös leikepöydällä olevaa tekstiä.
3. Press the dedicated shortcut key to translate the last spoken text.

## Pikanäppäimet ##
Seuraavia komentoja  on painettava toimintonäppäimen NVDA+Shift+T jälkeen:

* T: Käännä valittu teksti.
* Shift+T: Käännä leikepöydällä oleva teksti.
* S: Vaihda lähde- ja kohdekieliä.
* A: Ilmoita nykyiset asetukset.
* C: Kopioi viimeisin käännös leikepöydälle.
* I: Tunnista valitun tekstin kieli.
* L: translate the last spoken text,
* O: open translation settings dialog
* H: announces all available layered commands.

## Changes for 4.4.2 ##
* Restore language detection and auto-swapping (Thanks to Cyrille for fix)
* updated languages for translation (thanks to Cyrille)

## Changes for 4.4 ##
* Instant translate is now compatible with NVDA 2019.3 (Python 3 versions of
  NVDA)

## Changes for 4.3 ##
* nvda compatibility fix Now instant translate will be compatible with
  latest nvda builds.
* found a way to use google as a translation service again.

## Changes for 4.2 ##
* Restored working state with newer versions of nvda.
* Restored automatic language detection.

## Muutokset versiossa 4.1 ##
* Pikakääntäjä toimii taas, ja käyttää nyt Googlen sijaan
  Yandex-kääntäjäpalvelua.

## Muutokset versiossa 4.0 ##
* Käännös suoritetaan automaattisesti kielen vaihtamisen jälkeen.
* Välimuistibugi korjattu.

## Muutokset versiossa 3.0 ##
* Pikanäppäinten käyttötapaa on muutettu. Paina ensin Pikakääntäjän
  toimintonäppäintä (NVDA+Shift+T) ja sitten haluamaasi toimintoa vastaavaa
  kirjainta (katso kaikki komennot Pikanäppäimet-kappaleesta).
* Kielten vaihtaminen toteutettu.
* Asetusten muotoa on muutettu. Pikakääntäjän asetusten muuttaminen on nyt
  mahdollista vain luku -tiedostojärjestelmissä, mutta tehdyt muutokset ovat
  voimassa vain NVDA:n seuraavaan uudelleenkäynnistykseen asti.
* Poistettu käännettävän tekstimäärän rajoitus.
* Lisätty t-pikanäppäin englanninkieliseen Pikakäännöksen asetukset
  -valikkokohteeseen
* Automaattinen tunnistus on nyt ensimmäisenä vaihtoehtona
  Lähdekieli-yhdistelmäruudussa, ja poistettu kokonaan
  Kohdekieli-yhdistelmäruudusta.
* Lisätty valintaruutu käännöstuloksen kopioinnin määrittämiseksi.
* Asetustiedosto tallennetaan asetuskansion juureen.
* Lähde- ja kohdekielet synkronoitu Google-kääntäjän tällä hetkellä
  käyttämien kielten kanssa (22. huhtikuuta 2015).


## Muutokset versiossa 2.1 ##
* Lisäosa voi kääntää leikepöydällä olevan tekstin painettaessa
  NVDA+Shift+Y.

## Muutokset versiossa 2.0 ##
* Lisätty graafinen käyttöliittymä, josta voidaan valita lähde- ja
  kohdekieli.
* Lisätty valikko, joka löytyy Asetukset-valikosta.
* Asetukset kirjoitetaan nyt erilliseen asetustiedostoon.
* Käännöksen tulokset kopioidaan nyt automaattisesti leikepöydälle tulevaa
  käsittelyä varten.

## Muutokset versiossa 1.0 ##
* Ensimmäinen versio.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
