# Ekspres-oversættelse #

* Forfattere: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto
  Buffolino og andre NVDA -bidragydere.
* Download [stabil version][1]
* Download [udviklingsversion][2]

Denne tilføjelse bruges til at oversætte markeret og/eller
udklipsholdertekst fra et sprog til et andet. Dette gøres ved hjælp af
Google Translate -tjenesten.

## Konfiguration af sprog ##
For at konfigurere kilde, mål og ombytningssprog, skal du gå til: NVDA -menu/Opsætning/Indstillinger for Ekspres-oversættelse.

Der er to combo bokse, "Kildesprog" og "Målsprog" og en check box der
bestemmer, om oversættelsen skal kopieres til udklipsholderen.

Hvis du har valgt automatisk indstilling (førstevalget) fra boksen
"Kildesprog", er der også en komboboks kaldet "Sprog til ombytning" og en
check box til at aktivere automatisk ombytning.

Betydningen af to første bokse og afkrydsningsfelt for kopiering er nemme at
forstå udfra ordlyden, men nogle ord om resten er nødvendige. Husk altid, at
forklaringerne herunder tager udgangspunkt i det kildesprog, der er
indstillet for den automatiske oversættelse.

Komboboksen "Sprog til ombytning" er nyttig, når du skifter kilde- og
målsprog via script (se nedenfor). Faktisk har et målsprog, der er
indstillet på autoindstillingen ingen mening, så tilføjelsen indstiller
værdien af komboboksen ovenfor.

Så forestil dig denne situation: Du oversætter normalt til engelsk (dit
hovedsprog), men nogle gange (f.eks. Når du skriver et dokument) skal du
oversætte til italiensk (dit andet sprog). Du kan indstille boksen "Sprog
til ombytning" til italiensk, så tilføjelsen oversætter fra engelsk til
italiensk uden at det er nødvendigt at gå ind i tilføjelsesindstillingerne.

Nu kommer vi til check boksen "Automatisk ombytning". Denne mulighed vises,
hvis du indstiller autoindstillingen i boksen "Kildesprog" og er direkte
forbundet med "Sprog til ombytning". Hvis du aktiverer dette, forsøger
tilføjelsen automatisk at benytte dine indstillinger for kilde- og målsprog
til en konfiguration, hvor målsproget bliver kildesprog, og det sprog, der
er valgt i boksen "Sprog til ombytning", er det nye målsprog. Dette er
ekstremt nyttigt, hvis kildesproget for den tekst, du vil oversætte, er
målsproget.

Endnu et simpelt eksempel: husk på den tidligere forestillede
situation. Hvis du oversætter en tekst til et andet sprog end engelsk, er
der ikke noget problem. Du får den korrekte oversættelse til engelsk. Men
hvis du har brug for at oversætte en tekst fra engelsk, får du normalt en
oversættelse på engelsk identisk med originalteksten, og dette er jo ret
ubrugeligt. Takket være funktionen for automatisk ombytning, ændre
tilføjelsen automatisk målsproget til italiensk, så du får en gyldig og
brugbar oversættelse.

Dette er en midlertidig konfiguration. Hvis denne mulighed ikke har nogen
effekt (den er eksperimentel), skal du prøve at ændre manuelt til en stabil
konfiguration ved hjælp af kommandoen for ombytning beskrevet nedenfor. Det
er eksperimentelt, fordi Google i nogle situationer (typisk med korte
tekster) ikke genkender det rigtige kildesprog korrekt, og du skal skifte
sprog manuelt via script, for at tvinge kildesproget til at være det
tidligere målsprog (engelsk i vores eksempel).

I dialogen med parametre for taleindstillinger (NVDA -menu /Opsætning/Indstillinger/Tale) kan du ændre indstillingen "Automatisk skift af sprog". På denne måde, vil oversættelsen blive annonceret på det pågældende sprog, hvis du benytter en flersproget talesyntese.

## Brug ##
Du kan bruge denne tilføjelse på tre måder:

