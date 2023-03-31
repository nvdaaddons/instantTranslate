# Pikakääntäjä #

* Tekijät: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino
  sekä muut NVDA-yhteisön jäsenet.
* Lataa [vakaa versio][1]
* Lataa [kehitysversio][2]

Tätä lisäosaa käytetään valitun ja/tai leikepöydällä olevan tekstin
kääntämiseen kielestä toiselle.  Käännös suoritetaan
Google-kääntäjä-palvelua käyttäen.

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

Tämä asetus on oikeastaan tarkoitettu vain tilapäiseen käyttöön. Mikäli
tällä kokeellisella toiminnolla ei ole vaikutusta, kokeile vaihtaa
manuaalisesti vakaisiin asetuksiin alla kuvailtua kielenvaihtamiskomentoa
käyttäen. Toiminto on kokeellinen, koska Google ei tunnista todellista
lähdekieltä oikein joissakin tilanteissa (tyypillisesti lyhyiden tekstien
kanssa), ja sinun täytyy vaihtaa kieliä manuaalisesti näppäinkomentoa
käyttäen pakottaaksesi lähdekieleksi aiemman kohdekielen (meidän
tapauksessamme englanti).

Voit halutessasi valita "Vaihda kieltä automaattisesti (kun sitä tuetaan)" -asetuksen Puheasetukset-asetuspaneelista (NVDA-valikko -> Asetukset -> Asetukset -> Puhe). Tällä tavoin syntetisaattori puhuu käännöksen kohdekielen äänellä, mikäli käytät monikielistä syntetisaattoria.

## Käyttö ##
Voit käyttää tätä lisäosaa kolmella eri tavalla:

1. Valitse tekstiä valitsemiskomennoilla
   (esim. Shift+nuolinäppäimet). Käännä sitten valittu teksti painamalla
   määritettyä näppäinkomentoa. Tämän jälkeen käännös luetaan käyttämälläsi
   puhesyntetisaattorilla.
2. Voit kääntää myös leikepöydällä olevaa tekstiä.
3. Käännä viimeksi puhuttu teksti painamalla erillistä pikanäppäintä.

## Pikanäppäimet ##
Seuraavia komentoja  on painettava toimintonäppäimen NVDA+Shift+T jälkeen:

* T: Käännä valittu teksti.
* Shift+T: Käännä leikepöydällä oleva teksti.
* S: Vaihda lähde- ja kohdekieliä.
* A: Ilmoita nykyiset asetukset.
* C: Kopioi viimeisin käännös leikepöydälle.
* I: Tunnista valitun tekstin kieli.
* L: Käännä viimeksi puhuttu teksti.
* O: Avaa käännösasetusten valintaikkuna.
* H: Puhuu kaikki käytettävissä olevat komentokerroksen komennot.

## Muutokset versiossa 4.4.3 ##
* Lisätty mahdollisuus alaviivojen korvaamiseen välilyönneillä, mikä saattaa
  kontekstista riippuen tarjota parempia käännöstuloksia (kiitos Beka
  Gozalishvilille)
* Lisätty yhteensopivuus NVDA 2022.1:lle

## Muutokset versiossa 4.4.2 ##
* Kielen tunnistus ja automaattinen vaihto palautettu (kiitos Cyrille'lle
  korjauksesta).
* Käännöskieliä päivitetty (kiitos Cyrille'lle).

## Muutokset versiossa 4.4 ##
* Pikakääntäjä on nyt yhteensopiva NVDA 2019.3:n kanssa (NVDA:n Python 3
  -versiot).

## Muutokset versiossa 4.3 ##
* NVDA-yhteensopivuus korjattu. Pikakääntäjä on nyt yhteensopiva
  viimeisimpien NVDA-versioiden kanssa.
* Löydetty jälleen keino Googlen käyttämiseen käännöspalveluna.

## Muutokset versiossa 4.2 ##
* Palautettu toimivuus uudempien NVDA-versioiden kanssa.
* Automaattinen kielen tunnistus palautettu.

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

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
