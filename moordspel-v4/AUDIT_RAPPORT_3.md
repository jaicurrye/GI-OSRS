# AUDIT_RAPPORT_3 — derde auditronde op versie 4

**Auditor:** onafhankelijke controle, uitgevoerd op de huidige inhoud van
`START_HIER.md`, `SPELER_1_BRAM.md` t/m `SPELER_8_FLEUR.md` en `NA_AFLOOP_OPENEN.md`.

**Werkwijze.** De vier voorgeschreven werkstukken (T = tijdlijnmatrix, R = ruimtebezettings-
tabel, W = wederkerigheidsmatrix, A = aanwijzingenregister) zijn volledig opnieuw en
onafhankelijk opgebouwd vanaf de huidige bestanden, in de volgorde van de sectie "Werkwijze
voor de auditor": eerst introductie, dan de acht rolbladen, dan pas het oplossingsbestand.
De blinde reconstructie (C-13/C-16/C-17) is uitgevoerd met het daderblad én het
oplossingsbestand weggelegd, en daarna herhaald met alle zelfverklaringen geschrapt.
`AUDIT_RAPPORT.md` en `AUDIT_RAPPORT_2.md` zijn pas na afronding van alle eigen werkstukken
en oordelen gelezen, uitsluitend om te controleren of de daarin voorgestelde reparaties zijn
doorgevoerd. Geen oordeel in dit rapport is uit die rapporten overgenomen.

**Uitzondering op instructie van de eigenaar.** C-25, C-26 en C-27 (de weglaattest en de
externe verankering van wederzijds-alibiparen) zijn bewust losgelaten omdat wederzijdse
afhankelijkheid tussen spelers de bedoelde eindfase van het spel is. Zij zijn beoordeeld als
**N.V.T. (bewust losgelaten door de eigenaar)** en tellen niet als FAIL. Alle overige 64
regels gelden onverkort.

---

## 0. Vastgelegde ankers

**M — het beslissende moment.** 23:12. Bron voor deze vaststelling zonder daderblad: de
harde doffe klap uit de richting van de bibliotheek, gehoord door Daan en Sanne samen vanuit
de serre en onafhankelijk door Bram vanuit de keuken, met Noor en Lucas als getuigen van
Brams reactie.

