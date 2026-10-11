# Tier 1 SEO - meetprotocol en baseline

**Doel**: vaststellen wat de tier-1-aanpassingen aan de site opleveren in zoekresultaat-positie en organisch verkeer over de komende 4–6 weken.

**Wat we hebben aangepast** (mei 2026):
- Title-tags met "Apeldoorn-Zuid" in plaats van "Apeldoorn"
- H1's per pagina met focus-keyword (geo + dienst)
- Meta-descriptions met Surinameweg + Apeldoorn-Zuid + alle merken
- Nieuwe geo-sectie op de homepage met wijken-vermelding (De Maten, Zevenhuizen, Matenpoort)
- LocalBusiness schema `areaServed` uitgebreid van "Apeldoorn" naar 6 plaatsen + Apeldoorn-Zuid

---

## 1. Termen om te volgen

### Primair (verwacht effect zichtbaar binnen 4 weken)

| # | Zoekterm | Doelpagina | Doel-positie | Baseline-positie nu |
|---|----------|-----------|--------------|---------------------|
| 1 | `garage apeldoorn-zuid` | `/` | top-3 | _vul in_ |
| 2 | `garage surinameweg apeldoorn` | `/` | top-1 | _vul in_ |
| 3 | `apk apeldoorn-zuid` | `/apk` | top-5 | _vul in_ |
| 4 | `auto onderhoud apeldoorn-zuid` | `/onderhoud` | top-3 | _vul in_ |
| 5 | `auto-onderhoud apeldoorn-zuid` | `/onderhoud` | top-3 | _vul in_ |
| 6 | `auto diagnose apeldoorn` | `/specialistisch` | top-5 | _vul in_ |

### Secundair (verwacht effect 6–12 weken)

| # | Zoekterm | Doelpagina | Doel-positie |
|---|----------|-----------|--------------|
| 7 | `auto reparatie apeldoorn` | `/onderhoud` | top-10 |
| 8 | `garage apeldoorn` | `/` | top-15 |
| 9 | `banden apeldoorn-zuid` | `/banden` | top-5 |
| 10 | `airco apeldoorn-zuid` | `/airco` | top-5 |
| 11 | `schadeherstel apeldoorn-zuid` | `/schadeherstel` | top-5 |
| 12 | `motormanagement apeldoorn` | `/specialistisch` | top-5 |

---

## 2. Hoe meten

### A. Handmatige rank-check (5 minuten per ronde)

Open een **incognito-venster** (geen cookies, geen persoonlijke geschiedenis) en zoek de termen op `google.nl`. Noteer de positie van `all-cars-specialist.nl` in de organische resultaten.

Doe dit:
- **Vandaag** (baseline) - vul de "_vul in_" plekken hierboven in
- **Wekelijks** op vaste dag (bijv. maandag-ochtend)
- **Op exact dezelfde locatie** (laptop op kantoor, niet op telefoon ergens anders) want lokale resultaten verschillen per locatie

> Handige tip: zet je locatie in Google handmatig op "Apeldoorn" (rechtsonder in zoekresultaten of via &near= URL-parameter), zodat je consistent meet voor de doel-stad en niet je eigen huidige locatie volgt.

### B. Google Search Console (verplicht inrichten)

GSC laat zien op welke termen je site daadwerkelijk getoond wordt en wordt aangeklikt - dit is de **enige objectieve bron**.

**Setup-checklist** (eenmalig, ~10 minuten):

