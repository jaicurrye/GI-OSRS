# AUDIT_REGELS — herbruikbare auditchecklist voor rollenmoordspellen

Deze checklist is generiek. Hij is bedoeld voor een spelpakket dat bestaat uit
(a) een introductie-/regelbestand, (b) één rolblad per speler, en (c) een
afzonderlijk oplossingsbestand. Elke regel is als **PASS / FAIL / N.V.T.**
te beoordelen; smaakoordelen ("is het spannend?") horen hier niet thuis.

## Hulpmiddelen die je vóór het auditen opbouwt

Bouw deze vier werkstukken eerst; bijna elke regel verwijst ernaar.

- **T — Tijdlijnmatrix.** Eén rij per speler (plus het slachtoffer), één kolom per
  tijdvak van 5 minuten over het hele venster van de introductie tot het vinden
  van het lichaam. Vul per cel: locatie + bron (eigen blad / naam van getuige).
- **R — Ruimtebezettingstabel.** Eén rij per ruimte, dezelfde kolommen als T.
  Vul per cel de aanwezige personen in.
- **W — Wederkerigheidsmatrix.** Vierkante matrix speler × speler. Cel (A,B) =
  "blad van A stelt dat A B waarnam, met tijdvak". Gebruikt voor regels over
  wederzijdse bevestiging.
- **A — Aanwijzingenregister.** Eén regel per aanwijzing, waarneming, geluid,
  voorwerp, geheim en rekwisiet, met: bronbestand, tijdstip, en de kolom
  "verklaard door" (waar in het materiaal wordt dit opgelost?).

Noteer daarnaast **M = het beslissende moment** (het tijdvak waarin de daad
volgens het oplossingsbestand valt) en **B = de bewijsbare bovengrens/ondergrens**
van het moordvenster zoals afleidbaar uit niet-daderbladen.

---

## 1. Interne consistentie

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-01 | Geen enkele speler staat in hetzelfde tijdvak op twee plaatsen. | Loop T rij voor rij; markeer cellen met meer dan één locatie. |
| C-02 | Elke wederzijdse waarneming is symmetrisch: als A zegt met B te zijn, staat dat verenigbaar op B's blad. | W: vergelijk cel (A,B) met (B,A); een leeg tegenveld is alleen PASS als B's blad die periode niet beschrijft en niets tegenstrijdigs zegt. |
| C-03 | Genoemde tijdvakken van gezamenlijke aanwezigheid komen op beide bladen numeriek overeen (begin- en eindtijd binnen de gestelde tolerantie). | W + T: noteer per paar beide intervallen en het verschil in minuten. |
| C-04 | Ruimtebezetting is consistent: wie volgens één blad in ruimte X is, staat op geen enkel ander blad in datzelfde tijdvak in ruimte Y. | R: zoek per tijdvak naar dubbel geplaatste namen. |
| C-05 | "Er was verder niemand"-claims worden door geen enkel ander blad tegengesproken. | Grep alle exclusiviteitsformuleringen; toets elk tegen de betreffende cel in R. |
| C-06 | Verplaatsingen zijn fysiek haalbaar: tussen twee locaties zit genoeg tijd gegeven de plattegrond in de introductie. | T: bereken per speler het verschil tussen einde vorige en begin volgende blok; markeer overgangen van 0 minuten tussen niet-aangrenzende ruimtes. |
| C-07 | Geen onverklaarde gaten in de tijdlijn van een speler binnen het kritieke venster. | T: markeer lege cellen tussen B-ondergrens en B-bovengrens; elk gat moet ofwel expliciet "alleen" zijn ofwel bedoeld leeg voor de dader. |
| C-08 | Overlappende gebeurtenissen zijn onderling verenigbaar (twee gebeurtenissen in hetzelfde tijdvak sluiten elkaar niet uit qua deelnemers). | Sorteer A op tijdstip; toets per tijdstip of alle deelnemers volgens T beschikbaar zijn. |
| C-09 | Het slachtoffer heeft zelf een sluitende, niet-tegenstrijdige tijdlijn voor zover andere bladen die beschrijven. | Maak een aparte T-rij voor het slachtoffer, uitsluitend gevuld uit andermans bladen. |
| C-10 | Elk hoorbaar signaal (geluid, roep, klap, telefoon) is verenigbaar met de positie van elke waarnemer op dat moment. | A + R: per signaal alle waarnemers opzoeken en hun ruimte controleren tegen de plattegrond. |
| C-11 | De reconstructie in het oplossingsbestand is tijdlijn-identiek aan het daderblad en aan alle getuigenbladen. | Leg de reconstructie naast T; noteer elk tijdstip dat afwijkt. |
| C-12 | Het collectieve slotmoment (iedereen samen) wordt door alle bladen op hetzelfde tijdstip genoemd. | Grep het slottijdstip in alle bestanden en vergelijk. |