**B — bewijsbare grenzen van het moordvenster, uitsluitend uit niet-daderbladen.**
- Ondergrens ~22:59: `SPELER_5_DAAN.md` — "hoorde je Kees binnen praten … Je hoorde **geen
  tweede stem** … het klonk alsof hij aan de telefoon was. Kees leefde op dat moment dus nog."
  Onafhankelijk ondersteund door `SPELER_7_MILAN.md` ("Kees leefde toen jij hem rond **22:58**
  achterliet") en `SPELER_2_NOOR.md` (telefoon niet in de jas om 22:00, dus bij zich).
- Bovengrens 23:12 (de klap); harde uiterste bovengrens 00:50 (vondst, `START_HIER.md`).

**Kern van T (kritieke venster 22:45–23:25), per speler met bron:**

| Speler | 22:45–23:00 | 23:00–23:12 | 23:12–23:20 | 23:20–23:25 |
|---|---|---|---|---|
| Bram | hal 22:50–22:52 → keuken 22:55 (eigen; Noor, Lucas) | keuken (Noor, Lucas) | keuken (Noor, Lucas) | salon (Lucas) |
| Noor | keuken v.a. 22:50 (Lucas) | keuken (Lucas, Bram) | keuken (Lucas, Bram) | eetkamer (Fleur, Daan, Sanne) |
| Lucas | keuken v.a. 22:50 (Noor) | keuken (Noor, Bram) | keuken (Noor, Bram) | salon (Bram) |
| Sanne | kamer tot 23:00 (eigen, "alleen") | serre v.a. 23:02 (Daan) | serre (Daan) | eetkamer (Noor, Fleur, Daan) |
| Daan | salon tot 22:58 (eigen, "alleen") | serre v.a. 23:02 (Sanne) | serre (Sanne) | eetkamer + gezien door Lucas |
| Milan | bibliotheek tot 22:58 → boven (eigen) | boven; 23:11–23:14 overloop (Fleur) | boven (eigen) | hal → salon 23:25 (Noor, Bram, Lucas) |
| Fleur | kamer boven (eigen, "alleen") | kamer; 23:11–23:14 overloop (Milan) | kamer (eigen) | eetkamer (Noor, Daan, Sanne) |
| Iris | **geen externe bron** | **geen externe bron** | **geen externe bron** | boven aan de trap 23:20 (Noor), 23:22 (Milan) |
| Kees | bibliotheek (Milan tot 22:58; Daan ~22:59) | bibliotheek (Daan ~22:59) | — | — |

**W — wederkerigheidsmatrix:** 26 gedeelde intervallen, alle wederkerig ingevuld, alle met
verschil 0 minuten (zie C-02/C-03).

**A — aanwijzingenregister:** 27 items, alle met ingevulde kolom "verklaard door" (zie C-32).

---

## 1. Beoordeling per regel

### Categorie 1 — Interne consistentie

```
C-01  PASS
Bewijs: T, alle 22 tijdvakken van 20:00 tot 23:50, acht spelersrijen plus slachtofferrij:
        geen enkele cel bevat meer dan één locatie. Krapste controle op de kolom 23:10–23:15:
        SPELER_1_BRAM.md/SPELER_2_NOOR.md/SPELER_3_LUCAS.md plaatsen drie namen in de keuken,
        SPELER_4_SANNE.md/SPELER_5_DAAN.md twee in de serre, SPELER_7_MILAN.md/SPELER_8_FLEUR.md
        twee op de overloop, SPELER_6_IRIS.md één in de bibliotheek — acht namen, vier ruimtes,
        geen dubbeling.
        Kanttekening (geen dubbele locatie, wel een reistijdkwestie): SPELER_8_FLEUR.md laat het
        oranjerieblok om 22:45 eindigen en het kamerblok om 22:45 beginnen. Blokgrenzen die
        elkaar raken worden in het hele pakket als geldige overgang gebruikt; de kwestie is
        daarom als reistijdprobleem onder C-06 opgenomen en niet hier dubbel geteld.
```

```
C-02  PASS
Bewijs: W — alle 26 cellen met een gedeelde waarneming hebben een verenigbaar tegenveld.
        Steekproef op de dragende cellen:
        SPELER_7_MILAN.md — "Van **23:11 tot 23:14** stond je onafgebroken met Fleur te praten op
        de overloop." ↔ SPELER_8_FLEUR.md — "Van **23:11 tot 23:14** stond je onafgebroken met
        Milan te praten op de overloop."
        SPELER_4_SANNE.md — "Daan was van **23:02 tot 23:45** onafgebroken bij jou." ↔
        SPELER_5_DAAN.md — "Sanne was van **23:02 tot 23:45** onafgebroken bij jou."
        SPELER_6_IRIS.md — "Rond **23:22** loopt Milan langs je de trap af." ↔ SPELER_7_MILAN.md —
        "Toen je rond **23:22** de trap afliep, stond Iris nog boven aan de trap."
        SPELER_5_DAAN.md — "je kapt het af met: 'Dan laten we het hierbij.'" ↔ SPELER_4_SANNE.md —
        "In de serre probeerde je Daan te laten vertellen waarover hij en Kees ruzie hadden; hij
        hield het af met: 'Dan laten we het hierbij.'"
        Eenzijdige waarnemingen met leeg maar niet-tegenstrijdig tegenveld (toegestaan onder de
        regel): Bram ziet Sanne om 22:35 de bibliotheek ingaan; Daan ziet Noor om 22:05 bij de
        kapstok; Sanne ziet Lucas om 21:40 met de envelop; Lucas ziet Daan en Sanne om 23:20 uit
        de serre komen; Noor ziet Iris om 23:20. In alle vijf gevallen kón de waargenomene het
        niet weten en spreekt zijn blad de waarneming nergens tegen.
```

```
C-03  PASS
Bewijs: W, kolom "verschil in minuten" — alle 26 paren staan op 0. Gecontroleerde paren onder
        meer: salon 20:20–20:45 (Bram/Milan), salon 20:00–20:30 (Noor/Sanne), keuken 20:20–20:50
        (Lucas/Iris), eetkamer 21:00–21:25 (Noor/Lucas), serre 21:30–22:10 (Milan/Fleur), terras
        21:50–22:10 (Lucas/Sanne), terras 22:15–22:40 (Noor/Daan), oranjerie 22:15–22:45
        (Bram/Fleur), keuken 22:50–23:20 (Noor/Lucas), keuken 22:55–23:20 (Bram; SPELER_2_NOOR.md
        "Rond **22:55** komt Bram erbij; hij blijft tot ongeveer 23:20"), overloop 23:11–23:14
        (Milan/Fleur), serre 23:02–23:20 (Sanne/Daan), eetkamer 23:20–23:45 (Noor/Fleur/Daan/
        Sanne, vier bladen identiek), salon 23:20–23:45 (Bram/Lucas), salon 23:25–23:50
        (Bram/Lucas/Milan/Iris).
```

```
C-04  PASS
Bewijs: R — geen naam staat in enig tijdvak in twee ruimtes. Dichtste kolommen:
        22:35–22:40 (bibliotheek: Sanne; keuken: Iris; oranjerie: Bram en Fleur; terras: Noor en
        Daan; kamer: Lucas en Milan) en 23:20–23:25 (salon: Bram, Lucas; eetkamer: Noor, Sanne,
        Daan, Fleur; hal: Milan v.a. 23:22; boven aan de trap: Iris).
        Grenscontrole 23:22: SPELER_2_NOOR.md — "terwijl je bij de eetkamerdeur stond" is als
        eetkamer geboekt en botst dus niet met SPELER_8_FLEUR.md/SPELER_4_SANNE.md/SPELER_5_DAAN.md
        "onafgebroken bij jou in de eetkamer".
```

```
C-05  PASS
Bewijs: Zes exclusiviteitsclaims, elk getoetst tegen de betreffende cel in R:
        SPELER_2_NOOR.md en SPELER_5_DAAN.md — "**22:15–22:40:** … Verder was daar niemand."
        (R, terras 22:15–22:40: alleen die twee).
        SPELER_6_IRIS.md — "**22:35–22:42:** je bent alleen in de keuken. Er is verder niemand."
        (R, keuken 22:35–22:42: leeg op Iris na; Lucas en Noor komen pas 22:50 binnen).
        SPELER_4_SANNE.md — "Kees kwam tijdens jouw zoektocht niet binnen. De bibliotheek was
        leeg." (R, bibliotheek 22:35–22:40: alleen Sanne).
        SPELER_5_DAAN.md — "**22:47–22:58:** alleen in de salon." (R, salon: leeg).
        SPELER_3_LUCAS.md — "Daarvoor zaten Bram en jij daar alleen." (R, salon 23:20–23:25:
        alleen Bram en Lucas).
        SPELER_7_MILAN.md — "Hij was toen alleen in de bibliotheek." (R, 22:58: alleen Kees).
        De eerder onhoudbare negatieve claim over de overloop is vervangen door een niet-negatieve
        formulering: SPELER_6_IRIS.md — "Je hoort af en toe iemand over de overloop lopen, maar je
        ziet niemand." Dat is verenigbaar met R (Milan omhoog ~23:00, Sanne omlaag ~23:00–23:01).
        De blokaanduidingen "alleen op je kamer" zijn geen exclusiviteitsclaims over een ruimte
        waar anderen worden geplaatst; SPELER_3_LUCAS.md "**21:30–21:45:** alleen in de bijkeuken"
        botst niet met SPELER_4_SANNE.md "Rond **21:40** liep je langs de bijkeuken", omdat Sanne
        langsloopt en de ruimte niet betreedt.
```

```
C-06  FAIL
Bewijs: T, kolom "overgangen", rij Fleur.
        SPELER_8_FLEUR.md — "- **22:15–22:45:** stiekem roken met Bram bij de oranjerie." direct
        gevolgd door "- **22:45–23:11:** alleen op je kamer boven."
        Dat is een overgang van nul minuten van de oranjerie (buiten, aan het eind van het
        grindpad) naar een gastenkamer op de eerste verdieping. Dezelfde route kost op het blad
        van haar metgezel aantoonbaar meer tijd: SPELER_1_BRAM.md — "**22:50:** je loopt over het
        grindpad terug naar het huis en gaat via de hal naar binnen", dus alleen al oranjerie →
        hal duurt vijf minuten; Fleur moet daarna ook nog de trap op.
        Alle overige overgangen in T hebben marge: Iris keuken 22:42 → kamer boven 22:47 (5 min);
        Milan bibliotheek 22:58 → boven 23:00 (2 min); Daan salon 22:58 → bibliotheekdeur ~22:59
        → serre 23:02 (4 min); Sanne kamer boven 23:00 → serre 23:02 (2 min, krapste geldige
        overgang); Bram oranjerie 22:45 → grindpad 22:50 → hal 22:52 → keuken 22:55 (10 min).
        Kanttekening bij de methode: START_HIER.md geeft een ruimtelijst en geen aangrenzings-
        schema. De toets is daarom uitgevoerd op de wel gegeven relaties (bibliotheekraam op de
        tuinzijde met zicht op grindpad en oranjerie; serre–hal–bibliotheek volgens
        SPELER_4_SANNE.md "vanuit de serre, door de hal heen") en op de reistijden die de bladen
        zelf vaststellen.
Ernst:  KLEIN
Reparatie: SPELER_8_FLEUR.md, rubriek "Jouw avond": vervang
        "- **22:45–23:11:** alleen op je kamer boven."
        door
        "- **22:50:** je loopt over het grindpad terug en gaat via de hal naar binnen.
         - **22:52–23:11:** alleen op je kamer boven."
        Daarmee blijft het gat tussen 22:52 en 23:11 expliciet als "alleen" gemarkeerd (C-07
        blijft PASS), verandert er niets aan de dekking op M en sluit haar route aan op de
        reistijd die SPELER_1_BRAM.md voor dezelfde wandeling geeft.
```

```
C-07  PASS
Bewijs: T, kolommen tussen B-ondergrens (22:59) en B-bovengrens (23:12): geen enkele lege cel.
        Elk gat in dat venster is ofwel gedekt ofwel expliciet als "alleen" gemarkeerd:
        SPELER_8_FLEUR.md — "**22:45–23:11:** alleen op je kamer boven." (eerder onbenoemd, nu
        expliciet); SPELER_7_MILAN.md — "**23:00–23:22:** je bent boven."; SPELER_4_SANNE.md —
        "**22:45–23:00:** alleen op je kamer, deur dicht."; SPELER_5_DAAN.md — "**22:47–22:58:**
        alleen in de salon."; SPELER_6_IRIS.md is bedoeld leeg voor de dader.
        Het eerdere gat Milan 23:22–23:25 is gedicht: SPELER_7_MILAN.md — "Je blijft even in de
        hal staan en loopt om 23:25 samen met Iris de salon in."
        Buiten het venster resteert één ongemarkeerd gat (Bram, Lucas, Noor, Sanne, Daan en Fleur
        tussen 23:45 en 23:50); dat valt ruim na de bovengrens en raakt de eliminatie niet.
```

```
C-08  PASS
Bewijs: A gesorteerd op tijdstip; per tijdstip zijn alle deelnemers volgens T beschikbaar.
        Zwaarste knooppunt is 23:20, waar vijf gebeurtenissen samenvallen: Bram en Lucas verlaten
        de keuken richting salon, Noor verlaat de keuken richting eetkamer, Daan en Sanne komen
        uit de serre en steken de hal over, Lucas ziet dat vanuit de salon, en Noor ziet Iris
        boven aan de trap. T plaatst alle acht namen op verenigbare posities; geen enkel blad
        claimt op dat moment een lege hal.
        SPELER_2_NOOR.md — "Daan en Sanne komen vrijwel gelijktijdig binnen" bevestigt onafhankelijk
        de oversteek die SPELER_3_LUCAS.md waarneemt.
        Tweede knooppunt 23:11–23:15: Milan en Fleur op de overloop, Daan en Sanne in de serre,
        drie spelers in de keuken, Iris in de bibliotheek — deelnemers sluiten elkaar nergens uit.
```

```
C-09  PASS
Bewijs: Aparte T-rij voor Kees, uitsluitend gevuld uit andermans bladen, is niet-tegenstrijdig:
        21:00–21:15 serre (SPELER_1_BRAM.md; SPELER_5_DAAN.md "Rond **21:10** … hoorde je Bram en
        Kees in de serre hard praten"), ~21:50 hal (SPELER_5_DAAN.md), 22:35–22:40 níet in de
        bibliotheek (SPELER_4_SANNE.md "De bibliotheek was leeg"), 22:50–22:58 bibliotheek
        (SPELER_7_MILAN.md), ~22:52 bibliotheek (SPELER_1_BRAM.md "hoorde je Kees vanuit de
        bibliotheek hard zeggen: 'Dat meen je niet.'"), ~22:59 bibliotheek, telefonerend
        (SPELER_5_DAAN.md), 00:50 gevonden in de bibliotheek (START_HIER.md).
        De onbeschreven perioden (20:00–21:00, 21:15–21:50, 22:00–22:50) bevatten geen enkele
        claim die met een andere botst.
```

```
C-10  PASS
Bewijs: A + R, per signaal alle waarnemers en hun ruimte:
        21:00–21:15 luide ruzie in de serre — waarnemer Daan komt van buiten naar binnen
        (SPELER_5_DAAN.md); R plaatst niemand anders in de aangrenzende ruimtes.
        ~22:52 "Dat meen je niet." uit de bibliotheek — waarnemer Bram staat volgens zijn eigen
        blok in de hal; R plaatst Noor en Lucas in de keuken (buiten gehoorsafstand van een
        enkele uitroep) en verder niemand in de hal.
        ~22:59 Kees telefonerend — waarnemer Daan loopt langs de bibliotheekdeur; R plaatst
        niemand anders in de hal.
        23:12 de klap — waarnemers Daan en Sanne in de serre ("door de hal heen"), Bram in de
        keuken; niet-waarnemers zijn alle expliciet verklaard: SPELER_3_LUCAS.md "Jij hoorde zelf
        niets; de afzuigkap stond aan", SPELER_2_NOOR.md "Zelf hoorde je niets",
        SPELER_7_MILAN.md en SPELER_8_FLEUR.md identiek "Boven hoorde je niets bijzonders; de
        deuren op de overloop stonden dicht en jullie stonden te praten."
        22:45–23:05 voetstappen op de overloop — waarnemers Sanne en Iris, beiden op een
        kamer boven; R levert de veroorzakers (zie C-33).
        23:15 telefoongesprek — waarnemer Fleur op haar kamer; R plaatst het toestel bij de dader.
        Alle posities zijn verenigbaar met de plattegrond; geen waarnemer staat op een plek waar
        het signaal hem niet had kunnen bereiken.
```

```
C-11  PASS
Bewijs: Reconstructie naast T gelegd, elk genoemd tijdstip getoetst; geen enkele afwijking.
        NA_AFLOOP_OPENEN.md — "Milan verlaat Kees rond 22:58 levend in de bibliotheek" ≡
        SPELER_7_MILAN.md/SPELER_5_DAAN.md; "Iris komt rond 23:05 van boven naar beneden" ≡
        SPELER_6_IRIS.md; "Rond 23:12 slaat zij Kees" ≡ de drie klapwaarnemingen; "Om 23:15 belt
        Fleur naar die telefoon" ≡ SPELER_8_FLEUR.md; "Noor ziet haar rond 23:20 boven aan de
        trap met het opgevouwen vest" ≡ SPELER_2_NOOR.md woordelijk.
        Ook de eliminatiesectie is tijdlijn-identiek: "Fleur bevestigt hem van 23:11 tot 23:14
        onafgebroken op de overloop boven — dat venster omvat het moment van de klap" ≡ W.
```

```
C-12  PASS
Bewijs: Grep op het slottijdstip levert in alle tien bestanden 23:50 op, zonder afwijking:
        START_HIER.md — "Vanaf ongeveer **23:50** zit de hele groep bij elkaar in de salon."
        SPELER_2_NOOR.md, SPELER_4_SANNE.md, SPELER_5_DAAN.md, SPELER_8_FLEUR.md — identieke zin
        inclusief "in de salon"; SPELER_1_BRAM.md, SPELER_3_LUCAS.md, SPELER_7_MILAN.md — "Vanaf
        ongeveer **23:50** zit de hele groep bij elkaar." (minder specifiek, niet strijdig);
        SPELER_6_IRIS.md — "**23:25–23:50:** je zit in de salon … Daarna blijven jullie tussen de
        anderen."
        De eerdere afwijking "in de salon en de eetkamer" in START_HIER.md is verdwenen.
```

### Categorie 2 — Oplosbaarheid

```
C-13  PASS
Bewijs: Blinde reconstructie, uitgevoerd met SPELER_6_IRIS.md en NA_AFLOOP_OPENEN.md weggelegd.
        Uit de zeven overige bladen volgt: een verankerd moment (drie waarnemers, twee ruimtes),
        een dekkingstabel waarin zeven van de acht spelers op dat moment minstens één externe
        getuige hebben, en één speler die door geen enkel blad tussen 22:45 en 23:20 ergens wordt
        geplaatst. De eigen conclusie van deze audit is vóór het openen van het oplossingsbestand
        genoteerd en komt overeen met NA_AFLOOP_OPENEN.md.
        Controle op de volledigheid van de afwezigheid: grep op de daadnaam in de zeven
        niet-daderbladen levert buiten 20:45 (SPELER_3_LUCAS.md, imitatie) en 23:20/23:22/23:25
        (SPELER_2_NOOR.md, SPELER_7_MILAN.md, SPELER_1_BRAM.md, SPELER_3_LUCAS.md) geen enkele
        plaatsbepaling op.
```

```
C-14  PASS
Bewijs: Het ankersignaal in A is de klap van 23:12. Drie van de vier bronnen zijn niet-daderbladen:
        SPELER_5_DAAN.md — "Rond **23:12** hoorde jij samen met Sanne vanuit de serre een harde,
        doffe klap uit de richting van de bibliotheek."
        SPELER_4_SANNE.md — "Rond **23:12** hoorde je vanuit de serre, door de hal heen, een harde
        doffe klap uit de richting van de bibliotheek."
        SPELER_1_BRAM.md — "Rond **23:12** hoorde je vanuit de keuken heel kort een dof geluid."
        Met tijdstempelbevestiging door twee verdere bladen: SPELER_2_NOOR.md en SPELER_3_LUCAS.md
        — "Rond **23:12** keek Bram in de keuken opeens op, alsof hij iets hoorde."
```

```
C-15  PASS
Bewijs: Beide grenzen staan in A met een niet-daderbron.
        Ondergrens: SPELER_5_DAAN.md — "Kees leefde op dat moment dus nog." (~22:59), plus
        SPELER_7_MILAN.md — "Kees leefde toen jij hem rond **22:58** achterliet."
        Bovengrens: de klap van 23:12 (Daan, Sanne, Bram) en in laatste instantie de vondst om
        00:50 (START_HIER.md — "Rond **00:50** … Zij vinden hem dood in de bibliotheek").
        De schijnbare latere ondergrens van 23:15 is aantoonbaar onbetrouwbaar gemaakt:
        SPELER_8_FLEUR.md — "Het gesprek om **23:15** voelde vreemd … Het duurde nog geen vier
        seconden.", in combinatie met de verdwenen telefoon (START_HIER.md) en het extern bekende
        imitatievermogen (SPELER_3_LUCAS.md, SPELER_8_FLEUR.md).
```

```
C-16  PASS
Bewijs: Dekkingstabel op M (23:12), externe getuigen per speler:
        Bram — Noor, Lucas; Noor — Bram, Lucas; Lucas — Bram, Noor; Sanne — Daan; Daan — Sanne;
        Milan — Fleur; Fleur — Milan; achtste speler — nul externe getuigen.
        Aantal spelers met nul externe getuigen op M: precies één.
```

```
C-17  PASS
Bewijs: Herhaling van C-16 met alle zelfverklaringen geschrapt. Elke rij hierboven berust al
        uitsluitend op andermans bladen; er verdwijnt geen enkele cel. Steekproef op de twee
        krapste rijen: SPELER_8_FLEUR.md — "Van **23:11 tot 23:14** stond je onafgebroken met
        Milan te praten" dekt Milan zonder diens eigen woord, en SPELER_7_MILAN.md — "Van **23:11
        tot 23:14** stond je onafgebroken met Fleur te praten" dekt Fleur zonder haar eigen woord.
        Ook adversarieel blijft precies één speler over, dezelfde als in C-16.
```

```
C-18  PASS
Bewijs: In de bewijsketen van NA_AFLOOP_OPENEN.md (negen stappen, inclusief 6a en 6b) is elke
        stap doorgestreept die het daderblad als enige bron heeft. Er valt geen stap weg: alle
        negen dragen minstens één niet-daderbron (zie C-20). De oplossing stelt dat zelf ook vast
        — "De oplossing vereist geen bekentenis of verspreking van Iris" — en die claim houdt bij
        controle stand.
```

```
C-19  PASS
Bewijs: NA_AFLOOP_OPENEN.md bevat een positieve keten van negen stappen die motief, middel en
        gelegenheid dekt, elk met bron in een niet-daderblad:
        motief — "Kees wilde volgens Daan én Fleur dat weekend een oud probleem met Iris uitpraten"
        (SPELER_5_DAAN.md, SPELER_8_FLEUR.md);
        middel — "Sanne zag om 22:35 stof over de hele boekensteun, Bram ziet om 00:50 één
        schoongeveegde plek" (SPELER_4_SANNE.md, SPELER_1_BRAM.md), plus wapenkennis bij twee
        bladen (SPELER_4_SANNE.md, SPELER_7_MILAN.md);
        gelegenheid — het ontbreken van dekking op M plus de routewaarneming
        (SPELER_2_NOOR.md, SPELER_7_MILAN.md).
```

```
C-20  PASS
Bewijs: Tabel ketenstap → bestand → citaat; geen lege regel.
        1 → SPELER_5_DAAN.md "dit weekend eindelijk dat oude gedoe met Iris wilde afsluiten" /
            SPELER_8_FLEUR.md "Dit weekend praten we het eindelijk uit."
        2 → afgeleid uit de dekkingstabel (zeven bladen).
        3 → SPELER_5_DAAN.md "Kees leefde op dat moment dus nog." / SPELER_7_MILAN.md "Kees had
            zijn telefoon bij zich; hij legde hem tijdens jullie woordenwisseling op tafel."
        4 → SPELER_5_DAAN.md / SPELER_4_SANNE.md / SPELER_1_BRAM.md (drie klapcitaten).
        5 → START_HIER.md "**Kees' telefoon is niet gevonden**" / SPELER_2_NOOR.md "Kees' telefoon
            zat rond **22:00** niet in zijn jas. Hij had hem dus bij zich."
        6 → SPELER_8_FLEUR.md "'Niet nu, Fleur. Morgen.'"
        6a → SPELER_4_SANNE.md "Er zat overal een dun laagje stof op." / SPELER_1_BRAM.md
            "behalve op één plek die schoongeveegd leek".
        6b → SPELER_5_DAAN.md "iets met een oude benefietrekening waar ik nooit eerlijk over ben
            geweest" / SPELER_8_FLEUR.md "gedoe met het geld".
        7 → SPELER_3_LUCAS.md "een bijna perfecte imitatie van Kees" / SPELER_8_FLEUR.md "Iris
            heeft ooit via de telefoon zelfs kort Kees' moeder voor de gek gehouden."
        8 → SPELER_2_NOOR.md "had haar lichtgrijze vest opgevouwen in haar handen".
        9 → SPELER_4_SANNE.md "een zware bronzen boekensteun in de vorm van een hert" /
            SPELER_7_MILAN.md "De zware bronzen hertenboekensteun stond op het lage tafeltje."
```

```
C-21  PASS
Bewijs: De positieve keten is voor elk van de zeven andere spelers herhaald. Bij alle zeven
        breekt de keten al bij stap 2: elk van hen heeft op M een externe getuige (zie C-16).
        De naaste concurrenten zijn de twee spelers wier dekking op M op één getuige rust; ook
        bij hen blijven van de negen stappen er hoogstens twee overeind (motiefstap 1 valt weg,
        imitatiestap 7 valt weg, veststap 8 valt weg, en de wapenstappen 6a/9 zijn neutraal).
        Er is dus geen tweede speler die met dezelfde informatie even goed past.
```

```
C-22  PASS
Bewijs: Elk feit uit NA_AFLOOP_OPENEN.md is naar een spelersbestand terug te voeren. Het eerder
        alleen in de oplossing bestaande plaats-delict-feit is nu waarneembaar in het spel:
        NA_AFLOOP_OPENEN.md — "De map met de schuldbekentenis ligt onaangeroerd bij het lichaam;
        het ontbrekende hoekje past op Milans papiertje." ↔ SPELER_1_BRAM.md — "Naast het lichaam
        lag een open map met papieren. Er leek niets uit weggehaald, maar van één blad was een
        hoekje afgescheurd." ↔ SPELER_7_MILAN.md — "een klein afgescheurd hoekje bleef in je
        broekzak".
        Overige steekproef: het vest (SPELER_2_NOOR.md), het stof (SPELER_4_SANNE.md), de
        schoongeveegde plek (SPELER_1_BRAM.md), het viertal seconden aan de telefoon
        (SPELER_8_FLEUR.md) — alle in het spel aanwezig.
```

```
C-23  PASS
Bewijs: Het motief is uit twee onafhankelijke niet-daderbladen te reconstrueren.
        SPELER_5_DAAN.md — "Kees had je vrijdag verteld dat hij 'dit weekend eindelijk dat oude
        gedoe met Iris wilde afsluiten'. Hij noemde het 'iets met een oude benefietrekening waar
        ik nooit eerlijk over ben geweest'."
        SPELER_8_FLEUR.md — "Jaren geleden regelden Kees en Iris samen een benefietactie. Kees zei
        je ooit half gekscherend dat er destijds 'gedoe met het geld' was geweest en dat hij het
        had rechtgezet." en "Vrijdag hoorde je Kees tegen Iris zeggen: 'Dit weekend praten we het
        eindelijk uit.'"
        Beide bronnen samen leveren aanleiding, onderwerp en urgentie zonder het daderblad.
```

### Categorie 3 — Eerlijkheid en dekking

```
C-24  PASS
Bewijs: Dekkingstabel uit C-16: alle zeven onschuldigen hebben op M minstens één externe naam
        (Bram 2, Noor 2, Lucas 2, Sanne 1, Daan 1, Milan 1, Fleur 1). Geen enkele rij is leeg
        behalve die van de dader.
```

```
C-25  N.V.T. (bewust losgelaten door de eigenaar)
Reden: de eigenaar heeft de weglaattest-norm expliciet losgelaten omdat wederzijdse
        afhankelijkheid tussen spelers de bedoelde eindfase van het spel is. Ter informatie, niet
        als oordeel: weglating van SPELER_7_MILAN.md of SPELER_8_FLEUR.md laat één extra speler
        zonder externe dekking op M achter; hetzelfde geldt voor SPELER_4_SANNE.md en
        SPELER_5_DAAN.md. Weglating van SPELER_1_BRAM.md, SPELER_2_NOOR.md of SPELER_3_LUCAS.md
        laat de eliminatie intact.
```

```
C-26  N.V.T. (bewust losgelaten door de eigenaar)
Reden: idem. Ter informatie: W bevat op M twee paren die uitsluitend elkaar dekken. Eén paar is
        extern verankerd (SPELER_3_LUCAS.md ziet het paar acht minuten na M samen uit de serre
        komen); het andere paar is na M alleen afzonderlijk verankerd (SPELER_2_NOOR.md om 23:22
        respectievelijk vanaf 23:20).
```

```
C-27  N.V.T. (bewust losgelaten door de eigenaar)
Reden: idem; telling van C-26 wordt op instructie niet als FAIL geteld.
```

```
C-28  PASS
Bewijs: Per speler zijn de zelfverklaringen geschrapt; bij geen enkele speler blijft een
        zelfstandige onschuldsclaim over. De sterkst zelf-ontlastende formuleringen zijn
        SPELER_7_MILAN.md — "Kees leefde toen jij hem rond **22:58** achterliet." en
        SPELER_4_SANNE.md — "Kees kwam tijdens jouw zoektocht niet binnen." Beide betreffen het
        slachtoffer en niet de eigen dekking op M; hun dekking op M komt in beide gevallen
        uitsluitend van een ander blad (SPELER_8_FLEUR.md respectievelijk SPELER_5_DAAN.md).
```

```
C-29  PASS
Bewijs: Aantal items onder de rubriek "Wat jij weet": Bram 8, Noor 7, Lucas 7, Sanne 9, Daan 8,
        Iris 6, Milan 9, Fleur 9. Mediaan 8; laagste 6, hoogste 9. Geen uitschieter van meer dan
        factor twee ten opzichte van de mediaan; niemand is toeschouwer.
```

```
C-30  PASS
Bewijs: Snelle-ontmaskeringstest over alle zeven niet-daderbladen: er is geen enkele zin die op
        zichzelf alleen bij de dader past. De scherpste losse zin is SPELER_2_NOOR.md — "had haar
        lichtgrijze vest opgevouwen in haar handen", maar die is pas belastend in combinatie met
        SPELER_1_BRAM.md — "op één plek die schoongeveegd leek", dat pas om 00:50 beschikbaar is.
        Ook de imitatiezin (SPELER_3_LUCAS.md) en de motiefzin (SPELER_5_DAAN.md) leveren elk voor
        zich alleen een verdachtmaking op, van hetzelfde gewicht als de haringen bij zes andere
        spelers (schuld, affaire, doorzoeking, aanraking van het wapen).
        Ambiguïteit blijft bovendien intact zolang de groep het telefoontje van 23:15 gelooft: in
        die lezing zijn drie spelers onbewaakt, niet één.
```

```
C-31  PASS
Bewijs: A, kolom "bronnen per belastende aanwijzing" — de belasting is over zes van de zeven
        niet-daderbladen verdeeld: imitatievermogen 2 bronnen (SPELER_3_LUCAS.md,
        SPELER_8_FLEUR.md), motief 2 bronnen (SPELER_5_DAAN.md, SPELER_8_FLEUR.md), wapenkennis
        2 bronnen (SPELER_4_SANNE.md, SPELER_7_MILAN.md), stof/schoongeveegde plek 2 bronnen
        (SPELER_4_SANNE.md, SPELER_1_BRAM.md), positie na M 2 bronnen (SPELER_2_NOOR.md,
        SPELER_7_MILAN.md), verdwenen telefoon 2 bronnen (START_HIER.md, SPELER_2_NOOR.md).
        Slechts één belastend detail berust op één bron (het opgevouwen vest, SPELER_2_NOOR.md);
        dat detail is niet dragend voor de eliminatie.
```

### Categorie 4 — Dangling clues

```
C-32  PASS
Bewijs: A telt 27 items; de kolom "verklaard door" is bij alle 27 ingevuld. De twee eerder open
        items zijn nu afgewikkeld:
        item "Dan laten we het hierbij." (SPELER_3_LUCAS.md) ← SPELER_5_DAAN.md "Sanne vraagt je
        door over je gespannen gesprek met Kees; je kapt het af met: 'Dan laten we het hierbij.'"
        en SPELER_4_SANNE.md "In de serre probeerde je Daan te laten vertellen waarover hij en
        Kees ruzie hadden".
        item "afgescheurd hoekje" (SPELER_7_MILAN.md) ← SPELER_1_BRAM.md "van één blad was een
        hoekje afgescheurd" en NA_AFLOOP_OPENEN.md.
```

```
C-33  PASS
Bewijs: Elke waarneming in A heeft een veroorzakende handeling elders.
        Klap 23:12 ← SPELER_6_IRIS.md "Rond **23:12** sla je Kees één keer".
        Telefoongesprek 23:15 ← "Je neemt op en imiteert Kees".
        Schoongeveegde plek ← "Je veegt het gladde deel af met je lichtgrijze vest".
        Opgevouwen vest ← dezelfde handeling.
        "Dat meen je niet." ← SPELER_7_MILAN.md "Kees kwam binnen terwijl je zocht."
        Iets kleins in de broekzak ← "een klein afgescheurd hoekje bleef in je broekzak".
        "Dan laten we het hierbij." ← SPELER_5_DAAN.md en SPELER_4_SANNE.md (nieuw toegevoegd).
        Voetstappen op de overloop 22:45–23:05 ← R levert drie veroorzakers: Fleur die naar boven
        gaat, Milan die naar beneden en later weer naar boven gaat, Sanne die rond 23:00 naar
        beneden gaat.
        Envelop in de bijkeuken ← SPELER_3_LUCAS.md; imitatie 20:45 ← SPELER_6_IRIS.md.
```

```
C-34  PASS
Bewijs: Alle zelfstandig genoemde voorwerpen hebben een rol in A: bronzen hertenboekensteun
        (wapen), map met papieren en afgescheurd hoekje (Milans motief en ontlasting), telefoon
        (kern van de misleiding), lichtgrijze vest (afvegen), toilettas (verstopplek), envelop met
        reparatiekosten en handdoeken (Lucas' geheim), laptoptas (Sannes zoektocht), jas en
        kapstok (Noors zoektocht), wijnkast (aanleiding van het telefoontje om 23:15 en gespreks-
        onderwerp op de overloop), sigaretten (Fleurs rookgeheim).
        Whisky en speelkaarten dragen geen aanwijzing maar hebben wel een functie: zij verankeren
        de gezamenlijke blokken 20:20–20:45 respectievelijk 21:00–21:25 in T. Geen ongebruikt,
        onbenoemd rekwisiet aangetroffen.
```

```
C-35  PASS
Bewijs: Twee objecten ontbreken of verdwijnen; beide zijn in het oplossingsbestand verklaard.
        START_HIER.md — "**Kees' telefoon is niet gevonden**" → NA_AFLOOP_OPENEN.md "Iris neemt
        Kees' telefoon mee … verstopt de telefoon in haar toilettas" en "De telefoon wordt nooit
        teruggevonden."
        SPELER_1_BRAM.md — "van één blad was een hoekje afgescheurd" → NA_AFLOOP_OPENEN.md "het
        ontbrekende hoekje past op Milans papiertje."
        De verstopte envelop (SPELER_3_LUCAS.md) is geen zoekgeraakt object: het blad zelf noemt
        de bergplaats.
```

```
C-36  PASS
Bewijs: Grep op alle tijdstempels levert 48 unieke tijdstippen. Alle tijdstippen die een
        gebeurtenis met meer dan één betrokkene markeren, komen op minstens twee bladen voor
        (23:12 dertien keer, 23:20 negenendertig keer, 23:11/23:14 zeven keer, 22:58 zeven keer,
        22:35 acht keer).
        Acht tijdstippen komen één keer voor: 20:35, 21:20, 21:40, 21:55, 22:20, 22:42, 23:07 en
        23:24. Alle acht zijn blokgrenzen of privéhandelingen binnen de eigen route van één
        speler en zijn als zodanig verantwoord; geen ervan verwijst naar een gebeurtenis met een
        andere deelnemer. Voorbeeld: SPELER_4_SANNE.md — "Rond **21:40** liep je langs de
        bijkeuken" ligt binnen SPELER_3_LUCAS.md "**21:30–21:45:** alleen in de bijkeuken".
```

```
C-37  PASS
Bewijs: A bevat geen verwijzing naar een persoon, plaats of gebeurtenis zonder tegenhanger.
        Alle acht spelersnamen, het slachtoffer en alle veertien ruimtes komen terug in
        START_HIER.md of op een blad (zie C-60, C-61). Genoemde derden (Sannes zus, Fleurs
        partner, Daans affairepartner, Kees' moeder) treden nergens op als informatiebron en
        dragen geen open verwachting.
        Het dichtst bij een open verwachting komt SPELER_5_DAAN.md — "anderen kunnen dat gezien
        hebben"; dat is een hypothetische formulering ("kunnen"), geen claim dat een getuige
        bestaat, en de gebeurtenis zelf staat op zijn blad. Geen loze verwijzing.
```

```
C-38  PASS
Bewijs: Alle drie de bewust misleidende items zijn in NA_AFLOOP_OPENEN.md als zodanig benoemd:
        "de uitroep 'Dat meen je niet.' die Bram om 22:52 hoort, hoort bij deze woordenwisseling
        en niet bij de daad; die aanwijzing is bedoeld om het moordvenster te vroeg te leggen";
        "de zin 'Dan laten we het hierbij.' die Lucas om 23:20 opvangt, gaat over Sannes vragen
        naar Daans ruzie met Kees en heeft niets met de daad te maken";
        "de groep kan … vaststellen dat het telefoontje van 23:15 geen betrouwbaar 'Kees leeft
        nog'-bewijs is".
        Ook het vierde misleidende spoor is benoemd: "**Sanne:** heimelijk in de bibliotheek en
        aanraken van het waarschijnlijke wapen."
```

### Categorie 5 — Rode haringen

```
C-39  PASS
Bewijs: Ontkrachtingsregel per speler (verdenking → weerlegging → bron):
        Bram (vriendenpot, luide ruzie) → keuken 22:55–23:20 → SPELER_2_NOOR.md, SPELER_3_LUCAS.md.
        Noor (jas doorzocht, zakelijk conflict) → keuken 22:50–23:20 → SPELER_3_LUCAS.md,
        SPELER_1_BRAM.md.
        Lucas (schuld, verstopte envelop) → keuken 22:50–23:20 → SPELER_2_NOOR.md, SPELER_1_BRAM.md.
        Sanne (bibliotheek, wapen aangeraakt) → serre 23:02–23:20 → SPELER_5_DAAN.md, plus
        SPELER_3_LUCAS.md om 23:20.
        Daan (affaire, dreigement) → serre 23:02–23:20 → SPELER_4_SANNE.md, plus SPELER_3_LUCAS.md.
        Milan (schuld, diefstalpoging, in de bibliotheek geweest) → overloop 23:11–23:14 →
        SPELER_8_FLEUR.md.
        Fleur (huurcontract, rookgeheim) → overloop 23:11–23:14 → SPELER_7_MILAN.md.
```

```
C-40  PASS
Bewijs: Voor elk van de zeven haringen is de positieve keten uit C-19 herhaald; geen enkele haalt
        meer dan twee van de negen stappen, omdat stap 2 (geen externe dekking op M) bij alle
        zeven meteen faalt en de stappen 1, 7 en 8 uitsluitend op de dader passen.
        NA_AFLOOP_OPENEN.md stelt hetzelfde vast: "elk van deze zeven heeft op 23:12 minstens één
        getuige die niet zichzelf is."
```

```
C-41  PASS
Bewijs: Elke speler heeft een verdachtmakend feit dat via een ánder blad bekend is, zodat niemand
        uitsluitend door vrijwillige zelfonthulling in beeld komt:
        Bram ← SPELER_5_DAAN.md "hoorde je Bram en Kees in de serre hard praten. Je ving alleen
        op: 'de pot'."
        Noor ← SPELER_5_DAAN.md "zag je Noor in de hal bij de kapstok staan. Ze schrok".
        Lucas ← SPELER_4_SANNE.md "zag je Lucas daar met een envelop in zijn handen staan. Hij
        draaide zich weg toen hij je zag."
        Sanne ← SPELER_1_BRAM.md "Sanne kort de bibliotheek binnengaan" en SPELER_8_FLEUR.md.
        Daan ← SPELER_2_NOOR.md "Daan vertelde je op het terras dat hij een affaire heeft".
        Milan ← SPELER_5_DAAN.md "zag je Milan uit de bibliotheek komen. Milan stopte haastig iets
        kleins in zijn broekzak."
        Fleur ← SPELER_1_BRAM.md "Fleur liet bij de oranjerie iets vallen over 'dat huisje' en
        'negenduizend'."
        Iris ← SPELER_2_NOOR.md, SPELER_5_DAAN.md, SPELER_8_FLEUR.md, SPELER_3_LUCAS.md.
```

```
C-42  PASS
Bewijs: Motieflijst gekruist met de dekkingstabel op M: alle zeven onschuldigen met motief hebben
        op 23:12 minstens één externe getuige (C-24). De enige speler met motief én nul dekking op
        M is de dader. Geen enkele onschuldige combineert beide.
```

```
C-43  PASS
Bewijs: Spelers met een motief jegens het slachtoffer: acht van de acht — chantage over de
        vriendenpot (SPELER_1_BRAM.md), zakelijk conflict en belastende conceptmail
        (SPELER_2_NOOR.md), geëiste €2.500 (SPELER_3_LUCAS.md), niet-verwijderde intieme
        berichten (SPELER_4_SANNE.md), dreigement over de affaire (SPELER_5_DAAN.md), €12.000
        schuld (SPELER_7_MILAN.md), €9.000 huurcontract (SPELER_8_FLEUR.md) en de benefiet-
        rekening (SPELER_6_IRIS.md). Ruim boven de ondergrens van drie.
```

```
C-44  PASS
Bewijs: Alle acht bladen dragen dezelfde zeven koppen in dezelfde volgorde ("Wie je bent", "Wat
        iedereen van jou mag weten", "Jouw geheim", "Jouw avond", "Wat jij weet", "Wat je liever
        verborgen houdt", "Jouw doel"); zie C-67.
        Regelaantallen: 39, 40, 41, 42, 45, 46, 46, 48 — het daderblad ligt met 48 twee regels
        boven het langste onschuldige blad, en qua bestandsgrootte (2856 bytes) in het midden van
        het veld (2385–3577).
        De eerder afwijkende slotalinea is nu op alle acht bladen woordelijk gelijk: "Je mag
        hierover liegen of zwijgen, maar je mag geen getuigen, gesprekken of waarnemingen
        verzinnen die niet op je blad staan. Je mag niet beweren dat iemand jou ergens heeft
        gezien als dat niet werkelijk is gebeurd."
        De eerder verklappende doelzin op SPELER_7_MILAN.md is vervangen door "Je zit er tot over
        je oren in zonder dat je iets met de dood van Kees te maken hebt."
```

```
C-45  PASS
Bewijs: Categorisering van de zeven haringen: geld — Bram (vriendenpot), Lucas (€2.500), Milan
        (€12.000), Fleur (€9.000); relatie — Sanne (oude relatie, intieme berichten), Daan
        (affaire); gelegenheid — Sanne (in de bibliotheek), Milan (in de bibliotheek); gedrag —
        Noor (doorzoeking, schrikreactie), Bram (luide ruzie), Daan (gespannen gesprek in de hal).
        Vier categorieën bezet, geen enkele categorie draagt alle haringen.
```

### Categorie 6 — Geheimen en speelbaarheid

```
C-46  PASS
Bewijs: Tabel speler → geheim → gevolg bij onthulling; geen lege gevolgkolom.
        Bram — greep uit de vriendenpot → SPELER_1_BRAM.md "Hij dreigde het dit weekend aan de
        groep te vertellen."
        Noor — doorzoeking van de jas van het slachtoffer → directe verdenking.
        Lucas — rijden onder invloed plus €2.500 schuld → SPELER_3_LUCAS.md "Kees nam de schuld op
        zich, maar eiste €2.500 van je."
        Sanne — heimelijke doorzoeking naast het vermoedelijke wapen.
        Daan — affaire → SPELER_5_DAAN.md "dreigde na het weekend jouw partner in te lichten."
        Milan — €12.000 schuld en poging tot ontvreemding van bewijs.
        Fleur — rookgeheim tegenover haar partner én €9.000 huurcontract.
        Iris — verduistering van benefietgeld én de daad zelf.
```

```
C-47  PASS
Bewijs: Kruistabel geheim × wie kan het aanroeren; geen enkel geheim staat op nul.
        Zie de zeven citaten onder C-41, aangevuld met SPELER_8_FLEUR.md — "Kees zei je ooit half
        gekscherend dat er destijds 'gedoe met het geld' was geweest" (raakt Iris' geheim) en
        SPELER_1_BRAM.md — "Fleur rookt stiekem" (raakt Fleurs eerste geheim).
```

```
C-48  PASS
Bewijs: Per geheim de formulering bij eigenaar en bij de wetende partij vergeleken. Twee geheimen
        zijn volledig bekend bij één ander, beide met een in het materiaal gegeven reden:
        SPELER_5_DAAN.md — "Rond **22:20** vertelde je Noor alles op het terras." ↔
        SPELER_2_NOOR.md "Daan vertelde je op het terras dat hij een affaire heeft."
        SPELER_8_FLEUR.md rookgeheim ↔ SPELER_1_BRAM.md "Fleur rookt stiekem" — reden: zij rookten
        samen bij de oranjerie (beide bladen, 22:15–22:45).
        Alle overige geheimen zijn bij derden slechts fragmentarisch bekend: SPELER_1_BRAM.md
        kent van Fleurs huurcontract alleen "dat huisje" en "negenduizend"; SPELER_4_SANNE.md ziet
        van Lucas' geheim alleen de envelop; SPELER_5_DAAN.md ving van Brams geheim alleen "de
        pot" op.
```

```
C-49  PASS
Bewijs: Minstens vier expliciete belangenconflicten waarin een geheim een alibi of waarneming
        blokkeert:
        SPELER_1_BRAM.md — "Als je Fleur als getuige gebruikt voor je eerdere avond, moet haar
        rookgeheim waarschijnlijk boven tafel komen."
        SPELER_8_FLEUR.md — "Daardoor wil je aanvankelijk liever niet vertellen waar je tussen
        22:15 en 22:45 was."
        SPELER_7_MILAN.md — "Geef je aanwezigheid in de bibliotheek niet te makkelijk prijs — maar
        besef dat je gesprek met Fleur je enige harde dekking is."
        SPELER_4_SANNE.md — "Leg je aanwezigheid bij een mogelijk moordwapen pas uit wanneer dat
        echt nodig is."
```

```
C-50  PASS
Bewijs: Weglaattest met alle geheimen uit A geschrapt, C-16 en C-19 herhaald.
        C-16 blijft volledig intact: geen enkele dekkingscel op M is een geheim. De vier dragende
        alibicitaten (SPELER_2_NOOR.md/SPELER_3_LUCAS.md over de keuken, SPELER_4_SANNE.md/
        SPELER_5_DAAN.md over de serre, SPELER_7_MILAN.md/SPELER_8_FLEUR.md over de overloop)
        staan alle onder "Jouw avond"/"Wat jij weet" en niet onder "Jouw geheim".
        C-19 verliest hoogstens stap 6a (het stofdetail vereist dat Sanne haar aanwezigheid in de
        bibliotheek toegeeft), maar behoudt de acht overige stappen, inclusief de vervangende
        wapenwaarneming SPELER_1_BRAM.md "op één plek die schoongeveegd leek". Ook de ondergrens
        blijft staan zonder Milans bekentenis, want SPELER_5_DAAN.md levert die zelfstandig.
```

```
C-51  PASS
Bewijs: Alle acht doelrubrieken zijn actief geformuleerd en bevatten een spanning, niet alleen
        "vertel de waarheid". Voorbeelden: SPELER_5_DAAN.md — "Je hebt een sterk motief maar ook
        informatie die het moordvenster sterk kan vernauwen. Bepaal zelf wanneer je die inzet.";
        SPELER_8_FLEUR.md — "Gebruik het telefoongesprek aanvankelijk als bewijs … Als de tijdlijn
        daarmee botst, denk dan opnieuw na"; SPELER_6_IRIS.md — "Zorg dat de groep een andere
        verdachte kiest zonder de spelregels voor liegen te overtreden."
```

### Categorie 7 — Regelconformiteit

```
C-52  PASS
Bewijs: Grep op verzachtende formuleringen in de rubrieken "Wat jij weet". In alle gevallen is de
        waarneming zelf hard geformuleerd en hangt de verzachting uitsluitend aan de interpretatie:
        SPELER_1_BRAM.md — "hoorde je … heel kort een dof geluid" (hard) + "Je dacht op dat moment
        dat er iets omviel" (interpretatie);
        SPELER_4_SANNE.md — "hoorde je … een harde doffe klap" (hard) + "Jullie dachten dat iemand
        iets had laten vallen" (interpretatie);
        SPELER_1_BRAM.md — "op de zware bronzen boekensteun overal stof zat, behalve op één plek"
        (hard) + "die schoongeveegd leek" (interpretatie van de oorzaak).
        De vier dragende alibicitaten en de drie klapcitaten bevatten geen enkele verzachting; zij
        gebruiken alle "onafgebroken" respectievelijk "hoorde je".
```

```
C-53  PASS
Bewijs: START_HIER.md — "Je mag informatie achterhouden en liegen over je **eigen** handelingen of
        onbevestigde locatie. … Je mag geen nieuwe controleerbare feiten verzinnen: geen fictieve
        getuigen, gesprekken, waarnemingen of gebeurtenissen."
        Alle acht bladen herhalen dit woordelijk gelijk: "Je mag hierover liegen of zwijgen, maar
        je mag geen getuigen, gesprekken of waarnemingen verzinnen die niet op je blad staan. Je
        mag niet beweren dat iemand jou ergens heeft gezien als dat niet werkelijk is gebeurd."
        Geen verschil tussen introductie en bladen aangetroffen.
```

```
C-54  PASS
Bewijs: Simulatie van de toegestane leugen die de dader op M dekt.
        SPELER_6_IRIS.md — "Je mag ontkennen, zeggen dat je na 22:47 alleen op je kamer was, of
        een onbevestigde eigen route geven." Dat is een leugen over de eigen onbevestigde locatie
        en dus toegestaan onder START_HIER.md.
        De uitspraak wordt door geen enkel ander blad direct weerlegd: R plaatst op 23:12 niemand
        op de overloop of bij de kamerdeuren behalve twee spelers die het tegendeel niet
        vaststellen (SPELER_7_MILAN.md/SPELER_8_FLEUR.md melden alleen dat zij samen stonden te
        praten en niets bijzonders hoorden). Er is dus minstens één overlevende leugen.
```

```
C-55  PASS
Bewijs: De onder C-54 gesimuleerde verklaring vereist geen verzonnen getuige, gesprek of
        waarneming: zij bestaat uitsluitend uit ontkenning en een onbevestigde eigen locatie.
        Ook de tweede route (zwijgen over 22:47–23:20) blijft binnen de regels. De dader hoeft dus
        geen verboden verzinsel te gebruiken om te overleven.
```

```
C-56  PASS
Bewijs: Doel- en instructierubrieken van alle acht bladen naast de regelparagraaf gelegd. Geen
        enkel blad verplicht tot een verboden handeling. De scherpste instructie,
        SPELER_8_FLEUR.md — "Gebruik het telefoongesprek aanvankelijk als bewijs dat Kees om 23:15
        nog leefde", betreft een gebeurtenis die letterlijk op haar eigen blad staat en is dus
        geen verzinsel. SPELER_6_IRIS.md voegt de beperking zelf expliciet toe: "zonder de
        spelregels voor liegen te overtreden."
```

```
C-57  PASS
Bewijs: START_HIER.md belooft geen enkele bron die ontbreekt: "Er komen tijdens het spel geen
        nieuwe aanwijzingen. Er is geen spelleider nodig. Alles wat nodig is om de zaak op te
        lossen zit in deze introductie en de acht rolbladen." Acht rolbladen zijn aanwezig; er
        worden geen rekwisieten, extra rondes of externe bronnen in het vooruitzicht gesteld.
        "Open `NA_AFLOOP_OPENEN.md` pas nadat iedereen heeft gestemd" verwijst naar een bestaand
        bestand (zie C-66).
```

```
C-58  PASS
Bewijs: Lijst introductiefeiten, elk gegrepen in alle bladen; geen tegenspraak.
        "Rond **20:00** eindigt het diner" — vroegste blokstart op enig blad is 20:00
        (SPELER_2_NOOR.md, SPELER_4_SANNE.md).
        "Vanaf ongeveer **23:50** zit de hele groep bij elkaar in de salon" — zie C-12; de eerdere
        afwijking ("en de eetkamer") is verwijderd en geen blad plaatst de groep na 23:50 elders.
        "Rond **00:50** gaan Bram en Fleur samen kijken" ≡ SPELER_1_BRAM.md en SPELER_8_FLEUR.md.
        "**Kees' telefoon is niet gevonden**" ≡ SPELER_2_NOOR.md "De telefoon zat er niet in."
        "één zware klap tegen het hoofd met een hard, stomp voorwerp" ≡ SPELER_6_IRIS.md "sla je
        Kees één keer".
        "De bibliotheek heeft een groot raam op de tuinzijde, met uitzicht op het grindpad en de
        oranjerie" ≡ SPELER_1_BRAM.md "vanaf het grindpad bij de oranjerie, door het tuinraam".
```

### Categorie 8 — Hygiëne

```
C-59  PASS
Bewijs: START_HIER.md — "Jullie zijn met negen oude vrienden" (acht spelers plus het slachtoffer)
        en "Eén van de acht aanwezige spelers heeft Kees vermoord" en "de acht rolbladen".
        Aanwezig: acht bestanden `SPELER_1_BRAM.md` t/m `SPELER_8_FLEUR.md`.
        NA_AFLOOP_OPENEN.md behandelt in de eliminatiesectie precies acht namen. "negen
        gastenkamers" sluit aan op negen aanwezigen.
```

```
C-60  PASS
Bewijs: Grep op hoofdletternamen over alle tien bestanden levert acht spelersnamen plus "Kees";
        alle worden in START_HIER.md of op een rolblad geïntroduceerd. Genoemde derden (Sannes
        zus, Fleurs partner, Daans affairepartner, Kees' moeder) dragen geen eigennaam, worden op
        het blad van de vertellende speler geïntroduceerd en treden nergens op als informatiebron.
        Geen weespersonages.
```

```
C-61  PASS
Bewijs: Ruimtenamen per bestand geëxtraheerd en vergeleken met START_HIER.md — "eetkamer, salon,
        bibliotheek, keuken, bijkeuken, hal en serre. **Buiten:** overdekt terras, grindpad en een
        oude oranjerie. **Boven:** negen gastenkamers, badkamer en overloop."
        Alle voorkomens op de bladen vallen binnen die lijst; buiten de lijst komen alleen
        "buiten" (SPELER_5_DAAN.md), "trap"/"boven" en "tuinraam" voor, die alle drie door de
        introductietekst gedekt zijn.
```

```
C-62  PASS
Bewijs: Gesorteerde unieke namenlijst per bestand, gediff't. Volledige namen komen uitsluitend in
        de titelregels voor en zijn overal identiek gespeld: "Bram de Wit", "Noor van Dijk",
        "Lucas Meijer", "Sanne Vos", "Daan Smit", "Iris Bakker", "Milan Jansen", "Fleur de Boer".
        Het slachtoffer heet in alle tien bestanden "Kees", zonder achternaam en zonder
        verkleinvorm. Geen enkele spellingvariant aangetroffen.
```

```
C-63  PASS
Bewijs: Grep op alle tijdpatronen: 48 unieke tijdstippen, alle in HH:MM, 24-uurs, met dubbele punt
        en leidende nul (inclusief "00:50"). Nul afwijkende formaten; de twee eerdere verbale
        aanduidingen zijn verdwenen. De enige punt-gescheiden getallen in het pakket zijn
        geldbedragen (€2.500, €4.000, €6.000, €9.000, €12.000) en dus geen tijdnotatie.
```

```
C-64  PASS
Bewijs: Alle tien bestanden dragen dezelfde versieaanduiding: START_HIER.md — "WEEKEND OP LANDGOED
        DE LINDE — VERSIE 4"; elk rolblad — "*Weekend op Landgoed De Linde — versie 4*";
        NA_AFLOOP_OPENEN.md — "NA AFLOOP OPENEN — VERSIE 4". Mapnaam `moordspel-v4` en
        bestandsnamen `SPELER_<n>_<NAAM>.md` corresponderen met de koppen (Bram de Wit in
        SPELER_1_BRAM.md, enzovoort, in de volgorde 1 t/m 8).
```

```
C-65  PASS
Bewijs: Grep op namen en tijdstippen die maar in één bestand voorkomen, plus vergelijking met de
        git-historie van de map (commits `3d638fc`, `d600e30`, `31ec783`).
        Geen resten van eerdere versies: de eerder verwijderde formuleringen ("in de salon en de
        eetkamer", "kwart voor tien", "kwart voor elf", "Je bent een uitstekende rode haring",
        "de tuin", "door de gang heen") komen in de huidige bestanden niet meer voor. De acht
        eenmalig voorkomende tijdstippen zijn alle blokgrenzen binnen één route (zie C-36) en geen
        weesverwijzingen. Geen doorgehaalde plotlijnen aangetroffen.
```

```
C-66  PASS
Bewijs: De enige bestandsnaamverwijzing in het pakket is START_HIER.md — "Open
        `NA_AFLOOP_OPENEN.md` pas nadat iedereen heeft gestemd." Dat bestand bestaat onder exact
        die naam in dezelfde map. Geen enkele andere bestandsnaam wordt in de spelbestanden
        genoemd; er zijn dus geen dode verwijzingen.
```

```
C-67  PASS
Bewijs: Kopregels per blad geëxtraheerd; alle acht sets zijn identiek en in dezelfde volgorde:
        "# <naam>", "## Wie je bent", "## Wat iedereen van jou mag weten", "## Jouw geheim",
        "## Jouw avond", "## Wat jij weet", "## Wat je liever verborgen houdt", "## Jouw doel".
        Ook het daderblad wijkt niet af. Spelers vinden op elk blad dezelfde rubrieken.
```

---

## 2. Regressies ten opzichte van de vorige staat

De vorige reparatieronde (commit `31ec783`, tien wijzigingen over tien bestanden) is regel voor
regel nagelopen. **Aantal regressies: één.**

**REG-1 — nieuw ontstaan reistijdprobleem (C-06, KLEIN).**
De reparatie bij C-07 verving in `SPELER_8_FLEUR.md` de vertrekregel "**22:45:** je gaat naar
boven, naar je kamer." door de aanwezigheidsregel "**22:45–23:11:** alleen op je kamer boven."
Daarmee is het gat weliswaar als "alleen" gemarkeerd (C-07 is nu PASS), maar is een overgang van
nul minuten ontstaan tussen een buitenlocatie aan het eind van het grindpad en een kamer op de
eerste verdieping — terwijl `SPELER_1_BRAM.md` voor dezelfde wandeling vijf minuten nodig heeft.
Dit is een nieuw ontstane afwijking: in de vorige staat stond C-06 op PASS. De reparatie staat bij
C-06 hierboven; zij houdt de C-07-winst intact.

**Geen regressie geconstateerd op de overige risicopunten van de laatste ronde.** Expliciet
gecontroleerd:
- De twee nieuw toegevoegde zinnen over het serregesprek (`SPELER_5_DAAN.md`, `SPELER_4_SANNE.md`)
  zijn onderling wederkerig, gebruiken hetzelfde letterlijke citaat en sluiten aan op de
  waarneming op het derde blad; zij veroorzaken geen nieuwe tijdlijnbotsing (C-02, C-08, C-32,
  C-33).
- De nieuwe zin over het wachten in de hal (`SPELER_7_MILAN.md`) en de nieuwe regel van 23:24
  (`SPELER_6_IRIS.md`) sluiten het eerdere gat van 23:22–23:25 zonder een dubbele aanwezigheid te
  creëren; de vier bladen die het slotmoment van 23:25 noemen blijven onderling gelijk (C-01,
  C-04, C-07).
- De nieuwe waarneming bij het lichaam (`SPELER_1_BRAM.md`) heeft een tegenhanger op een ander
  blad en in het oplossingsbestand en laat geen nieuwe aanwijzing open (C-22, C-32, C-35).
- De toegevoegde slotzin in de liegparagraaf staat nu op alle acht bladen woordelijk gelijk; het
  daderblad is er niet meer aan te herkennen (C-44, C-53, C-67).
- De notatiereparaties hebben het pakket weer volledig uniform gemaakt: nul afwijkende
  tijdformaten (C-63).
- De ruimtereparatie in de introductie wordt door geen enkel blad tegengesproken (C-12, C-58).

**Controle op triviale oplosbaarheid en op afleidbaarheid zonder daderblad.** De laatste ronde
heeft de zaak niet triviaal gemaakt: er is nog steeds geen enkele zin op enig niet-daderblad die
op zichzelf alleen bij de dader past (C-30), de belastende aanwijzingen zijn over zes van de zeven
niet-daderbladen verdeeld (C-31), en het spoor blijft pas sluitend na het weerleggen van het
telefoontje van 23:15 — waarvoor drie afzonderlijke bladen plus de introductie nodig zijn. De
blinde reconstructie is opnieuw volledig uitgevoerd zonder ook maar iets van het daderblad of het
oplossingsbestand te gebruiken en levert, ook adversarieel met geschrapte zelfverklaringen,
precies één overblijvende verdachte op, gelijk aan die in het oplossingsbestand (C-13, C-16,
C-17). De dader is dus onverminderd afleidbaar.

**Verificatie van de reparaties uit de eerdere rapporten.** Alle tien in `AUDIT_RAPPORT_2.md`
voorgestelde reparaties (C-01, C-05, C-07, C-22, C-32, C-33, C-38, C-44, C-58, C-63) zijn
doorgevoerd en houden bij hercontrole stand; alle bijbehorende regels staan in dit rapport op
PASS. Ook de negentien bevindingen uit `AUDIT_RAPPORT.md` zijn in de huidige staat niet meer
aanwezig, met uitzondering van C-25/C-26/C-27, die op instructie van de eigenaar buiten
beoordeling blijven.

---

## 3. Samenvattingstabel

| Categorie | Regels | PASS | FAIL | N.V.T. |
|---|---|---|---|---|
| 1. Interne consistentie (C-01–C-12) | 12 | 11 | 1 | 0 |
| 2. Oplosbaarheid (C-13–C-23) | 11 | 11 | 0 | 0 |
| 3. Eerlijkheid en dekking (C-24–C-31) | 8 | 5 | 0 | 3 |
| 4. Dangling clues (C-32–C-38) | 7 | 7 | 0 | 0 |
| 5. Rode haringen (C-39–C-45) | 7 | 7 | 0 | 0 |
| 6. Geheimen en speelbaarheid (C-46–C-51) | 6 | 6 | 0 | 0 |
| 7. Regelconformiteit (C-52–C-58) | 7 | 7 | 0 | 0 |
| 8. Hygiëne (C-59–C-67) | 9 | 9 | 0 | 0 |
| **Totaal** | **67** | **63** | **1** | **3** |

### FAILs naar ernstgraad

| Ernstgraad | Aantal | Regel-ID's |
|---|---|---|
| **BLOKKEREND** | **0** | — |
| **ERNSTIG** | **0** | — |
| **KLEIN** | **1** | C-06 |

De drie N.V.T.-regels (C-25, C-26, C-27) zijn op instructie van de eigenaar buiten beoordeling
gelaten en tellen niet als FAIL.

---

## 4. Eindoordeel

## **VRIJGEGEVEN MET REPARATIES**

De harde logica houdt onder volledige, onafhankelijke hercontrole stand. De tijdlijn is sluitend:
geen enkele speler staat in enig tijdvak op twee plaatsen (T), geen enkele naam staat in enig
tijdvak in twee ruimtes (R), alle 26 gedeelde intervallen zijn wederkerig ingevuld en komen tot op
de minuut overeen (W), en alle 27 aanwijzingen hebben een ingevulde kolom "verklaard door" (A).
Het moordvenster heeft een aantoonbare onder- én bovengrens uit niet-daderbladen, en het
beslissende moment is door drie waarnemers in twee ruimtes verankerd, met twee verdere bladen als
tijdstempel. De blinde reconstructie levert, ook adversarieel met alle zelfverklaringen geschrapt,
precies één overblijvende verdachte. Motief, wapen, methode, telefoon en route zijn alle
reconstrueerbaar uit steeds minstens twee onafhankelijke niet-daderbladen; geen bewijsstap leunt
op een bekentenis of verspreking. Er is dus geen BLOKKEREND en geen ERNSTIG bevinding.

Er resteert één KLEIN gebrek, en dat is tevens de enige regressie van de laatste reparatieronde:
op één blad is bij het dichten van een tijdlijngat een overgang van nul minuten tussen twee ver
uiteen liggende locaties ontstaan. Het raakt de dekking op het beslissende moment niet, verandert
niets aan de eliminatie en is met twee regels op één blad te herstellen (zie C-06).

**Aanbeveling:** voer de reparatie bij C-06 door — twee regels in één bestand, buiten het
kritieke venster — en herbouw daarna T, R, W en A nog eenmaal ter controle. Daarmee komt het
pakket op nul FAILs en kan het worden vrijgegeven.
