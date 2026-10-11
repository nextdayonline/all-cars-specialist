# Content-gap analyse - All-Cars Specialist (SEO + GEO)

**Datum**: 24 juni 2026
**Doel**: in kaart brengen welke content ontbreekt om de site sterker te maken in klassieke zoekresultaten (SEO) én in AI-antwoorden zoals Google AI Overviews, ChatGPT, Perplexity en Gemini (GEO).
**Vorige documenten**: `strategie.md`, `seo-plan.md`, `concurrentie-analyse.md`, `claims-audit.md`, `seo-meetprotocol-tier1.md`. Dit document bouwt daarop voort en kijkt naar de feitelijk gebouwde site (8 HTML-pagina's, statisch op Vercel).

## Status (bijgewerkt 24 juni 2026)

- ✅ **Prio 1 (quick wins) live**: FAQ + FAQPage-schema op alle 6 dienstpagina's, banden-schema gefixt, `llms.txt` toegevoegd.
- ✅ **Prio 2 live**: 3 nieuwe dienstpagina's: `/aankoopkeuring`, `/distributieriem-vervangen`, `/foutmelding-uitlezen` (elk met Service- + FAQPage-schema en interne links).
- ✅ **Prio 3 compleet**: alle 5 buurplaats-pagina's live (`/garage-beekbergen`, `/garage-twello`, `/garage-vaassen`, `/garage-loenen`, `/garage-klarenbeek`), elk met eigen openingstekst, reistijd en lokale FAQ; gelinkt vanaf homepage geo-sectie + footer.
- ✅ **Prio 5 deels**: `/over-ons` uitgebreid (~250 → ~475 woorden) met verhaal, diagnose-aanpak en werkplaats-feiten (drie hefbruggen, uitleesapparatuur). Person-schema + persoonlijke foto volgen zodra naam en foto beschikbaar zijn.
- ✅ **`sameAs` toegevoegd**: het Google-bedrijfsprofiel (entity `/g/1ptwtjfd9`) staat nu in het AutoRepair-schema op alle pagina's. Entiteitssignaal voor SEO en GEO.
- ⛔ **Niet beschikbaar (bevestigd)**: garagetarieven zijn niet bekend, dus prijsvragen blijven "bel/app voor tarief". Foto eigenaar is er niet, dus geen persoonsfoto; Person-schema blijft achterwege zolang er geen naam is.
- **Nog te doen**: blogartikelen (prio 4, bewust geparkeerd). Optioneel later: extra social-profielen aan `sameAs` toevoegen (bv. Facebook) als die er zijn.
- Site telt nu 19 indexeerbare URL's (was 11).

### Wijzigingen 11 oktober 2026 (op verzoek van Peter)

- ⛔ **Aankoopkeuring vervallen**: de pagina `/aankoopkeuring` en alle verwijzingen ernaar zijn verwijderd (footer, homepage, APK- en onderhoudspagina, schema, sitemap, `llms.txt`). De oude URL verwijst met een 301 naar de homepage. Niet opnieuw opnemen zonder overleg; de aanbevelingen hierover verderop in dit document en in `seo-plan.md` zijn daarmee achterhaald.
- 🔁 **Versnellingsbakolie verversen is nu versnellingsbak spoelen**: nieuwe URL `/versnellingsbak-spoelen`, met een 301 vanaf `/versnellingsbakolie-verversen`. Onderbouwing uit Google Keyword Planner (Nederland, per maand): "versnellingsbakolie verversen" 720, "automaat spoelen" 590, "automaat spoelen kosten" 590, "automaatbak spoelen" 480, "versnellingsbak spoelen" 320. De schrijfwijzen "versnellingsbakolie spoelen" en "versnellingsbak spoeling" hebben geen meetbaar volume, daarom is de paginatitel "Versnellingsbak spoelen". Verversen blijft op de pagina staan als uitleg en als aanpak voor de handbak.
- De sitemap telt na deze wijziging 19 URL's.

---

## 1. Wat er nu staat (nulmeting van de gebouwde site)

| Pagina | Bodytekst | FAQ zichtbaar | FAQPage schema | Prijs genoemd |
|--------|-----------|---------------|----------------|---------------|
| Home | lang (>600) | nee | nee | nee |
| APK | middel (300-600) | ja (6) | ja | nee |
| Onderhoud | lang (>600) | nee | nee | nee |
| Specialistisch | middel | nee | nee | nee |
| Banden | middel | ja (3) | **nee** | nee |
| Airco | middel | nee | nee | nee |
| Schadeherstel | middel | nee | nee | nee |
| Over ons | kort (<300) | nee | nee | n.v.t. |
| Contact | middel | nee | nee | Maps-embed aanwezig |

**Technisch is de site in orde.** Op elke pagina staat AutoRepair-schema, Service-schema per dienst, BreadcrumbList, drie Review-objecten, AggregateRating (4.9 / 33 reviews) op de home, canonicals, Open Graph, snelle statische HTML. De tier-1 geo-targeting (Apeldoorn-Zuid in titles, H1's, areaServed met 6 plaatsen) is doorgevoerd.

**De zwakte zit in de content-laag, niet de techniek.** De meeste dienstpagina's halen 300-600 woorden, "Over ons" minder dan 300. Er is geen blog, geen buurplaats-pagina, geen prijsinformatie, en FAQ-content staat maar op twee van de acht pagina's. Precies de content uit `seo-plan.md` paragraaf 2 (extra dienstpagina's, buurplaats-hubs, uitlegartikelen) is nog niet gebouwd. Dat is tegelijk het grootste gat en de grootste kans.

---

## 2. Waarom GEO nu apart aandacht vraagt

De bestaande plannen zijn sterk op klassieke lokale SEO, maar geschreven vóór de doorbraak van AI-antwoorden in de zoekresultaten. Een groeiend deel van de zoekopdrachten eindigt nu in een AI-overzicht in plaats van een lijst blauwe links. Voor een garage betekent dat: als iemand vraagt "wat kost een APK in Apeldoorn" of "mijn motormanagementlampje brandt, wat nu", dan wil je dat de AI jouw site citeert als bron.

AI-modellen citeren ander materiaal dan waar Google traditioneel op rankt. Wat ze oppikken:

- **Korte, letterlijk te citeren antwoorden.** Een vraag als kop, daaronder een antwoord van 40-60 woorden dat op zichzelf staat. Dit is het belangrijkste GEO-mechanisme en de site doet het bijna nergens.
- **Concrete getallen.** Prijzen, tijdsduur, intervallen in kilometers, jaartallen. Modellen hechten aan specifieke data en vage teksten ("bel voor een tarief") worden zelden geciteerd.
- **Heldere entiteit.** Eén consistente naam, adres en telefoonnummer overal, plus `sameAs`-links naar het Google Bedrijfsprofiel en social. Dit ontbreekt nu in de schema.
- **Expertise-signalen (E-E-A-T).** Wie doet het werk, hoeveel jaar ervaring, welke apparatuur. Een herkenbare monteur/eigenaar met naam weegt zwaarder dan een anonieme "wij".

Het mooie: vrijwel elke GEO-verbetering helpt ook de klassieke SEO. Het is geen aparte werkstroom, het is dezelfde content scherper opgeschreven.

---

## 3. De gaten, geprioriteerd

### Prio 1 - quick wins (laag werk, direct effect)

**1a. FAQ-blokken op elke dienstpagina, met FAQPage-schema.**
Nu staat FAQ alleen op APK (goed gedaan, met schema) en op Banden (zichtbaar maar zónder schema, dus dat schema-blok mist en is een directe fix). Voeg op onderhoud, specialistisch, airco en schadeherstel elk 4-6 vragen toe in dezelfde `<details>`-stijl plus FAQPage-schema. Dit is de meest renderende GEO-ingreep: het levert letterlijk citeerbare vraag-antwoord-paren.

Voorbeelden per pagina:
- Onderhoud: "Wat is het verschil tussen een kleine en grote beurt?", "Hoe vaak moet mijn auto onderhoud?", "Behoud ik mijn garantie bij een onafhankelijke garage?"
- Specialistisch: "Wat kost een diagnose?", "Mijn foutmelding komt steeds terug, wat betekent dat?", "Kunnen jullie een storing vinden die een andere garage liet liggen?"
- Airco: "Hoe vaak moet ik mijn airco laten vullen?", "Waarom koelt mijn airco niet meer?", "Wat kost airco vullen?"
- Schadeherstel: "Regelen jullie de afhandeling met mijn verzekeraar?", "Kan ik ook terecht voor niet-verzekerde schade?"

**1b. Banden-FAQ alsnog een FAQPage-schema geven.** Klein, want de zichtbare vragen staan er al.

**1c. Prijsindicaties toevoegen waar mogelijk.** Zelfs een vanaf-prijs of bandbreedte (APK vanaf €X, diagnose-uurtarief, kleine beurt vanaf €Y) is een sterk SEO- én GEO-signaal en een onderscheid tegenover concurrenten die niets noemen. Vereist input van Peter (zie claims-audit: prijzen zijn niet geverifieerd). Als harde prijzen niet kunnen: geef in elk geval tijdsduur en wat inbegrepen is.

**1d. `sameAs` in het AutoRepair-schema.** Voeg links toe naar het Google Bedrijfsprofiel, Facebook en eventuele listings (AutomotiveBedrijven.nl). Versterkt de entiteitsherkenning voor zowel Google als AI-modellen. Puur techniek, geen tekst nodig.

**1e. `aggregateRating` nu alleen op de home.** Overweeg dit op alle dienstpagina's te zetten (mits review-aantal kloppend en eerlijk gekoppeld), zodat sterren breder meeliften.

### Prio 2 - ontbrekende dienstpagina's (medium werk, hoog intentieverkeer)

Deze stonden al in `seo-plan.md` 2A maar zijn niet gebouwd. Allemaal hoge koopintentie, lage lokale concurrentie:

1. **`/aankoopkeuring`** - auto laten checken vóór tweedehands aankoop. Gat in de markt volgens de concurrentie-analyse. Hoog conversiepotentieel.
2. **`/distributieriem-vervangen`** - veel zoekvolume, mensen zoeken specifiek op deze klus plus prijs.
3. **`/foutmelding-uitlezen`** (of `/diagnose-uitlezen`) - past precies bij de specialist-positionering, vangt de "lampje brandt"-zoeker.

Elke pagina volgens het bewezen patroon: pijn → oplossing → werkwijze → FAQ met schema → CTA. Mik op 500-800 woorden met minstens één concreet getal en een FAQ-blok.

### Prio 3 - buurplaats-hubs (medium werk, breidt bereik uit)

De `areaServed` in de schema noemt Beekbergen, Loenen, Vaassen, Klarenbeek en Twello, maar er is geen enkele pagina die op die plaatsen target. Dat is een mismatch: je claimt het gebied in de data maar hebt geen landingspagina waar een zoeker uit Twello op binnenkomt. Bouw per kern één pagina (`/garage-beekbergen`, `/garage-twello` eerst, die zijn het grootst), met eigen H1, eigen openingsalinea, route/afstand vanaf Surinameweg, en een plaats-specifieke FAQ. Geen duplicate content: elke pagina krijgt een eigen invalshoek.

### Prio 4 - uitleg-/blogartikelen (doorlopend, long-tail magneet)

Nul artikelen nu. Dit is de motor voor de tier-3 klacht-zoektermen uit `seo-plan.md` (`auto trilt`, `abs-lampje brandt`, `koppakking`, etc.) en tegelijk het beste GEO-materiaal: vraaggestuurde uitleg is precies wat AI-modellen samenvatten en citeren. Start met 2 per maand, ~800-1200 woorden, elk met een FAQ-blok onderaan, interne link naar de relevante dienstpagina en een externe autoriteitsbron (RDW, BOVAG, ANWB) waar logisch.

Eerste vijf, op intentie gesorteerd:
1. Waarschuwingslampje op je dashboard: wat betekenen de kleuren en wat moet je doen
2. Versleten distributieriem herkennen (en wat vervanging kost)
3. Wanneer is mijn auto APK? Datum checken en wat je kunt verwachten
4. Auto trilt tijdens het rijden: de meest voorkomende oorzaken
5. Aankoopkeuring tweedehands auto: waar wij op letten

### Prio 5 - structurele E-E-A-T en GEO-techniek

- **"Over ons" uitbreiden** van <300 woorden naar een echt verhaal met een naam en gezicht: wie is de monteur/eigenaar, sinds wanneer, waar komt de diagnose-expertise vandaan. Dit is nu de dunste pagina en juist de belangrijkste voor vertrouwen en E-E-A-T. Voeg een `Person`-schema voor de eigenaar toe.
- **`llms.txt`** in de root plaatsen: een kort, plat tekstbestand dat AI-crawlers een samenvatting geeft van wie ACS is, wat de diensten zijn, het adres en de openingstijden. Goedkope GEO-hygiëne.
- **Auteur/datum op artikelen** zodra de blog er staat (versheid + E-E-A-T).
- **Interne links verrijken.** Nu linkt alles identiek via header/footer. Voeg contextuele links in de body toe (vanuit een blogartikel over trillingen naar `/specialistisch`, vanuit APK naar `/onderhoud`), dat verdeelt autoriteit en helpt zowel Google als de AI-crawl de samenhang zien.

---

## 4. Afhankelijkheid: claims-audit

Een groot deel van de nieuwe content raakt feiten die nog niet bevestigd zijn (zie `claims-audit.md`): prijzen, exacte werkwijze, of ze EV-diagnose doen, bandenopslag, verzekeringsafhandeling. Schrijf nieuwe pagina's dus in twee slagen: eerst het skelet met de wél-geverifieerde feiten, dan de details invullen zodra Peter per punt ja/nee zegt. Verzin geen prijzen of garanties om een pagina "compleet" te maken; dat ondermijnt precies het vertrouwen dat de specialist-positionering moet uitstralen.

---

## 5. Aanbevolen volgorde

1. **Week 1**: FAQ + FAQPage-schema op alle dienstpagina's, banden-schema fixen, `sameAs` toevoegen, `llms.txt` plaatsen. (Quick wins, grotendeels zonder nieuwe feiten.)
2. **Week 1-2**: prijslijst ophalen bij Peter en indicaties op de dienstpagina's zetten.
3. **Week 2-3**: drie ontbrekende dienstpagina's (aankoopkeuring, distributieriem, foutmelding-uitlezen).
4. **Week 3-4**: "Over ons" uitbreiden + Person-schema; eerste twee blogartikelen.
5. **Maand 2**: buurplaats-pagina's Beekbergen en Twello; blog-ritme van 2 per maand vasthouden.

Elke nieuw geschreven tekst gaat vóór publicatie door de humanizer-pass (Nederlands), zodat de content menselijk leest en niet als AI-sjabloon. Concreet, "je"-vorm, geen opgeklopte significantie, geen rijtjes-van-drie als opvulling.