1. Vælg noget tekst ved hjælp af markeringskommandoer (f.eks. Skift med
   piletasterne), og tryk på den tilhørende tast for at
   oversætte. Oversættelsesresultatet læses med den talesyntese, du bruger.
2. Du kan også oversætte tekst fra udklipsholderen.
3. Tryk på den tilknyttede genvejstast for at oversætte den sidst udtalte
   tekst.

## Tastaturkommandoer ##
Alle følgende kommandoer skal trykkes efter kommandoen NVDA+Shift+t er
trykket:

* T: Oversæt den valgte tekst
* Shift+t: Oversæt tekst fra udklipsholderen
* S: Byt kilde- og målsprog
* A: Annoncér den aktuelle konfiguration
* C: Kopier det sidste resultat til udklipsholderen
* I: Genkendt sproget for den valgte tekst
* L: Oversæt den sidste udtalte tekst
* O: Åbn dialogen med oversættelsesindstillinger
* H: annoncerer alle tilgængelige lagdelte kommandoer.

## Ændringer for 4.4.3 ##
* Tilføjet muligheden for at erstatte understregninger med mellemrum, kan
  give bedre oversættelsesresultater afhængigt af kontekst (takket være Beka
  Gozalishvili)
* Tilføjet kompatibilitet til NVDA 2022.1

## Ændringer for 4.4.2 ##
* Gendannet sprogregistrering og automatisk ombytning af sprog(Tak til
  Cyrille for rettelsen)
* Opdaterede oversættelser for tilføjelsen(tak til Cyrille)

## Ændringer i 4.4 ##
* Ekspres-oversættelse er nu kompatibel med NVDA 2019.3 (Python 3 -versioner
  af NVDA)

## Ændringer til 4.3 ##
* Rettelse for NVDA-kompatibilitet
* Fandt en måde at bruge google som oversættelsestjeneste igen.

## Ændringer til 4.2 ##
* Gendannet fungerbar tilstand med nyere versioner af NVDA.
* Gendannet automatisk sprogregistrering.

## Ændringer for 4.1 ##
* Ekspres-oversættelse fungerer igen, nu med Yandex oversættelsestjeneste i
  stedet for Google.

## Ændringer i4.0  ##
* Oversættelse udføres automatisk efter ombytning.
* Cache-fejl rettet.

## Ændringer i 3.0 ##
* Ændret måde, hvorpå genveje bruges. Nu kan du trykke på NVDA+Shift+t for
  at aktivere lagdelte kommandoer for Ekspres-oversættelse, og derefter en
  enkelt bogstavstast for at udføre en handling (se alle kommandoer i
  afsnittet "Tastaturkommandoer").
* Implementerede ombytning af sprog.
* Ændret konfigurationsformat, nu kan vi ændre øjeblikkelige
  oversættelsesindstillinger, hvis vi er i skrivebeskyttet rude, men husk,
  at dette ikke vil fungere før en genstart af NVDA.
* Fjernet grænsen for mængden af tekst, der kan oversættes.
* Tilføjet genvejen t til menupunktet Ekspres-oversættelse indstillinger
* Indstillingen for automatisk sprog er nu første mulighed i den combo boks,
  der bestemmer kildesproget. Indstillingen er ikke længere i boksen for
  målsprog.
* Tilføjet en check box til kopiering af oversættelsesresultater i
  indstillingerne.
* Gem konfigurationsfilen i roden af indstillingsmappen.
* Kilde- og målsprog synkroniseret med, hvad Google Translate i øjeblikket
  viser (22. april 2015).


## Ændringer i 2.1 ##
* Nu kan tilføjelsen oversætte tekst fra udklipsholderen, når der trykkes på
  NVDA+shift+y.

## Ændringer i 2.0 ##
* Tilføjet gui -konfigurator, hvor du kan vælge kilde- og målsprog.
* Tilføjet tilføjelsesmenupunkt i Opsætning fra NVDA-menuen
* Indstillinger skrives nu til separat konfigurationsfil.
* Oversættelsesresultater kopieres nu automatisk til udklipsholderen.

## Ændringer i 1.0 ##
* Første version.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=instantTranslate

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