## 2. Oplosbaarheid

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-13 | De dader is afleidbaar uit uitsluitend de introductie plus de niet-daderbladen. | Voer een **blinde reconstructie** uit: leg het daderblad en het oplossingsbestand weg, bouw T/W opnieuw en probeer de eliminatie te voltooien. |
| C-14 | Het beslissende moment M is uit niet-daderbladen vast te stellen (een gebeurtenis die het venster verankert). | Zoek in A naar het ankersignaal; controleer dat minstens één bron ervan geen daderblad is. |
| C-15 | Het moordvenster heeft zowel een aantoonbare ondergrens ("slachtoffer leefde nog") als bovengrens. | Zoek beide grenzen in A en noteer bron per grens. |
| C-16 | De eliminatie is sluitend: precies één verdachte blijft over na toepassing van dekking op M. | Maak een dekkingstabel: per speler alle externe getuigen op M; tel de spelers met nul externe getuigen. |
| C-17 | Bij de eliminatie tellen eigen verklaringen van de verdachte niet mee; ook dan blijft precies één speler over. | Herhaal C-16 met alle zelfverklaringen geschrapt (adversariële modus). |
| C-18 | Geen bewijsstap leunt op een bekentenis, verspreking of vrijwillige onthulling van de dader. | Streep in de bewijsketen van het oplossingsbestand elke stap door met het daderblad als enige bron; de keten moet blijven staan. |
| C-19 | Naast negatieve eliminatie is er een positieve keten naar de dader (motief + middel + gelegenheid). | Tel in het oplossingsbestand de ketenstappen en controleer per stap de bron in een niet-daderblad. |
| C-20 | Elke ketenstap is aan minstens één concreet citaat uit een niet-daderblad te koppelen. | Maak een tabel ketenstap → bestandsnaam → letterlijk citaat; lege regels = FAIL. |
| C-21 | Er is geen tweede speler die met dezelfde informatie even goed als dader past. | Herhaal de positieve keten voor elke andere speler; noteer hoeveel stappen blijven kloppen. |
| C-22 | De oplossing vereist geen kennis die alleen in het oplossingsbestand staat. | Markeer elk feit in het oplossingsbestand dat in geen enkel spelersbestand voorkomt. |
| C-23 | De vraag naar het motief is beantwoordbaar zonder het daderblad. | Zoek in andermans bladen naar de vermelding van de relatie/aanleiding tussen dader en slachtoffer. |

