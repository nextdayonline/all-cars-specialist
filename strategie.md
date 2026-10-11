# All-Cars Specialist - Strategische basis nieuwe website

**Project**: Volledige rebuild van all-cars-specialist.nl
**Stack**: Next.js (App Router) op Vercel + Supabase + GitHub
**Doel**: Méér leads (afspraken/offertes), sterkere lokale SEO-positie, professionele uitstraling die past bij het werkelijke kennisniveau van de garage.
**Datum**: mei 2026

---

## 1. Wie is All-Cars Specialist (zoals het nu blijkt)

- **Locatie**: Surinameweg 33, 7333 PC Apeldoorn (Apeldoorn-Zuid)
- **Sinds**: 2013
- **Diensten**: onderhoud, reparatie, APK, banden, tuning, autoschade, specialistische diagnose
- **Tagline huidig**: "Dé Garage voor Onderhoud, Reparatie en Tuning"
- **Reviews-signaal**: "uitzonderlijke autotechnische kennis", "zelfs gerenommeerde autobedrijven komen hier als ze er zelf niet uitkomen", "geen poespas, uitstekende service"
- **Huidige site**: gebouwd op SiteGround Website Builder - beperkt CMS, geen LocalBusiness schema, telefoon/adres niet prominent, geen werkplaatsfoto's, geen review-block, geen booking-flow

## 2. Positionering - kerngedachte

> **"De garage waar zelfs garages naartoe komen."**

Niet de goedkoopste APK-shop in Apeldoorn (Vakgarage, KwikFit, Bakker domineren dat segment), maar de **specialist voor diagnose en complexe storingen** - met onderhoud en APK als toegangspoort. Dit is geen marketingclaim die we zelf bedenken: dit is letterlijk wat klanten en collega-garages al zeggen. We maken het alleen zichtbaar.

### Drie positioneringspijlers
1. **Specialist** - "Wat anderen niet kunnen oplossen, lossen wij op." Diagnose, motormanagement, elektronica, hybride/EV.
2. **Eerlijk vakmanschap** - Vaste werkplaats sinds 2013, geen verkooppraatjes, transparante prijzen, alleen nodig werk.
3. **Compleet** - APK, onderhoud, banden, schade, tuning. Eén adres voor de hele auto.

## 3. Doelgroepen (in volgorde van prioriteit)

| # | Doelgroep | Behoefte | Belangrijkste pagina |
|---|-----------|----------|---------------------|
| 1 | **Autobezitter Apeldoorn met klacht/storing** | "Mijn auto doet raar, andere garage komt er niet uit" | Specialistisch onderhoud / Diagnose |
| 2 | **APK-zoeker Apeldoorn-Zuid** | Snelle APK + check-up | APK |
| 3 | **Onderhoud + reparatie zoeker** | Vertrouwde vaste garage | Onderhoud |
| 4 | **Banden- en seizoenswissel** | Banden + opslag | Banden & wielen |
| 5 | **Zakelijk / kleine wagenparken** (groei-doelgroep) | Vaste partner voor lease/leaseteruggave | (later) Zakelijk |

## 4. Conversie-doelen op de site (in volgorde)

1. **Bel ons** - telefoon prominent in header (sticky), op elke pagina, op mobile als tap-to-call.
2. **Afspraak inplannen** - formulier of (later) booking-widget.
3. **Offerte aanvragen** - voor reparaties / specialistisch werk.
4. **Routebeschrijving** - Google Maps embed + adres-CTA.
5. **WhatsApp** - moderne, drempelverlagende klantroute (optioneel maar sterk).

## 5. Sitemap (v1 launch)

```
/                                  Home
/diensten/apk                      APK-keuring Apeldoorn
/diensten/onderhoud                Algemeen onderhoud
/diensten/specialistisch           Specialistisch onderhoud / Diagnose ⭐ topprio
/diensten/banden-en-wielen         Banden & wielen
/diensten/airco-service            (sub van onderhoud, of eigen pagina)
/diensten/schadeherstel            Schade
/diensten/tuning                   Tuning (kort, niet-prominent)
/over-ons                          Verhaal, team, werkplaats
/reviews                           Klantbeoordelingen
/contact                           Contact + afspraak
/afspraak                          Afspraak-formulier (kan ook /contact zijn)
```

