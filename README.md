# All-Cars Specialist B.V. - Website

Statische multi-page website voor [all-cars-specialist.nl](https://all-cars-specialist.nl).
Geoptimaliseerd voor de **Vercel + GitHub stack**.

## Stack

- HTML/CSS, geen build-step. Lichtgewicht, snel, makkelijk te beheren.
- Fonts: Google Fonts (Barlow Condensed + Inter)
- Hosting: **Vercel** (statische deploy)
- Versie-beheer: **GitHub**
- Latere uitbreiding: Next.js + Supabase voor het afspraak-formulier (zie `strategie.md`)

## Pagina-structuur

```
/                  Home
/apk               APK-keuring
/onderhoud         Onderhoud & reparatie
/specialistisch    Specialistisch onderhoud (diagnose) - SEO-prioriteit
/banden            Banden & wielen
/airco             Airco-service
/schadeherstel     Schadeherstel
/over-ons          Over ons
/contact           Contact + afspraak-formulier
/404               Niet-gevonden pagina
```

`vercel.json` zorgt voor clean URLs (geen `.html` in de browser-balk).

## Lokaal bekijken

Met clean URLs (`/apk` ipv `/apk.html`) werkt direct openen via `file://` niet meer voor navigatie - gebruik een lokale dev-server:

```bash
# Optie 1: Vercel CLI (exact gelijk aan productie, inclusief cleanUrls)
npx vercel dev
# → http://localhost:3000

# Optie 2: simpele static server (.html wordt auto-detected)
npx serve .
# → http://localhost:3000
```

De homepage `index.html` openen via `file://` werkt nog wel voor een snelle stylinge-check, maar interne navigatie naar `/apk` etc. werkt alleen via een server.

## Deployen via Vercel + GitHub

1. **Maak een GitHub repo** (bijv. `all-cars-specialist`):
   ```bash
   git init
   git add .
   git commit -m "Initial site"
   git remote add origin git@github.com:<jouw-org>/all-cars-specialist.git
   git push -u origin main
   ```
2. **Importeer in Vercel**: ga naar [vercel.com/new](https://vercel.com/new), kies de repo. Geen framework-detectie nodig - Vercel ziet vanzelf dat het statische HTML is.
3. **Domein koppelen**: in Vercel → Settings → Domains → voeg `all-cars-specialist.nl` toe en wijs DNS bij je registrar (CNAME of A-record naar Vercel).
4. **Done**: elke push naar `main` deployt automatisch. PRs krijgen preview-URLs.

## Wat is er nog niet definitief?

- [x] **Telefoonnummer**: 06 33 93 57 20 (geverifieerd)
- [x] **Privacyverklaring + AV**: pagina's staan live en zijn gekoppeld in de footer.
- [x] **Opgeruimd**: de 8 stale root-.html-bestanden en de ongebruikte logo's zijn verwijderd.
- [ ] **Logo**: huidig SVG-logo is een nabouw, vervang door echte versie zodra Peter die aanlevert (zoek `acs-logo-symbol` in deze map en vervang).
- [ ] **Foto-shoot**: één werkplaatsfoto. Idealiter komen er 5-10 eigen foto's bij (gevel, monteurs, brug, klantruimte, diagnose-apparatuur).
- [ ] **Afspraak-formulier**: post nu naar FormSubmit. Later te verbinden met Supabase + Resend voor mailbevestiging - zie `strategie.md` fase 3.

### Geverifieerd (audit 6 juli 2026)

- [x] **Reviews en rating**: alle 6 reviewnamen op de homepage staan echt op het Google-profiel; rating 4,9 met 33 reviews klopt exact. Henk Marijnus gaf 4 sterren (site toont nu ook 4).
- [x] **Openingstijden**: ma-vr 09:00-17:00, weekend gesloten - aangepast op verzoek van Peter (augustus 2026). Let op: Google Business Profile vermeldde eerder 08:30-17:30 en moet daar ook worden bijgewerkt.
- [x] **RDW**: All Cars Specialist B.V. heeft volgens het openbare RDW-register alleen een Handelaarskenteken-erkenning, geen eigen APK-erkenning. De site-formulering "APK via RDW-erkend partner-station" is dus correct.
- [x] **Reistijden**: gecheckt via routeservice (OSRM). Beekbergen 6 min, Loenen 13, Klarenbeek 13, Vaassen 20, Twello 19. Twello-claim aangepast van "kwartier" naar "twintig minuten".
- [x] **NAP op Google**: naam, adres, telefoon en website-link op het profiel kloppen met de site.

### Te bevestigen door Peter

- [ ] APK: welk partner-station voert de keuring uit? (Dat het geen eigen erkenning is, is bevestigd.)
- [ ] Parkeergelegenheid bij de werkplaats ("ruime parkeermogelijkheid" op de site is onbevestigd).
- [ ] priceRange "€€" (middenklasse-tarief) in het schema.
- [ ] De aangepaste AV-clausules: meerwerk (artikel 6) en stalling van voertuigen (artikel 8).
- [ ] Google Business Profile: laatste foto's zijn ~8 jaar oud - nieuwe werkplaats-/gevelfoto's uploaden helpt lokale ranking.
- [ ] Google Business Profile: openingstijden bijwerken naar ma-vr 09:00-17:00 (site is al aangepast; afwijkende tijden op Google schaden de lokale ranking).

## Bouwen / regenereren

Het `build_site.py` script (in de outputs-map van Cowork) genereert alle pagina's vanuit één template.
Aanpassingen aan navigatie, footer of meta-data: pas het script aan en run opnieuw.

```bash
python3 build_site.py
```

## SEO-status

- ✅ LocalBusiness + AutoRepair schema op elke pagina
- ✅ FAQPage-schema + zichtbare FAQ op alle 6 dienstpagina's (apk, onderhoud, specialistisch, banden, airco, schadeherstel)
- ✅ llms.txt voor AI-crawlers (GEO)
- ✅ Open Graph meta-tags
- ✅ Per-page title + description
- ✅ Sitemap.xml + robots.txt
- ✅ Clean URLs via vercel.json
- ✅ Werkplaatsfoto met beschrijvende alt-tekst
- ⚠️ Nog toevoegen: GA4 of Plausible (privacy-vriendelijk), GSC-verificatie, Bing Webmaster Tools

## Verkeer en lokale SEO (na launch)

Volg de roadmap in `strategie.md` paragraaf 9, fase 6.

---

Vragen of toevoegingen? Open een issue in de GitHub-repo of geef het door aan Peter.