## 3. Eerlijkheid en dekking

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-24 | Elke onschuldige speler heeft op M minstens één externe getuige. | Dekkingstabel uit C-16; elke rij behalve de dader moet ≥1 externe naam bevatten. |
| C-25 | Geen dragende conclusie hangt aan één enkele bron: verwijder één willekeurig niet-daderblad en de zaak blijft oplosbaar of faalt aantoonbaar gecontroleerd. | Voer een **weglaattest** uit voor elk niet-daderblad afzonderlijk; noteer per weglating of C-16/C-17 nog PASS is. |
| C-26 | Wederzijds-alibiparen (twee spelers die alleen elkaar dekken) zijn extern verankerd door een derde waarneming of tijdstempel. | W: zoek paren die uitsluitend elkaar noemen op M; controleer of een derde blad het paar op of vlak na M plaatst. |
| C-27 | Het aantal wederzijds-alibiparen zonder externe verankering is nul. | Tel de FAIL-gevallen uit C-26. |
| C-28 | Er bestaat geen speler die aantoonbaar onschuldig is puur door zijn eigen blad, zonder externe steun. | Per speler: schrap zelfverklaringen en controleer of dekking overblijft. |
| C-29 | Alle spelers hebben een vergelijkbare informatiedichtheid (aantal bruikbare waarnemingen), zodat niemand louter toeschouwer is. | Tel per blad de items onder de weet-/waarnemingsrubriek; markeer uitschieters van meer dan factor twee ten opzichte van de mediaan. |
| C-30 | De dader kan niet al in de eerste minuten door één triviaal detail worden ontmaskerd. | Voer een **snelle-ontmaskeringstest**: is er één zin op één blad die alleen bij de dader past? Zo ja, controleer of er nog ambiguïteit is. |
| C-31 | De belastende waarneming(en) over de dader zijn verdeeld over meerdere bladen, niet geconcentreerd bij één speler. | A: tel bronnen per belastende aanwijzing. |

## 4. Dangling clues

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-32 | Elke aanwijzing in A heeft een ingevulde kolom "verklaard door". | Loop A door; lege cellen = FAIL. |
| C-33 | Elke waarneming heeft een oorzaak elders in het materiaal (iemand veroorzaakte wat er is gezien of gehoord). | A: koppel elke waarneming aan een handeling op een ander blad of in het oplossingsbestand. |
| C-34 | Elk genoemd rekwisiet/voorwerp heeft een rol of is expliciet gemarkeerd als bewust ongebruikt decor. | Grep alle zelfstandig genoemde voorwerpen; toets tegen A. |
| C-35 | Elk ontbrekend of verdwenen object heeft een verklaring in het oplossingsbestand. | Zoek in de bestanden naar formuleringen over ontbreken/niet gevonden; controleer de oplossing. |
| C-36 | Elk expliciet genoemd tijdstip komt in minstens één andere context terug of is als geïsoleerd detail verantwoord. | Grep alle tijdstempels; tel voorkomens per tijdstip. |
| C-37 | Geen aanwijzing wijst naar een gebeurtenis die nergens in het materiaal bestaat (loze verwijzing). | A: markeer verwijzingen naar personen, plaatsen of gebeurtenissen zonder tegenhanger. |
| C-38 | Aanwijzingen die bewust misleiden zijn in het oplossingsbestand als zodanig benoemd. | Vergelijk de misleidende items uit A met de rode-haringlijst in de oplossing. |

## 5. Rode haringen

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-39 | Elke verdachte behalve de dader is met materiaal uit het spel te ontkrachten. | Maak per speler een ontkrachtingsregel: verdenking → weerlegging → bron. |
| C-40 | Geen rode haring is zo sterk dat hij ook na volledige eliminatie blijft staan. | Test: leidt de haring tot een even complete keten als C-19? Zo ja, FAIL. |
| C-41 | Geen rode haring is zo zwak dat hij binnen de eerste ronde verdampt (elke speler heeft minstens één moment waarop hij plausibel verdacht is). | Per speler: bestaat er een verdachtmakend feit dat door een ander blad bekend is? |
| C-42 | Motief en gebrek aan dekking vallen bij geen enkele onschuldige samen op M. | Kruis de motieflijst tegen de dekkingstabel; een speler met motief én nul dekking op M = FAIL. |
| C-43 | De dader heeft niet als enige een motief; er zijn meerdere concurrerende motieven. | Tel spelers met een motief jegens het slachtoffer; minder dan drie = FAIL. |
| C-44 | De dader valt niet op door een afwijkende bladstructuur, lengte of formulering. | Vergelijk koppenstructuur, regelaantal en toon van alle bladen; noteer afwijkingen. |
| C-45 | De haringen zijn over verschillende soorten verdenking verdeeld (geld, relatie, gelegenheid, gedrag), niet allemaal van één type. | Categoriseer elke haring en tel per categorie. |