1. Ga naar [search.google.com/search-console](https://search.google.com/search-console)
2. Voeg property toe: `https://all-cars-specialist.nl` (of de Vercel-URL tot het domein gekoppeld is)
3. Verifieer via DNS-TXT-record (bij je domein-registrar) of via HTML-meta-tag (kan ik in de site zetten als je de tag stuurt)
4. Submit de sitemap: `https://all-cars-specialist.nl/sitemap.xml`
5. Wacht 3–7 dagen voor eerste data

Vanaf dan: dagelijks tot wekelijks check op:
- **Performance** → Queries → top zoektermen waar je op getoond wordt
- **Performance** → Pages → welke pagina's krijgen impressies
- **Performance** → Countries → 99% NL verwacht
- **Performance** → Devices → mobile vs desktop

### C. Plausible of Google Analytics 4

Voor verkeersmeting (los van zoektermen). Plausible is privacy-vriendelijker en heeft geen cookie-banner nodig, GA4 heeft meer features.

**Aanbeveling**: Plausible (€9/maand voor 10K pageviews) of GA4 (gratis maar wel cookie-banner verplicht in NL).

Beide krijgen dan per maand:
- Aantal bezoekers
- Top-pages
- Verkeersbron (organisch / direct / verwijzing)
- Gemiddelde sessieduur
- Bounce rate

---

## 3. Baseline vastleggen - vandaag

Voer de volgende stappen vandaag of morgen uit, voordat de zoekmachines de nieuwe versie volledig hebben opgepikt:

### Stap 1 - handmatige rank-check
Loop de tabel in paragraaf 1 langs en vul "Baseline-positie nu" in. Als de site niet in de top-50 staat, schrijf "n.v.t." of "buiten top-50".

### Stap 2 - Search Console verifiëren
Volg de setup-stappen in B. Hoe eerder verified, hoe meer historische data je later hebt.

### Stap 3 - Analytics installeren
Plausible of GA4 toevoegen aan de site. Als je voor Plausible kiest: laat me het script weten en ik plaats het in de `<head>`. Voor GA4: stuur de Measurement ID.

### Stap 4 - Reviews-startwaarde noteren
Open Google Maps op All-Cars Specialist B.V. en noteer:
- Aantal reviews vandaag: _____
- Gemiddelde score vandaag: _____

---

## 4. Evaluatie-momenten

| Wanneer | Wat checken | Verwacht resultaat |
|---------|------------|---------------------|
| **Week 1** | Of de nieuwe content geïndexeerd is | Meeste pagina's in `site:all-cars-specialist.nl` zoekopdracht zichtbaar |
| **Week 2** | Eerste rank-check vs baseline | Lichte beweging op tier-1 termen |
| **Week 4** | Volledige rank-check + eerste GSC-data | Tier-1 termen merkbaar omhoog (3–10 posities) |
| **Week 6** | Verkeersgroei zichtbaar in analytics | 1.5–2× organisch verkeer t.o.v. baseline |
| **Week 12** | Doelposities tier 1 behaald? | top-3/top-5 conform doelmatrix |

---

## 5. Realistische verwachting

**Wat tier 1 NU al doet** (zonder extra werk):
- Voor zoekers in Apeldoorn-Zuid is de site direct **veel relevanter**: de title in de SERP zegt "APK-keuring Apeldoorn-Zuid" in plaats van "APK-keuring in Apeldoorn", wat de click-through rate verhoogt
- Het LocalBusiness-schema met uitgebreid `areaServed` helpt de site verschijnen in lokale zoekresultaten voor omliggende plaatsen
- De nieuwe geo-sectie op de homepage geeft Google een sterk signaal dat dit een Apeldoorn-Zuid-bedrijf is, niet "een garage in Nederland"

**Wat tier 1 NIET doet**:
- Het lost het reviews-tekort niet op (KwikFit/Vakgarage hebben er honderden meer)
- Het lost het GBP-tekort niet op (cruciaal voor map-pack-ranking)
- Het zet de site nog niet bovenaan voor `garage apeldoorn` (te competitief, hoog volume)

**Voor échte sprong**: tier 1 + GBP-volledig + reviews-acquisitie + buurplaats-pagina's. Dat is het volledige plan in `seo-plan.md`.

---

## 6. Wat als ik na 6 weken geen verbetering zie?

Drie meest waarschijnlijke oorzaken in volgorde van waarschijnlijkheid:

1. **Search Console is niet goed verbonden** of sitemap niet ingediend - controleer dat elke pagina via GSC "ingediend en geïndexeerd" staat.
2. **Domein staat nog op `vercel.app`** in plaats van op `all-cars-specialist.nl` - Google ziet dan twee verschillende sites en verdeelt het ranking-vermogen. Volle effect pas na DNS-cutover naar het echte domein.
3. **Geen externe links / weinig review-momentum** - dan moet je wachten op trust-opbouw. Begin parallel met GBP-uitbreiding en review-flow.

Bij geen-effect-na-6-weken: laat me opnieuw kijken, dan analyseren we GSC-data samen en sturen bij.

---

**Volgende stap**: deploy de aanpassingen (`./deploy.sh`), vul de baseline-tabel in paragraaf 1 in, en richt Search Console in. Daarna meten we elke week 5 minuten en laten de data spreken.