**SEO-haakjes**: alle dienstpagina's krijgen `[dienst] Apeldoorn`-targeting in title + H1. Eén lokale vestigingspagina is genoeg (1 vestiging), maar `/apeldoorn-zuid`-vermelding op homepage en in schema.

## 6. Content-blokken per pagina (v1)

### Home
1. Hero: krachtige claim + 2 CTAs (Bel / Afspraak) + foto werkplaats
2. USP-strip (4 iconen): RDW erkend · Sinds 2013 · Specialist diagnose · Eerlijk advies
3. Diensten-grid (4 cards): APK · Onderhoud · Specialistisch · Banden
4. "Waarom All-Cars Specialist" - kerngedachte uitgelegd, met klantcitaat
5. Reviews-block (Google reviews via API of statisch)
6. Mini "Over ons" - werkplaatsfoto + kort verhaal
7. Contact + Maps + openingstijden + grote bel-CTA
8. Footer

### Specialistisch onderhoud (belangrijkste SEO-pagina)
1. Hero: "Vastgelopen diagnose? Wij lossen het op."
2. Voor wie: lijst van symptomen ("foutmelding die niet weggaat", "trillingen", "olielekkage", "EV-laadprobleem", "motormanagement", "ABS/airbag")
3. Hoe wij werken: stappenplan in 3-4 stappen (uitlezen → meten → diagnose → herstel)
4. Waar wij in gespecialiseerd zijn: merk-/systeem-blokjes
5. Citaat van garage-collega of klant
6. CTA: "Stuur foto van foutmelding via WhatsApp" + "Bel direct"

### APK
- Wat is APK, wat doen wij extra (gratis 30-puntencheck)
- Prijs transparant
- Direct inplannen
- Veelgestelde vragen (FAQ → schema markup voor zoekresultaten)