## 6. Geheimen en speelbaarheid

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-46 | Elke speler heeft minstens één eigen geheim met reëel sociaal gewicht (iets dat schade doet als het uitkomt). | Tabel speler → geheim → gevolg bij onthulling; ontbrekend gevolg = FAIL. |
| C-47 | Elk geheim staat onder druk: minstens één andere speler kan het aanroeren of raakt eraan. | Kruistabel geheim × wie weet ervan; nul verwijzingen = FAIL. |
| C-48 | Geen geheim is al volledig bij een ander bekend zonder dat het materiaal daar een reden voor geeft. | Voor elk geheim: vergelijk de formulering bij eigenaar en bij de wetende partij; volledige overlap zonder verklaring = FAIL. |
| C-49 | Er is minstens één belangenconflict waarbij een speler moet kiezen tussen zijn geheim beschermen en de zaak helpen oplossen. | Zoek per blad naar een geheim dat een alibi of waarneming blokkeert. |
| C-50 | Geen speler hoeft zijn geheim te onthullen om de zaak oplosbaar te maken. | Weglaattest: schrap alle geheimen uit A en herhaal C-16/C-19. |
| C-51 | Elke speler heeft een doelstelling die actief spelen uitlokt (niet alleen "vertel de waarheid"). | Lees de doelrubriek van elk blad; passieve doelen zonder spanning = FAIL. |

## 7. Regelconformiteit

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-52 | Waarnemingen op de bladen zijn als harde feiten geformuleerd, niet als vermoedens, waar de regels dat vereisen. | Grep op verzachtende formuleringen (dacht, misschien, meende) in waarnemingsrubrieken en toets tegen de regeltekst. |
| C-53 | De liegregels in de introductie zijn consistent met wat de bladen spelers toestaan. | Leg de liegparagraaf naast de lieginstructies op elk blad; noteer verschillen. |
| C-54 | De dader kan binnen de regels liegen: er is minstens één toegestane leugen die hem dekt op M. | Simuleer: welke uitspraak mag de dader doen die niet door een ander blad direct wordt weerlegd? |
| C-55 | De dader hoeft geen verboden leugen (verzonnen getuige, gesprek of waarneming) te vertellen om te overleven. | Test C-54: als elke overlevende verklaring een verboden verzinsel vereist, FAIL. |
| C-56 | Geen enkel blad verplicht een speler tot een handeling die de introductie verbiedt. | Vergelijk de doel- en instructierubrieken met de regelparagraaf. |
| C-57 | De introductie belooft geen informatiebronnen die niet bestaan (spelleider, extra rondes, nieuwe aanwijzingen, rekwisieten). | Grep de introductie op beloofde elementen en vink af tegen de aanwezige bestanden. |
| C-58 | Wat de introductie als vaststaand feit meldt, wordt door geen enkel rolblad tegengesproken. | Maak een lijst introductiefeiten; grep elk feit in alle bladen. |

## 8. Hygiëne

| ID | Regel | Controlemethode |
|----|-------|-----------------|
| C-59 | Het aantal rolbladen komt overeen met het aantal spelers dat de introductie noemt. | Tel bestanden; vergelijk met het getal in de introductie en in de oplossing. |
| C-60 | Alle genoemde personen (spelers plus slachtoffer plus derden) komen in de introductie of een blad voor; geen weespersonages. | Grep alle hoofdletternamen over alle bestanden en kruis af. |
| C-61 | Het aantal en de namen van ruimtes zijn overal gelijk; geen blad speelt in een ruimte die de plattegrond niet kent. | Extraheer alle ruimtenamen per bestand en vergelijk met de introductie. |
| C-62 | Namen zijn overal identiek gespeld (inclusief achternamen en verkleinvormen). | Genereer een gesorteerde unieke namenlijst per bestand en diff. |
| C-63 | Tijdnotatie is uniform (zelfde formaat, zelfde 12-/24-uursconventie, zelfde scheidingsteken). | Grep alle tijdpatronen; tel afwijkende formaten. |
| C-64 | Bestandsnamen, koppen en versieaanduidingen komen overeen en verwijzen alle naar dezelfde versie. | Vergelijk de versietekst in elke kop met de bestandsnamen. |
| C-65 | Er zijn geen resten van een vorige versie (oude namen, oude tijden, oude ruimtes, doorgehaalde plotlijnen). | Grep op namen en tijdstippen die maar in één bestand voorkomen; controleer de git-historie of eerdere versiemappen als die er zijn. |
| C-66 | Verwijzingen naar andere bestanden (bijvoorbeeld het oplossingsbestand) kloppen exact met de werkelijke bestandsnamen. | Grep op bestandsnaamverwijzingen en vergelijk met de directorylijst. |
| C-67 | De koppenstructuur van de rolbladen is uniform, zodat spelers dezelfde rubrieken vinden. | Extraheer alle kopregels per blad en vergelijk de sets. |