(Andere dienstpagina's volgen vergelijkbaar patroon: pijn → oplossing → bewijs → CTA)

## 7. Design concept

### Kleurenpalet (uit logo)

| Token | Hex | Gebruik |
|-------|-----|---------|
| `--brand-red` | `#E11D2E` | Primair accent, CTA's, hover, highlights, logo |
| `--brand-red-dark` | `#B7141F` | Hover-state, donkere variant |
| `--ink` | `#0F0F10` | Headings, sterke tekst |
| `--ink-2` | `#2A2A2D` | Body-tekst |
| `--muted` | `#6B7280` | Secundaire tekst |
| `--line` | `#E5E7EB` | Borders, dividers |
| `--surface` | `#FFFFFF` | Achtergrond |
| `--surface-2` | `#F7F7F8` | Sectie-achtergrond afwisselend |
| `--surface-dark` | `#0F0F10` | Donkere secties (hero, CTA-strip) |
| `--accent-yellow` | `#FFC107` | Sparingly: badges, "spoed" labels (optioneel) |

**Visuele richting**: modern & strak, witte achtergrond met krachtige rode accenten. Donkere sectie(s) voor contrast (hero of CTA-blok). Geen gradient-spelletjes, geen drop-shadows-overload - clean, professioneel, vertrouwd.

### Typografie

- **Headings**: `Barlow Condensed` (700/800) - krachtig, technisch, automotive-feel
- **Body**: `Inter` (400/500/600) - modern, leesbaar
- **Numerals**: tabular voor prijzen/openingstijden

### Components-stijl

- Knoppen: solide rode primary (`#E11D2E`), zwart secondary outline; rounded-md (6px), niet rond.
- Cards: witte achtergrond, 1px lichte border (`--line`), hover: lichte schaduw + lichte rode bovenrand-accent.
- Iconen: monoline (Lucide) - niet gekleurd, alleen line, in `--ink` of `--brand-red` op hover.
- Foto's: eigen werkplaatsfoto's (laten maken!) - geen stockfoto's. Tot dat moment: hoogwaardige stock met menselijke monteurs.
- Spacing: ruim (8/12/16/24/32/48/64/96 px schaal).
- Breekpunten: 360 / 768 / 1024 / 1280.

### Logo-update (advies)

Het huidige logo is functioneel maar gedateerd (cursief italic, twee blokken, rommelige hiërarchie). Aanbevelingen:
- **Behouden**: rode kleur, gelaagde structuur (merknaam + activiteit)
- **Verfrissen**: cleane sans-serif (Barlow Condensed of vergelijkbaar), strakkere uitlijning, minder schaduwwerking, mogelijk los pictogram (steeksleutel/chassis-silhouet) voor favicon en social
- **Variant**: zowel een full-logo (horizontaal) als een compact icoon-only versie (favicon/avatar)
- **Afgeleide**: zwart-wit-versie + omgekeerde versie voor donkere achtergronden

Niet meteen mee aan de slag - eerst de site, dan het logo polijsten zodra de richting staat.

## 8. Tech-blueprint

### Stack
- **Framework**: Next.js 15 (App Router, RSC)
- **Styling**: Tailwind CSS v4 + design tokens als CSS-variabelen
- **Components**: shadcn/ui voor base components (Button, Input, Dialog, Accordion voor FAQ)
- **Hosting**: Vercel (auto-deploy van GitHub `main`)
- **Database**: Supabase - alleen voor formulier-inzendingen (afspraak, contact, offerte) en eventueel reviews-cache
- **Formulieren**: server actions → Supabase → e-mail naar info@all-cars-specialist.nl via Resend (of Supabase Functions + SMTP)
- **Analytics**: Vercel Analytics + Plausible (privacy-vriendelijk, geen cookie-banner gedoe)
- **Images**: `next/image` met WebP/AVIF, lazy-loaded
- **Schema.org**: `LocalBusiness` + `AutoRepair` op homepage; `FAQPage` op APK-pagina; `Service` per dienstpagina

### Repository-structuur (voorstel)
```
all-cars-specialist/
├── app/
│   ├── layout.tsx          (header, footer, fonts, schema)
│   ├── page.tsx            (home)
│   ├── diensten/
│   │   ├── apk/page.tsx
│   │   ├── onderhoud/page.tsx
│   │   ├── specialistisch/page.tsx
│   │   └── banden-en-wielen/page.tsx
│   ├── over-ons/page.tsx
│   ├── contact/page.tsx
│   └── api/
│       └── afspraak/route.ts  (server action handler)
├── components/
│   ├── header.tsx
│   ├── hero.tsx
│   ├── service-card.tsx
│   └── ...
├── lib/
│   └── supabase.ts
├── public/
│   └── images/
└── tailwind.config.ts
```

### Deploy-flow
1. Lokaal ontwikkelen → push naar `main` op GitHub.
2. Vercel auto-deploys preview op elke PR + production op `main`.
3. Custom domain `all-cars-specialist.nl` → A/CNAME naar Vercel.
4. Supabase project (eu-west) voor formulier-data.

## 9. Roadmap (advies)

| Fase | Duur | Resultaat |
|------|------|-----------|
| **0. Akkoord op strategie + design** | nu (deze sessie) | Strategiedoc + hero-mockup vastgesteld |
| **1. Visueel concept volledig** | 1 sessie | Volledige homepage-mockup + 1 dienstpagina-mockup als HTML |
| **2. Foto-shoot werkplaats** | 1 dag (extern) | 15-25 eigen foto's: gevel, werkplaats, monteurs, brug, diagnose-apparatuur |
| **3. Build v1 (homepage + 4 dienstpagina's + contact)** | 3-5 dagen | Live op Vercel staging, klant-reviewbaar |
| **4. Content polishing + SEO-optimalisatie** | 1-2 dagen | Schema, meta, internal linking, sitemap.xml, robots.txt |
| **5. Go-live + DNS-cutover** | halve dag | Live op `all-cars-specialist.nl` |
| **6. Lokale SEO-push (na launch)** | doorlopend | Google Business Profile-optimalisatie, citations, review-flow |

## 10. Wat heb ik van Peter/de klant nodig

- [ ] Telefoonnummer + correcte openingstijden (uit GBP halen)
- [ ] 5-10 echte klantcitaten (uit Google Reviews) - mag ik anonimiseren waar nodig
- [ ] Akkoord op de "specialist"-positionering en de claim "De garage waar zelfs garages naartoe komen"
- [ ] Lijst van merken/systemen waar ze écht in uitblinken (voor specialistisch-pagina)
- [ ] APK-prijs + indicatie kosten standaard onderhoudsbeurt
- [ ] Toestemming voor foto-shoot (week ernaartoe naar afspraak)
- [ ] Eventuele bestaande logo-bestanden (hoge resolutie / vector)

---

**Bijlage**: `all-cars-specialist-mockup.html` - werkende visuele mockup van homepage in nieuwe stijl, openbaar in browser.