---

## Werkwijze voor de auditor

### Volgorde
1. **Voorbereiding.** Lees eerst de introductie, dan alle rolbladen, dan pas het oplossingsbestand. Bouw T, R, W en A. Leg M, en de onder- en bovengrens van het venster vast.
2. **Hygiëne (C-59 t/m C-67).** Doe dit eerst: spelfouten in namen, ruimtes of tijden vervuilen alle latere matrices.
3. **Interne consistentie (C-01 t/m C-12).** Zonder een kloppende tijdlijn is de rest niet te beoordelen.
4. **Regelconformiteit (C-52 t/m C-58).** Stel vast wat als feit telt en wat gelogen mag worden, vóór je bewijs weegt.
5. **Oplosbaarheid (C-13 t/m C-23).** Voer de blinde reconstructie uit vóórdat je het oplossingsbestand als leidraad gebruikt; noteer je eigen conclusie en pas daarna vergelijken.
6. **Eerlijkheid en dekking (C-24 t/m C-31).** Inclusief de weglaattest per blad.
7. **Rode haringen (C-39 t/m C-45)** en **dangling clues (C-32 t/m C-38)**.
8. **Geheimen en speelbaarheid (C-46 t/m C-51).** Als laatste, want deze regels raken de speelervaring en niet de logische houdbaarheid.

Werk elke categorie volledig af voordat je doorgaat. Herbouw T, R, W en A na elke reparatie: één tijdswijziging kan tientallen regels omkeren.

### Verplicht rapportageformat
Rapporteer per regel-ID, in volgorde van ID, één blok:

```
C-xx  [PASS | FAIL | N.V.T.]
Bewijs: <bestandsnaam> — "<letterlijk citaat of celverwijzing uit T/R/W/A>"
        (bij meerdere bronnen: één regel per bron)
Ernst:  [BLOKKEREND | ERNSTIG | KLEIN]        (alleen bij FAIL)
Reparatie: <concreet voorstel: welk bestand, welke zin, welke nieuwe formulering of tijd>
```

Regels:
- Een **PASS** vermeldt óók bewijs (welke matrix of welk citaat de uitspraak draagt). PASS zonder bewijs is zelf een auditfout.
- **N.V.T.** mag alleen met een reden ("het spel kent geen rekwisieten").
- Ernstgraden:
  - **BLOKKEREND** — het spel is onspeelbaar of onoplosbaar: de dader is niet af te leiden, twee daders passen even goed, of een harde tegenstrijdigheid in de tijdlijn.
  - **ERNSTIG** — het spel is speelbaar maar oneerlijk of gammel: een onschuldige zonder dekking, een dragende conclusie op één bron, een niet te ontkrachten rode haring.
  - **KLEIN** — cosmetisch of hygiënisch: spelling, notatie, een los detail zonder gevolg.
- **Reparatie** is altijd concreet en uitvoerbaar: benoem bestand, plaats en de voorgestelde tekst. "Beter uitwerken" is geen reparatievoorstel.

Sluit af met een **samenvattingstabel**: aantal PASS / FAIL / N.V.T. per categorie, het totaal aantal BLOKKEREND en ERNSTIG, en een eindoordeel:
**VRIJGEGEVEN** (geen FAIL boven KLEIN), **VRIJGEGEVEN MET REPARATIES** (alleen KLEIN en ERNSTIG) of **GEBLOKKEERD** (minstens één BLOKKEREND).
