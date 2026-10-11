#!/usr/bin/env python3
"""
Build alle HTML-pagina's voor de All-Cars Specialist site.
Output → /sessions/modest-elegant-shannon/mnt/all-cars-specialist/
"""
import os, json, textwrap

OUT = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://all-cars-specialist.nl"

# Cache-bust: hash of styles.css (recomputed each build)
def _compute_styles_version():
    import hashlib
    css_path = os.path.join(OUT, "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    return "1"
STYLES_VERSION = _compute_styles_version()


# ---------- WHATSAPP FLOATING CTA ----------
import urllib.parse as _urlparse

WA_PHONE = "31633935720"
WA_TEMPLATES = {}
_WA_DEFAULT = "Goedendag, ik heb een vraag voor All Cars Specialist die ik graag per Whatsapp deel."

REVIEW_CARDS = '''      <article class="review">
        <div class="stars" aria-label="Beoordeling 5 van 5">
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
        </div>
        <p>"Uitstekende service, werkt snel en efficiënt, een echte aanrader."</p>
        <div class="author">
          <span class="avatar" aria-hidden="true">EG</span>
          <div><strong>Edgaras Gedmintas</strong><br>Februari 2025 · Google review</div>
        </div>
      </article>

      <article class="review">
        <div class="stars" aria-label="Beoordeling 5 van 5">
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
        </div>
        <p>"Topmonteur."</p>
        <div class="author">
          <span class="avatar" aria-hidden="true">RT</span>
          <div><strong>Rens Tiekstra</strong><br>Vorig jaar · Google review</div>
        </div>
      </article>

      <article class="review">
        <div class="stars" aria-label="Beoordeling 5 van 5">
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
        </div>
        <p>"Vlot en netjes geholpen, kundig en niet duur. Echt top."</p>
        <div class="author">
          <span class="avatar" aria-hidden="true">MS</span>
          <div><strong>Marjolein Smit</strong><br>Eerder · Google review</div>
        </div>
      </article>

      <article class="review">
        <div class="stars" aria-label="Beoordeling 5 van 5">
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
        </div>
        <p>"Geweldige garage. Echte vakmensen die denken in oplossingen. Eerlijke nota en geen verrassingen. Aanrader."</p>
        <div class="author">
          <span class="avatar" aria-hidden="true">FH</span>
          <div><strong>Fred Hartgers</strong><br>Eerder · Google review</div>
        </div>
      </article>

      <article class="review">
        <div class="stars" aria-label="Beoordeling 4 van 5">
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
        </div>
        <p>"Mijn FFCC gaf elke keer storing, steeds weer wat anders. Niemand kon mij helpen, behalve dit bedrijf. Na lang zoeken kwamen zij erachter dat mijn teller kapot was. Professioneel gerepareerd."</p>
        <div class="author">
          <span class="avatar" aria-hidden="true">HM</span>
          <div><strong>Henk Marijnus</strong><br>Eerder · Google review</div>
        </div>
      </article>

      <article class="review">
        <div class="stars" aria-label="Beoordeling 5 van 5">
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
          <svg viewBox="0 0 24 24"><path d="M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
        </div>
        <p>"Nieuwe APK en bijbehorende reparaties goed uitgevoerd. En dat dan ook nog eens € 1.600 goedkoper dan dat ik bij de merkdealer als offerte had gekregen."</p>
        <div class="author">
          <span class="avatar" aria-hidden="true">PJ</span>
          <div><strong>Paul van Jaarsveld</strong><br>Eerder · Google review</div>
        </div>
      </article>'''

def wa_widget(slug):
    msg = WA_TEMPLATES.get(slug, _WA_DEFAULT)
    encoded = _urlparse.quote(msg, safe="")
    return (
        '<a class="wa-float" '
        f'href="https://wa.me/{WA_PHONE}?text={encoded}" '
        'target="_blank" rel="noopener noreferrer" '
        'aria-label="Stuur ons een bericht via WhatsApp" '
        'data-wa-cta="true">'
        '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>'
        '</svg>'
        '<span class="wa-tooltip"><strong>WhatsApp</strong>Stuur ons een bericht</span>'
        '</a>'
    )


# ---------- LOGO ----------
# Vervangen door echte PNG; LOGO_SYMBOL niet meer nodig
LOGO_SYMBOL = ""

# ---------- TOPBAR + HEADER ----------
def header(active="home"):
    items = [
        ("home", "/", "Home"),
        ("diensten", "#diensten", "Diensten"),  # placeholder, see below
        ("specialist", "/specialistisch", "Specialist"),
        ("over-ons", "/over-ons", "Over ons"),
        ("contact", "/contact", "Contact"),
    ]
    # Dropdown vervangen door simpele links naar belangrijkste diensten
    nav_links = [
        ("home", "/", "Home"),
        ("apk", "/apk", "APK"),
        ("onderhoud", "/onderhoud", "Onderhoud"),
        ("specialistisch", "/specialistisch", "Specialist"),
        ("banden", "/banden", "Banden"),
        ("contact", "/contact", "Contact"),
    ]
    nav_html = ""
    for key, href, label in nav_links:
        cls = ' class="active"' if key == active else ""
        nav_html += f'<a href="{href}"{cls}>{label}</a>\n      '
    return f'''<div class="topbar">
  <div class="container">
    <div>
      <span>📍 Surinameweg 33, Apeldoorn-Zuid</span>
      <span class="pipe">|</span>
      <span>Ma–Vr 09:00–17:00</span>
    </div>
    <div>
      <a href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">💬 WhatsApp: 06 33 93 57 20</a>
      <span class="pipe">|</span>
      <a href="mailto:info@all-cars-specialist.nl">✉ info@all-cars-specialist.nl</a>
    </div>
  </div>
</div>

<header class="header">
  <div class="container">
    <a href="/" aria-label="All-Cars Specialist B.V. - naar home">
      <picture><source type="image/webp" srcset="/logo-1x.webp 1x, /logo-2x.webp 2x, /logo-3x.webp 3x"><img class="acs-logo" src="/logo-1x.png" srcset="/logo-1x.png 1x, /logo-2x.png 2x, /logo-3x.png 3x" alt="All-Cars Specialist B.V. - Onderhoud & Reparatie" width="280" height="40" decoding="async"></picture>
    </a>
    <nav class="nav">
      {nav_html.strip()}
    </nav>
    <div class="header-cta">
      <a class="btn btn-outline" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">
        <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
        WhatsApp
      </a>
      <a class="btn btn-primary" href="/contact">Afspraak</a>
      <button class="nav-toggle" aria-label="Menu openen of sluiten" aria-expanded="false">
        <svg class="icon-open" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>
        <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="6" y1="18" x2="18" y2="6"/></svg>
      </button>
    </div>
  </div>
</header>\n<main>'''

# ---------- CONTACT CTA ----------
CONTACT_CTA = '''<section class="contact-cta">
  <div class="container">
    <div>
      <h2>Afspraak maken</h2>
      <p>Stuur een appje of plan online. We nemen zo snel mogelijk contact op.</p>
    </div>
    <div class="btns">
      <a class="btn btn-primary btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">💬 WhatsApp ons</a>
      <a class="btn btn-outline btn-lg" href="/contact">Afspraak inplannen →</a>
    </div>
  </div>
</section>'''

# ---------- FOOTER ----------
FOOTER = '''</main>\n<footer class="footer">
  <div class="container">
    <div class="grid">
      <div>
        <div class="footer-brand">
          <span class="footer-name">All-Cars-Specialist <em>B.V.</em></span><br>
          <span class="footer-sub"><span>Onderhoud &amp; Reparatie</span></span>
        </div>
        <p style="color:#8A8A92; font-size:13.5px; margin-top:12px;">
          Universele garage in Apeldoorn-Zuid. Onderhoud, APK, banden, airco, schadeherstel en specialistisch werk. Sinds 2013.
        </p>
      </div>
      <div>
        <h2 class="footer-title">Diensten</h2>
        <ul>
          <li><a href="/apk">APK-keuring</a></li>
          <li><a href="/onderhoud">Onderhoud &amp; reparatie</a></li>
          <li><a href="/specialistisch">Specialistisch onderhoud</a></li>
          <li><a href="/banden">Banden &amp; wielen</a></li>
          <li><a href="/airco">Airco-service</a></li>
          <li><a href="/schadeherstel">Schadeherstel</a></li>
          <li><a href="/aankoopkeuring">Aankoopkeuring</a></li>
          <li><a href="/distributieriem-vervangen">Distributieriem vervangen</a></li>
          <li><a href="/versnellingsbakolie-verversen">Versnellingsbakolie verversen</a></li>
          <li><a href="/foutmelding-uitlezen">Foutmelding uitlezen</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-title">Bedrijf</h2>
        <ul>
          <li><a href="/over-ons">Over ons</a></li>
          <li><a href="/contact">Contact</a></li>
          <li><a href="/contact#openingstijden">Openingstijden</a></li>
          <li><a href="/garage-beekbergen">Garage Beekbergen</a></li>
          <li><a href="/garage-twello">Garage Twello</a></li>
          <li><a href="/garage-vaassen">Garage Vaassen</a></li>
          <li><a href="/garage-loenen">Garage Loenen</a></li>
          <li><a href="/garage-klarenbeek">Garage Klarenbeek</a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer-title">Contact</h2>
        <ul>
          <li>Surinameweg 33</li>
          <li>7333 PC Apeldoorn</li>
          <li><a href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp: 06 33 93 57 20</a></li>
          <li><a href="mailto:info@all-cars-specialist.nl">info@all-cars-specialist.nl</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© 2026 All-Cars Specialist B.V. - Alle rechten voorbehouden</span>
      <span><a href="/privacyverklaring">Privacyverklaring</a> · <a href="/algemene-voorwaarden">Algemene voorwaarden</a> · KvK 56939485 · Vibe coded by <a href="https://nextdayonline.nl">nextdayonline.nl</a></span>
    </div>
  </div>
</footer>'''

# ---------- NAV TOGGLE JS ----------
NAV_JS = """<script>
(function() {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', function() {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  nav.addEventListener('click', function(e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    }
  });
})();
</script>"""


# ---------- LOCAL BUSINESS SCHEMA ----------
# Basis-schema staat op elke pagina; aggregateRating + reviews alleen op de
# homepage (rich results horen bij de entiteit, niet bij elke subpagina).
_LOCAL_SCHEMA_HEAD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AutoRepair",
  "name": "All-Cars Specialist B.V.",
  "image": "https://all-cars-specialist.nl/og-image.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Surinameweg 33",
    "addressLocality": "Apeldoorn",
    "postalCode": "7333 PC",
    "addressCountry": "NL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 52.1864,
    "longitude": 5.9523
  },
  "hasMap": "https://www.google.com/maps/search/?api=1&query=52.1864,5.9523",
  "telephone": "+31633935720",
  "email": "info@all-cars-specialist.nl",
  "url": "https://all-cars-specialist.nl",
  "sameAs": [
    "https://share.google/cpPfnH02v4F3mFdFh",
    "https://g.page/r/Ca6jilmVWAZBEAE"
  ],
  "priceRange": "€€",
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00",
    "closes": "17:00"
  }],
  "areaServed": [
    {"@type": "City", "name": "Apeldoorn"},
    {"@type": "Place", "name": "Apeldoorn-Zuid"},
    {"@type": "City", "name": "Beekbergen"},
    {"@type": "City", "name": "Loenen"},
    {"@type": "City", "name": "Vaassen"},
    {"@type": "City", "name": "Klarenbeek"},
    {"@type": "City", "name": "Twello"}
  ],
  "foundingDate": "2013"'''

_LOCAL_SCHEMA_RATING = ''',
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": 33,
    "bestRating": "5",
    "worstRating": "1"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "author": {"@type": "Person", "name": "Edgaras Gedmintas"},
      "reviewBody": "Uitstekende service, werkt snel en efficiënt, een echte aanrader."
    },
    {
      "@type": "Review",
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "author": {"@type": "Person", "name": "Rens Tiekstra"},
      "reviewBody": "Topmonteur."
    },
    {
      "@type": "Review",
      "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
      "author": {"@type": "Person", "name": "Marjolein Smit"},
      "reviewBody": "Vlot en netjes geholpen, kundig en niet duur. Echt top."
    }
  ]'''

_LOCAL_SCHEMA_TAIL = '''
}
</script>'''

def local_schema(slug=""):
    rating = _LOCAL_SCHEMA_RATING if slug in ("", "index") else ""
    return _LOCAL_SCHEMA_HEAD + rating + _LOCAL_SCHEMA_TAIL

# ---------- HTML SHELL ----------
def page(title, description, body, slug="", active="home", extra_schema=""):
    canonical_url = BASE_URL if slug in ("", "index") else f"{BASE_URL}/{slug}"
    og_type = "website" if slug in ("", "index") else "article"
    # 404: noindex en geen canonical; alle andere pagina's een canonical
    if slug == "404":
        robots_canonical = '<meta name="robots" content="noindex">'
    else:
        robots_canonical = f'<link rel="canonical" href="{canonical_url}">'
    # LCP: preload van de hero-image, alleen op de homepage.
    # imagesrcset/imagesizes matchen exact met de <picture> in HOME_BODY.
    hero_preload = ""
    if slug in ("", "index"):
        hero_preload = '\n<link rel="preload" as="image" imagesrcset="/werkplaats-all-cars-specialist-419w.webp 419w, /werkplaats-all-cars-specialist-838w.webp 838w, /werkplaats-all-cars-specialist-1257w.webp 1257w" imagesizes="(max-width: 900px) 100vw, 50vw">'
    return f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="{BASE_URL}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="All-Cars Specialist B.V.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{BASE_URL}/og-image.png">
{robots_canonical}
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,600;0,700;0,800;0,900;1,800;1,900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v={STYLES_VERSION}">{hero_preload}
{local_schema(slug)}
{extra_schema}
</head>
<body>
{LOGO_SYMBOL}
{header(active)}
{body}
{CONTACT_CTA}
{wa_widget(slug)}
{FOOTER}
{NAV_JS}
</body>
</html>'''



# ---------- PER-PAGE SCHEMA's ----------
def service_schema(name, description, slug):
    return f"""<script type=\"application/ld+json\">
{{
  \"@context\": \"https://schema.org\",
  \"@type\": \"Service\",
  \"serviceType\": \"{name}\",
  \"name\": \"{name} bij All-Cars Specialist Apeldoorn\",
  \"description\": \"{description}\",
  \"provider\": {{
    \"@type\": \"AutoRepair\",
    \"name\": \"All-Cars Specialist B.V.\",
    \"telephone\": \"+31633935720\",
    \"address\": {{
      \"@type\": \"PostalAddress\",
      \"streetAddress\": \"Surinameweg 33\",
      \"addressLocality\": \"Apeldoorn\",
      \"postalCode\": \"7333 PC\",
      \"addressCountry\": \"NL\"
    }}
  }},
  \"areaServed\": [
    {{\"@type\": \"City\", \"name\": \"Apeldoorn\"}},
    {{\"@type\": \"City\", \"name\": \"Beekbergen\"}},
    {{\"@type\": \"City\", \"name\": \"Loenen\"}},
    {{\"@type\": \"City\", \"name\": \"Vaassen\"}},
    {{\"@type\": \"City\", \"name\": \"Klarenbeek\"}},
    {{\"@type\": \"City\", \"name\": \"Twello\"}}
  ],
  \"url\": \"{BASE_URL}/{slug}\"
}}
</script>"""

FAQ_APK_SCHEMA = """<script type=\"application/ld+json\">
{
  \"@context\": \"https://schema.org\",
  \"@type\": \"FAQPage\",
  \"mainEntity\": [
    {
      \"@type\": \"Question\",
      \"name\": \"Wanneer moet mijn auto APK?\",
      \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"De eerste APK is vanaf 4 jaar na datum eerste toelating voor benzine en hybride, en vanaf 3 jaar voor diesel. Daarna jaarlijks vanaf 8 jaar (benzine/hybride) of jaarlijks (diesel). Stuur ons je kenteken via WhatsApp en we zoeken het voor je op.\"}
    },
    {
      \"@type\": \"Question\",
      \"name\": \"Wat kost een APK-keuring?\",
      \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Onze APK-prijs is transparant en vast. Stuur ons een appje of mail voor het exacte tarief. Eventuele reparaties die nodig zijn, bespreken we vooraf en pakken we pas aan als je akkoord bent.\"}
    },
    {
      \"@type\": \"Question\",
      \"name\": \"Hoelang duurt de keuring?\",
      \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Een APK duurt doorgaans rond een uur als alles in orde is. App ons even voor het exacte tijdslot bij jouw afspraak.\"}
    },
    {
      \"@type\": \"Question\",
      \"name\": \"Wat als mijn auto wordt afgekeurd?\",
      \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Dan bespreken we wat er moet gebeuren en wat het gaat kosten. Reparaties voeren we alleen uit als jij akkoord bent; herkeuring volgt zodra het werk klaar is.\"}
    },
    {
      \"@type\": \"Question\",
      \"name\": \"Kunnen kleine reparaties direct mee?\",
      \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Kleine zaken zoals ruitenwisserbladen, lampjes of bandenspanning kunnen we vaak meteen oplossen. Bij grotere reparaties plannen we een vervolgafspraak en geven we vooraf een offerte.\"}
    },
    {
      \"@type\": \"Question\",
      \"name\": \"Kan ik dezelfde dag een afspraak maken?\",
      \"acceptedAnswer\": {\"@type\": \"Answer\", \"text\": \"Soms wel. App ons even en we kijken wat er die dag past. Voor zekerheid raden we aan een paar dagen vooruit in te plannen.\"}
    }
  ]
}
</script>"""

# ---------- GENERIEKE FAQ (zichtbaar blok + FAQPage-schema uit dezelfde data) ----------
import html as _html

def faq_schema(qas):
    items = []
    for q, a in qas:
        items.append(
            "    {\n"
            "      \"@type\": \"Question\",\n"
            f"      \"name\": {json.dumps(q, ensure_ascii=False)},\n"
            f"      \"acceptedAnswer\": {{\"@type\": \"Answer\", \"text\": {json.dumps(a, ensure_ascii=False)}}}\n"
            "    }"
        )
    return (
        "<script type=\"application/ld+json\">\n"
        "{\n"
        "  \"@context\": \"https://schema.org\",\n"
        "  \"@type\": \"FAQPage\",\n"
        "  \"mainEntity\": [\n"
        + ",\n".join(items) + "\n"
        "  ]\n"
        "}\n"
        "</script>"
    )

def faq_html(eyebrow, heading, qas, alt=False):
    rows = []
    for q, a in qas:
        rows.append(
            "      <details>\n"
            f"        <summary>{_html.escape(q, quote=False)}</summary>\n"
            f"        <div class=\"answer\"><p>{_html.escape(a, quote=False)}</p></div>\n"
            "      </details>"
        )
    section_cls = "section-tight section-alt" if alt else "section-tight"
    return (
        f"\n<section class=\"{section_cls}\">\n"
        "  <div class=\"container container-narrow\">\n"
        "    <div class=\"section-header left\">\n"
        f"      <span class=\"eyebrow\">{eyebrow}</span>\n"
        f"      <h2>{heading}</h2>\n"
        "    </div>\n"
        "    <div class=\"faq\">\n"
        + "\n".join(rows) + "\n"
        "    </div>\n"
        "  </div>\n"
        "</section>"
    )

# FAQ-content per dienstpagina. Conservatief geformuleerd: geen prijzen of
# specifieke beloften die nog niet door Peter bevestigd zijn (zie claims-audit.md).
FAQS = {
    "onderhoud": ("Veelgestelde vragen", "Onderhoudsvragen die we vaak krijgen", [
        ("Wat is het verschil tussen een kleine en een grote beurt?",
         "Bij een kleine beurt verversen we de olie en het oliefilter en lopen we de standaard controlepunten na. Bij een grote beurt komen daar onder meer het lucht- en interieurfilter, de bougies en een uitgebreidere controle van remmen en ophanging bij. Wat jouw auto nodig heeft, hangt af van het merk, de kilometerstand en het onderhoudsschema van de fabrikant."),
        ("Hoe vaak moet mijn auto onderhoud?",
         "De meeste fabrikanten schrijven onderhoud voor per jaar of per aantal kilometers, vaak ergens tussen de 15.000 en 30.000 km. Rijd je weinig, dan telt vooral de tijd: ook een auto die stilstaat heeft jaarlijks verse olie nodig. Twijfel je? Geef je kenteken door, dan kijken we het interval voor je na."),
        ("Behoud ik mijn fabrieksgarantie bij een onafhankelijke garage?",
         "Ja. Door de Europese groepsvrijstelling voor motorvoertuigen mag je onderhoud laten doen bij een onafhankelijke garage zonder je fabrieksgarantie te verliezen, zolang het werk volgens de voorschriften van de fabrikant gebeurt en met onderdelen van gelijke kwaliteit. Wij werken volgens die voorschriften en houden het bij in de onderhoudshistorie."),
        ("Wat kost een onderhoudsbeurt?",
         "Dat hangt af van het type beurt en je auto. App of mail ons met je kenteken voor een prijsindicatie. Je krijgt vooraf een heldere opgave en we voeren geen werk uit waar je niet van weet."),
    ]),
    "specialistisch": ("Veelgestelde vragen", "Vragen over diagnose en specialistisch werk", [
        ("Wat kost een diagnose?",
         "Een diagnose kost tijd op de uitleesapparatuur en aan de meetbank. App of mail ons met je klacht, dan geven we een indicatie van wat het zoeken kost. Je hoort vooraf waar je aan toe bent voordat we beginnen."),
        ("Mijn foutmelding komt steeds terug na het wissen, wat betekent dat?",
         "Een foutmelding die terugkomt, betekent dat het onderliggende probleem nog niet is opgelost; de auto registreert de fout opnieuw. Wissen helpt dan niet. Wij zoeken de oorzaak met uitleesapparatuur en metingen, zodat we het bij de bron aanpakken in plaats van het lampje te resetten."),
        ("Kunnen jullie een storing vinden die een andere garage liet liggen?",
         "Vaak wel. We krijgen regelmatig auto's binnen waar elders al onderdelen voor zijn vervangen zonder resultaat. Onze aanpak is eerst zoeken en meten, dan pas vervangen. We kunnen niet beloven dat we alles oplossen, maar we zetten de diagnose methodisch op."),
        ("Hoelang duurt een diagnose?",
         "Dat verschilt per klacht. Een duidelijke foutcode is soms binnen een uur herleid; een storing die maar af en toe optreedt, vraagt meer tijd en soms een testrit. We laten je weten wat we verwachten zodra we de eerste meting hebben gedaan."),
    ]),
    "airco": ("Veelgestelde vragen", "Aircovragen die we vaak krijgen", [
        ("Hoe vaak moet ik mijn airco laten vullen?",
         "Een airco verliest elk jaar wat koelmiddel, gemiddeld zo'n 10 procent. Meestal is bijvullen elke twee tot drie jaar genoeg. Koelt de airco merkbaar minder of duurt het afkoelen langer, laat dan eerder controleren."),
        ("Waarom koelt mijn airco niet meer goed?",
         "Meestal zit er te weinig koelmiddel in, vaak door een klein lek. Soms ligt het aan het interieurfilter, de compressor of een verstopte condensor. We controleren het systeem en zoeken op waar het koelmiddel verdwijnt voordat we bijvullen."),
        ("Mijn airco ruikt muf, wat kan ik daaraan doen?",
         "Een muffe geur komt door bacterien en schimmel op de verdamper achter het dashboard. Een reiniging en een nieuw interieurfilter lossen dat meestal op. Vraag ernaar bij je afspraak."),
        ("Wat kost airco vullen?",
         "App of mail ons voor het tarief. Blijkt er een lek te zitten, dan bespreken we eerst wat de reparatie kost voordat we iets doen."),
    ]),
    "schadeherstel": ("Veelgestelde vragen", "Vragen over schadeherstel", [
        ("Kan ik bij jullie terecht voor kleine schade zoals krassen en deuken?",
         "Ja. Van een kras of parkeerdeuk tot bumper- en plaatwerk: app ons een foto van de schade, dan laten we weten wat er mogelijk is en wat het ongeveer kost."),
        ("Loopt schadeherstel via mijn verzekering?",
         "Heb je een cascoverzekering (allrisk of beperkt casco), dan valt veel schade onder je dekking. Neem contact met ons op met je gegevens bij de hand, dan kijken we samen hoe we het traject het beste aanpakken."),
        ("Repareren jullie ook schade die niet verzekerd is?",
         "Zeker. Voor niet-verzekerde schade maken we vooraf een eerlijke opgave, zodat je weet waar je aan toe bent voordat we beginnen."),
        ("Hoelang duurt een reparatie?",
         "Dat hangt af van de omvang van de schade en de levertijd van onderdelen. Een kleine reparatie kan vaak snel; voor groter plaatwerk plannen we een vaste periode in. Je hoort de verwachte doorlooptijd bij de offerte."),
    ]),
    "aankoopkeuring": ("Veelgestelde vragen", "Vragen over de aankoopkeuring", [
        ("Wat kost een aankoopkeuring?",
         "App of mail ons voor het tarief. Je weet vooraf wat de keuring kost, zodat er achteraf geen verrassingen zijn."),
        ("Hoelang duurt een aankoopkeuring?",
         "We geven je vooraf een inschatting van hoeveel tijd we nodig hebben. Bij twijfelpunten nemen we de tijd om door te meten en dat hoor je dan ook."),
        ("Kan ik een auto van een particulier laten keuren?",
         "Ja. Of je nu bij een particulier of een bedrijf koopt: maak met de verkoper een afspraak om de auto bij ons langs te brengen, dan keuren we hem."),
        ("Wat krijg ik na de keuring?",
         "Een heldere toelichting van de staat van de auto: wat is goed, wat is versleten en wat komt er op korte termijn aan. Met die informatie beslis jij zelf of je de auto koopt."),
        ("Moet de auto naar jullie werkplaats komen?",
         "Ja, we keuren in onze eigen werkplaats omdat we de auto dan op de brug en met uitleesapparatuur kunnen controleren. Stem even af wanneer het uitkomt."),
    ]),
    "distributieriem-vervangen": ("Veelgestelde vragen", "Vragen over de distributieriem", [
        ("Wanneer moet de distributieriem vervangen worden?",
         "Dat hangt af van je merk en model. Veel fabrikanten schrijven vervanging voor tussen de 60.000 en 120.000 km, of na vier tot zes jaar, wat het eerst komt. Geef je kenteken door, dan zoeken we het exacte interval op."),
        ("Wat gebeurt er als de distributieriem breekt?",
         "Bij de meeste motoren raken de zuigers dan de kleppen, met zware motorschade tot gevolg. Een reparatie is dan vaak duurder dan de auto waard is. Daarom is op tijd vervangen zoveel goedkoper dan wachten."),
        ("Moet de waterpomp tegelijk vervangen worden?",
         "Bij veel auto's wordt de waterpomp door de distributieriem aangedreven. Omdat het arbeidsloon dan grotendeels overlapt, is het meestal verstandig de waterpomp meteen mee te nemen. We adviseren per geval."),
        ("Heb ik een distributieriem of een distributieketting?",
         "Dat verschilt per motor. Een ketting gaat vaak langer mee, maar is niet onderhoudsvrij. Twijfel je wat jouw auto heeft? Geef je kenteken door, dan zoeken we het op."),
        ("Wat kost een distributieriem vervangen?",
         "Dat verschilt sterk per auto en of de waterpomp meegaat. App of mail ons met je kenteken voor een prijsindicatie; je krijgt vooraf een heldere offerte."),
    ]),
    "versnellingsbakolie-verversen": ("Veelgestelde vragen", "Vragen over versnellingsbakolie", [
        ("Hoe vaak moet versnellingsbakolie ververst worden?",
         "Bij een handgeschakelde bak is rond de 100.000 kilometer een goed moment, eerder bij trekhaakgebruik of veel korte ritten. Voor automaten adviseren veel fabrikanten elke 60.000 tot 80.000 kilometer, inclusief filter. Geef je kenteken door, dan zoeken we het voorschrift voor jouw bak op."),
        ("Mijn automaat heeft 'lifetime' olie, moet die dan toch ververst worden?",
         "'Lifetime' betekent in de praktijk: de levensduur die de fabrikant voor de bak rekent. De olie slijt intussen gewoon. Automaten met op tijd ververste olie schakelen soepeler en gaan langer mee. We adviseren per geval, op basis van kilometerstand en gebruik."),
        ("Wat merk ik van versleten versnellingsbakolie?",
         "Stroef of krakend schakelen bij een koude motor, een automaat die schokt of te laat schakelt, of een brom die met de snelheid meeloopt. Ook donkere, verbrand ruikende olie op de peilstok van de automaat is een teken. Twijfel je? We beoordelen de olie voordat we iets vervangen."),
        ("Wat kost versnellingsbakolie verversen?",
         "Dat hangt af van het type bak en de hoeveelheid olie; een automaat vraagt meer olie en vaak een nieuw filter. App of mail ons met je kenteken, dan krijg je vooraf een heldere prijs."),
        ("Kan verversen kwaad bij een automaat met hoge kilometerstand?",
         "Verversen kan vrijwel altijd. Alleen agressief spoelen van een automaat die nooit onderhouden is, raden we soms af. We kijken eerst naar de staat van de olie en adviseren dan eerlijk wat zinvol is."),
        ("Verversen jullie ook differentieelolie?",
         "Ja. Ook de olie van het differentieel en van de tussenbak bij vierwielaandrijving verversen we. Dat is goed te combineren met de versnellingsbakolie of met een beurt."),
    ]),
    "foutmelding-uitlezen": ("Veelgestelde vragen", "Vragen over foutmeldingen uitlezen", [
        ("Wat kost het uitlezen van een foutcode?",
         "App of mail ons voor het tarief. Blijkt er meer onderzoek nodig, dan bespreken we dat eerst voordat we verdergaan."),
        ("Mijn motorlampje brandt, mag ik nog doorrijden?",
         "Een oranje motorlampje betekent meestal: laat het op korte termijn nakijken, vaak kun je nog voorzichtig verder. Knippert het lampje of is het rood, stop dan en stuur ons direct een appje; doorrijden kan dan schade veroorzaken."),
        ("Het lampje ging vanzelf weer uit, hoef ik niets te doen?",
         "Niet per se. Een storing kan tijdelijk verdwijnen terwijl het probleem blijft, en de foutcode staat vaak nog in het geheugen. Laat het uitlezen om zeker te weten of er iets speelt."),
        ("Lossen jullie de storing ook meteen op?",
         "Uitlezen geeft een richting, geen kant-en-klare conclusie. Soms is de oorzaak meteen duidelijk en lossen we het direct op; bij hardnekkige storingen meten we verder via ons specialistisch onderhoud."),
        ("Kan ik langskomen zonder afspraak?",
         "Stuur even een appje, dan kijken we of het die dag past. Met een afspraak ben je doorgaans sneller geholpen."),
    ]),
    "garage-beekbergen": ("Veelgestelde vragen", "Vragen van klanten uit Beekbergen", [
        ("Hoe ver is het van Beekbergen naar jullie garage?",
         "Vanaf het centrum van Beekbergen rijd je in ongeveer tien minuten naar de Surinameweg in Apeldoorn-Zuid. We liggen vlak bij de uitvalswegen, dus makkelijk te bereiken."),
        ("Kan ik mijn auto brengen en weer ophalen?",
         "Ja. Maak een afspraak, dan stemmen we af wanneer je de auto brengt. Voor de meeste klussen weet je nog dezelfde dag waar je aan toe bent."),
        ("Doen jullie ook APK voor auto's uit Beekbergen?",
         "Zeker. We regelen de APK via een vast keuringsstation en pakken benodigd onderhoud meteen mee. Geef je kenteken door, dan zoeken we je keuringsdatum op."),
        ("Voor welke merken kan ik terecht?",
         "We zijn een universele garage en werken voor alle merken, van een dagelijkse gezinsauto tot een auto met een hardnekkige storing die elders niet opgelost raakte."),
    ]),
    "garage-twello": ("Veelgestelde vragen", "Vragen van klanten uit Twello", [
        ("Hoe lang rijd ik van Twello naar jullie garage?",
         "Vanuit Twello ben je via de A1 in ongeveer twintig minuten bij de Surinameweg in Apeldoorn-Zuid. Goed te doen voor onderhoud of een diagnose-afspraak."),
        ("Waarom naar Apeldoorn-Zuid rijden als er garages dichterbij zijn?",
         "Veel klanten komen voor onze diagnose-aanpak: we zoeken en meten eerst, en vervangen pas daarna. Juist voor storingen die blijven terugkomen, is dat het verschil."),
        ("Kan ik terecht voor banden en seizoenswissel?",
         "Ja. De bandenwissel doen we bij ons in Apeldoorn-Zuid. Plan de wissel op tijd in het voor- en najaar, dan ben je snel klaar."),
        ("Hoe maak ik een afspraak vanuit Twello?",
         "Stuur een appje met je kenteken en je klacht of wens. We plannen je in en laten weten wat je kunt verwachten voordat je langskomt."),
    ]),
    "garage-vaassen": ("Veelgestelde vragen", "Vragen van klanten uit Vaassen", [
        ("Hoe lang is de rit van Vaassen naar jullie garage?",
         "Vanuit Vaassen ben je in ongeveer twintig minuten bij de Surinameweg in Apeldoorn-Zuid, via de N309 en de doorgaande wegen. Prima te doen voor onderhoud of een afspraak."),
        ("Zit ik bij jullie goed met elk merk?",
         "Ja, we zijn een universele garage en werken voor alle merken. Of je nu een gewone beurt nodig hebt of een lastige storing: we kijken wat jouw auto vraagt."),
        ("Kan ik er ook terecht voor APK?",
         "Zeker. We regelen de APK via een vast keuringsstation en pakken nodig onderhoud meteen mee. Geef je kenteken door, dan zoeken we je keuringsdatum op."),
        ("Hoe plan ik een afspraak vanuit Vaassen?",
         "Stuur een appje met je kenteken en wat er aan de hand is. We plannen je zo snel mogelijk in."),
    ]),
    "garage-loenen": ("Veelgestelde vragen", "Vragen van klanten uit Loenen", [
        ("Hoe ver is Loenen van jullie werkplaats?",
         "Vanaf Loenen rijd je in ongeveer een kwartier naar de Surinameweg in Apeldoorn-Zuid. Goed bereikbaar, ook voor wie het werk wil afwachten of de auto laat staan."),
        ("Waarvoor komen klanten uit Loenen naar jullie?",
         "Veel voor onze diagnose-aanpak bij storingen die blijven terugkomen, maar net zo goed voor gewoon onderhoud, APK en banden. Alles onder een dak."),
        ("Doen jullie onderhoud volgens fabrieksvoorschrift?",
         "Ja. We onderhouden volgens het schema van de fabrikant en houden het bij in de onderhoudshistorie, zodat je dat netjes op orde houdt."),
        ("Hoe maak ik een afspraak?",
         "App of mail ons met je kenteken en je wens. Je hoort wat je kunt verwachten voordat je langskomt."),
    ]),
    "garage-klarenbeek": ("Veelgestelde vragen", "Vragen van klanten uit Klarenbeek", [
        ("Hoe lang rijd ik van Klarenbeek naar jullie garage?",
         "Vanuit Klarenbeek ben je in ongeveer een kwartier bij de Surinameweg in Apeldoorn-Zuid. Een korte, rustige rit zonder druk centrumverkeer."),
        ("Zijn jullie een merkdealer?",
         "Nee, we zijn een onafhankelijke universele garage. We zitten niet vast aan een merk en kiezen wat het beste is voor jouw auto."),
        ("Kan ik banden laten wisselen?",
         "Ja, de bandenwissel doen we bij ons in Apeldoorn-Zuid. Plan hem op tijd in het voor- en najaar, dan ben je snel klaar."),
        ("Hoe plan ik een afspraak in?",
         "Stuur een appje met je kenteken en je klacht of wens, dan plannen we je in."),
    ]),
}

# Banden heeft al een zichtbare FAQ in de body; hier alleen het bijpassende schema
# (tekst gelijk aan de zichtbare antwoorden, zonder HTML-entiteiten).
BANDEN_FAQ = [
    ("Wanneer moet ik mijn banden wisselen?",
     "Bij een profieldiepte onder 1,6 mm is vervangen wettelijk verplicht, maar onder 3 mm zijn banden in de winter al onveilig. Wij meten gratis bij elke beurt en geven advies."),
    ("Heb ik per se winterbanden nodig?",
     "Winterbanden zijn in Nederland niet wettelijk verplicht, maar bij temperaturen onder 7 graden presteren zomerbanden minder. Voor wie veel rijdt of in heuvelig gebied woont, zijn ze een aanrader. Allseasonbanden kunnen een goed compromis zijn."),
    ("Mijn auto trilt, wat kan dat zijn?",
     "Meestal komt trillen door ongebalanceerde wielen, soms door een bobbel in een band of een verbogen velg. We meten op de balanceerbank en lossen het op."),
]

BREADCRUMB_HOME = ""
def breadcrumb_schema(slug, label):
    return f"""<script type=\"application/ld+json\">
{{
  \"@context\": \"https://schema.org\",
  \"@type\": \"BreadcrumbList\",
  \"itemListElement\": [
    {{\"@type\": \"ListItem\", \"position\": 1, \"name\": \"Home\", \"item\": \"{BASE_URL}/\"}},
    {{\"@type\": \"ListItem\", \"position\": 2, \"name\": \"{label}\", \"item\": \"{BASE_URL}/{slug}\"}}
  ]
}}
</script>"""

# ============================================================
# PAGES
# ============================================================

# ---------- HOME ----------
HOME_BODY = '''<!-- Hero -->
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Apeldoorn-Zuid &middot; sinds 2013</span>
        <h1>Universele garage in <span class="accent">Apeldoorn-Zuid.</span></h1>
        <p class="lead">
          Auto-onderhoud, APK, banden, airco, schadeherstel en diagnose voor alle merken.
          Sinds 2013 aan de Surinameweg in Apeldoorn-Zuid. Wij doen het werk in eigen
          werkplaats en bespreken vooraf wat het kost.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">
            Afspraak inplannen
            <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">
            <svg class="btn-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
            WhatsApp ons
          </a>
        </div>
        <div class="hero-trust">
          <div>Onafhankelijke <strong>universele</strong> garage</div>
          <div>Sinds <strong>2013</strong></div>
          <div>Alle merken</div>
        </div>
      </div>
      <div style="position:relative;">
        <div class="hero-visual">
          <picture><source type="image/webp" srcset="/werkplaats-all-cars-specialist-419w.webp 419w, /werkplaats-all-cars-specialist-838w.webp 838w, /werkplaats-all-cars-specialist-1257w.webp 1257w" sizes="(max-width: 900px) 100vw, 50vw"><img src="/werkplaats-all-cars-specialist-838w.jpg" srcset="/werkplaats-all-cars-specialist-419w.jpg 419w, /werkplaats-all-cars-specialist-838w.jpg 838w, /werkplaats-all-cars-specialist-1257w.jpg 1257w" sizes="(max-width: 900px) 100vw, 50vw" alt="Werkplaats van All-Cars Specialist in Apeldoorn-Zuid met drie hefbruggen" loading="eager" fetchpriority="high" decoding="async" width="1749" height="1004"></picture>
        </div>
        <div class="hero-badge">
          <span class="num">12+</span>
          <span class="lbl">Jaar ervaring</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- USPs -->
<div class="usps">
  <div class="container">
    <div class="usp">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>
      <div>
        <h2 class="usp-title">Universele garage</h2>
        <p>Voor alle merken. Geen merkdealer, geen keten.</p>
      </div>
    </div>
    <div class="usp">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
      <div>
        <h2 class="usp-title">Diagnose-apparatuur</h2>
        <p>Voor elektronische storingen en motormanagement.</p>
      </div>
    </div>
    <div class="usp">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v4"/><path d="M12 18v4"/><path d="M4.93 4.93l2.83 2.83"/><path d="M16.24 16.24l2.83 2.83"/><path d="M2 12h4"/><path d="M18 12h4"/></svg>
      <div>
        <h2 class="usp-title">Vooraf afgestemd</h2>
        <p>Prijsafspraak vooraf. Meerwerk altijd in overleg.</p>
      </div>
    </div>
    <div class="usp">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      <div>
        <h2 class="usp-title">Inplannen op afspraak</h2>
        <p>App of plan online. Spoed in overleg.</p>
      </div>
    </div>
  </div>
</div>

<!-- Geo-blok: Apeldoorn-Zuid + Surinameweg -->
<section class="section-tight" id="apeldoorn-zuid">
  <div class="container container-narrow">
    <div class="section-header left" style="max-width: 100%;">
      <span class="eyebrow">Apeldoorn-Zuid &middot; Surinameweg</span>
      <h2>Garage in Apeldoorn-Zuid voor &eacute;lk merk</h2>
      <p>Sinds 2013 zijn wij gevestigd aan de <strong>Surinameweg 33</strong> in Apeldoorn-Zuid -
      goed bereikbaar vanuit heel Apeldoorn en de omliggende dorpen. Wij werken voor
      particulieren en kleine zakelijke klanten.</p>
      <p style="margin-top: 12px;">Wat wij doen voor klanten in Apeldoorn-Zuid:</p>
      <ul class="checks-list" style="margin-top: 12px;">
        <li>Periodiek onderhoud volgens fabrieksvoorschrift - voor alle merken</li>
        <li>Reparatie en diagnose, ook voor klachten die andere garages laten liggen</li>
        <li>APK-keuring via een vast RDW-erkend partner-station - wij regelen de afspraak</li>
        <li>Banden, airco-service en schadeherstel</li>
        <li><a href="/versnellingsbakolie-verversen">Versnellingsbakolie verversen</a> - voor handbak, automaat, DSG en CVT</li>
        <li><a href="/aankoopkeuring">Aankoopkeuring</a> - voordat je een tweedehands auto koopt</li>
        <li>Werkplaats met ruime parkeermogelijkheid; geen druk centrum-verkeer</li>
      </ul>
      <p style="margin-top: 12px;">Ook een vaste garage voor de omliggende dorpen:
      <a href="/garage-beekbergen">garage voor Beekbergen</a>, <a href="/garage-twello">garage voor Twello</a>,
      <a href="/garage-vaassen">garage voor Vaassen</a>, <a href="/garage-loenen">garage voor Loenen</a> en
      <a href="/garage-klarenbeek">garage voor Klarenbeek</a>.</p>
    </div>
  </div>
</section>

<!-- Services -->
<section id="diensten">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Diensten</span>
      <h2>Wat wij doen</h2>
      <p>Onderhoud, reparatie, APK en specialistisch werk - in eigen werkplaats.</p>
    </div>

    <div class="services-grid">
      <article class="service-card">
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
        </div>
        <h3>APK-keuring</h3>
        <p>Wij plannen de keuring via een RDW-erkend partner-station en pakken benodigd onderhoud meteen mee.</p>
        <a href="/apk">Meer over APK →</a>
      </article>

      <article class="service-card">
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
        </div>
        <h3>Onderhoud &amp; reparatie</h3>
        <p>Beurten, olie, remmen, distributie. Duidelijke prijsafspraken en vakwerk, zonder verrassingen achteraf.</p>
        <a href="/onderhoud">Meer over onderhoud →</a>
      </article>

      <article class="service-card featured">
        <span class="badge">Specialiteit</span>
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        </div>
        <h3>Specialistisch onderhoud</h3>
        <p>Foutmeldingen die niet weggaan, motormanagement, elektronica en sensorstoringen.</p>
        <a href="/specialistisch">Onze specialisaties →</a>
      </article>

      <article class="service-card">
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/></svg>
        </div>
        <h3>Banden &amp; wielen</h3>
        <p>Seizoenswissel, balanceren en uitlijnen. Inclusief advies bij nieuwe banden.</p>
        <a href="/banden">Banden &amp; wielen →</a>
      </article>
    </div>

    <div class="services-grid" style="margin-top:20px;">
      <article class="service-card">
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h2l3-9 4 18 3-12 2 6h4"/></svg>
        </div>
        <h3>Airco-service</h3>
        <p>Vullen, controleren en reinigen. Voor frisse lucht en een airco die het blijft doen.</p>
        <a href="/airco">Airco-service →</a>
      </article>

      <article class="service-card">
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z"/></svg>
        </div>
        <h3>Schadeherstel</h3>
        <p>Van bumpertje en deuken tot grotere schade. Wij maken op verzoek een schadebegroting.</p>
        <a href="/schadeherstel">Schadeherstel →</a>
      </article>

      <article class="service-card">
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="18" cy="18" r="3"/><path d="M9 6h9M6 9v9"/></svg>
        </div>
        <h3>Versnellingsbakolie</h3>
        <p>Verversen voor handbak, automaat, DSG en CVT. Olie op fabrieksspecificatie.</p>
        <a href="/versnellingsbakolie-verversen">Versnellingsbakolie verversen →</a>
      </article>

      <article class="service-card">
        <div class="icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5h14v14H5z"/><path d="M5 12h14"/></svg>
        </div>
        <h3>Elektrische storingen</h3>
        <p>Foutmeldingen, accuproblemen, elektrische ramen, verlichting - wij speuren en lossen op.</p>
        <a href="/specialistisch">Specialistisch werk →</a>
      </article>
    </div>
  </div>
</section>

<!-- Specialistisch werk -->
<section id="specialist" class="section-alt">
  <div class="container">
    <div class="section-header left" style="max-width: 900px;">
      <span class="eyebrow">Specialistisch werk</span>
      <h2>Diagnose en elektronica</h2>
      <p>Niet elke storing los je op door onderdelen te vervangen. Bij foutmeldingen die terugkomen,
      motormanagement-problemen en elektronica-storingen werken wij met uitleesapparatuur
      en een vaste werkwijze: uitlezen, meten, diagnose, herstel.</p>
    </div>
    <div style="max-width: 900px;">
      <ul class="checks" style="list-style:none; padding:0; display:grid; grid-template-columns:1fr 1fr; gap:12px;">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Foutmeldingen die niet wijken</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Motormanagement &amp; elektronica</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>ABS &amp; veiligheidssystemen</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Trillingen &amp; geluiden lokaliseren</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Olie- en koelvloeistoflekkages</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Sensoren &amp; comfortsystemen</li>
      </ul>
      <div style="margin-top: 32px;">
        <a class="btn btn-primary" href="/specialistisch">
          Meer over specialistisch werk
          <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>

<!--
  REVIEWS - selectie uit echte Google Reviews
  (4,9 sterren, 33 reviews op het Google bedrijfsprofiel).
-->
<section class="reviews section-tight" id="reviews">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Wat klanten zeggen</span>
      <h2>Ervaringen van klanten</h2>
      <p>Een greep uit recensies van onze Google-klanten, met een gemiddelde beoordeling van <strong>4,9 / 5</strong> over <strong>33 reviews</strong>.</p>
    </div>

    <div class="reviews-grid">
''' + REVIEW_CARDS + '''
    </div>

    <p class="reviews-cta" style="text-align:center; margin-top:32px; color:var(--muted); font-size:14px;">
      Zelf je ervaring delen? <a href="https://g.page/r/Ca6jilmVWAZBEAE/review" target="_blank" rel="noopener noreferrer" style="color:var(--brand-red-dark); font-weight:600; text-decoration:underline;">Plaats een review op Google</a>.
    </p>
  </div>
</section>

'''

# ---------- APK ----------
APK_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">APK</span>
        <h1>APK-keuring in <span class="accent">Apeldoorn-Zuid.</span></h1>
        <p class="lead">
          Wij plannen de APK voor je in en kijken bij dezelfde afspraak of er
          nog onderhoud of slijtagepunten aandacht nodig hebben - zodat de keuring
          afgerond kan worden zonder herhalingsafspraak.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">APK inplannen</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Hoe wij dat regelen</span>
        <h2>Jij brengt 'm bij ons, wij regelen de keuring.</h2>
        <p>De wettelijke APK-keuring zelf wordt uitgevoerd door ons RDW-erkende partner-station.
        Wij doen de coördinatie, voorbereiding en eventueel direct uitgevoerde reparaties.
        Voor jou betekent het &eacute;&eacute;n adres - geen apart bezoek aan een keuringsstation.</p>
        <ul class="checks-list">
          <li>Verlichting, ruitenwissers en zicht</li>
          <li>Remsysteem (remblokken, schijven, leidingen)</li>
          <li>Banden, wielophanging en stuurinrichting</li>
          <li>Carrosserie, chassis en onderstel</li>
          <li>Uitlaatsysteem en emissies (roetfilter, lambda)</li>
          <li>Gordels, airbags en veiligheidssystemen</li>
          <li>Algehele identificatie van het voertuig</li>
        </ul>
        <a class="btn btn-primary" href="/contact">APK-afspraak maken →</a>
      </div>
      <div>
        <picture><source type="image/webp" srcset="/werkplaats-all-cars-specialist-419w.webp 419w, /werkplaats-all-cars-specialist-838w.webp 838w, /werkplaats-all-cars-specialist-1257w.webp 1257w" sizes="(max-width: 900px) 100vw, 50vw"><img src="/werkplaats-all-cars-specialist-838w.jpg" srcset="/werkplaats-all-cars-specialist-419w.jpg 419w, /werkplaats-all-cars-specialist-838w.jpg 838w, /werkplaats-all-cars-specialist-1257w.jpg 1257w" sizes="(max-width: 900px) 100vw, 50vw" alt="Werkplaats All-Cars Specialist tijdens APK-keuring" loading="lazy" decoding="async" width="1749" height="1004"></picture>
      </div>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Bij elke APK</span>
      <h2>Aanvullende controle van slijtagepunten</h2>
      <p>We kijken verder dan alleen de keuringseisen, zodat je weet welke onderhouds- of
      reparatiepunten in de aankomende periode aandacht vragen.</p>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <h3>Onderstel &amp; banden</h3>
        <p>Ophanging, schokdempers, stabilisatorstangen, banden (profiel, slijtage, druk).</p>
      </article>
      <article class="service-card">
        <h3>Aandrijflijn</h3>
        <p>Olie en filters, koelvloeistof, distributie-indicatie, lekkages onder de motor.</p>
      </article>
      <article class="service-card">
        <h3>Elektronica</h3>
        <p>Accu-conditie, dynamo-uitgang, <a href="/foutmelding-uitlezen">foutcodes uitlezen</a> via OBD.</p>
      </article>
      <article class="service-card">
        <h3>Comfort &amp; veiligheid</h3>
        <p>Airco-werking (kort), ruitenwissers, claxon, gordels, kindzitbevestigingen.</p>
      </article>
    </div>
    <p style="margin-top:24px;">Tweedehands auto op het oog? Voor je koopt zetten we hem op de brug: kijk bij de <a href="/aankoopkeuring">aankoopkeuring</a>.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">Veelgestelde vragen</span>
      <h2>APK in Apeldoorn - wat klanten ons vragen</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Wanneer moet mijn auto APK?</summary>
        <div class="answer">
          <p>De eerste APK is vanaf 4 jaar na datum eerste toelating (DET) voor benzine en hybride,
          en vanaf 3 jaar voor diesel. Daarna jaarlijks vanaf 8 jaar (benzine/hybride) of jaarlijks (diesel).
          Niet zeker? Stuur ons je kenteken via WhatsApp en we zoeken het voor je op.</p>
        </div>
      </details>
      <details>
        <summary>Wat kost een APK-keuring?</summary>
        <div class="answer">
          <p>Onze APK-prijs is transparant en vast. Stuur ons een appje of mail voor het exacte tarief -
          we werken niet met verrassingen achteraf. Eventuele reparaties die nodig zijn, bespreken we
          vooraf en pakken we pas aan als je akkoord bent.</p>
        </div>
      </details>
      <details>
        <summary>Hoelang duurt de keuring?</summary>
        <div class="answer">
          <p>Een APK duurt doorgaans rond een uur als alles in orde is. App ons even voor het exacte tijdslot bij jouw afspraak.</p>
        </div>
      </details>
      <details>
        <summary>Wat als mijn auto wordt afgekeurd?</summary>
        <div class="answer">
          <p>Dan bespreken we wat er moet gebeuren en wat het gaat kosten. Reparaties voeren we alleen uit als jij akkoord bent; daarna brengen we je auto opnieuw langs het keuringsstation voor herkeuring.</p>
        </div>
      </details>
      <details>
        <summary>Kunnen kleine reparaties direct mee?</summary>
        <div class="answer">
          <p>Kleine zaken zoals ruitenwisserbladen, lampjes of bandenspanning kunnen we vaak meteen oplossen. Bij grotere reparaties plannen we een vervolgafspraak en geven we vooraf een offerte.</p>
        </div>
      </details>
      <details>
        <summary>Kan ik dezelfde dag een afspraak maken?</summary>
        <div class="answer">
          <p>Soms wel. App ons even en we kijken wat er die dag past. Voor zekerheid raden we aan een paar dagen vooruit in te plannen.</p>
        </div>
      </details>
    </div>
  </div>
</section>'''

# ---------- ONDERHOUD ----------
ONDERHOUD_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Onderhoud &amp; reparatie</span>
        <h1>Auto-onderhoud in <span class="accent">Apeldoorn-Zuid.</span></h1>
        <p class="lead">
          Periodiek onderhoud, reparatie en alles ertussenin - voor alle merken,
          aan de Surinameweg in Apeldoorn-Zuid. Wij werken volgens fabrieksvoorschrift
          en gebruiken passende onderdelen.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Onderhoudsafspraak</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Wat valt onder onderhoud?</span>
      <h2>De volledige beurt - niets uitgesloten</h2>
      <p>Wij werken volgens de fabrieksvoorschriften en houden je auto op zijn fabriekswaarde,
      ook na de garantieperiode.</p>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
        <h3>Kleine onderhoudsbeurt</h3>
        <p>Olie, oliefilter, vloeistoffen op niveau, banden- en remmencheck, <a href="/foutmelding-uitlezen">foutcodes uitlezen</a>.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M2 12h20"/></svg></div>
        <h3>Grote onderhoudsbeurt</h3>
        <p>Alles van de kleine beurt plus luchtfilter, brandstoffilter, interieurfilter, distributie-controle, ophanging.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="18" cy="18" r="3"/><path d="M9 6h9M6 9v9"/></svg></div>
        <h3>Distributieriem &amp; -ketting</h3>
        <p>Op tijd vervangen voorkomt motorschade. Volgens fabrieksinterval, met waterpomp waar nodig.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg></div>
        <h3>Remsysteem</h3>
        <p>Remblokken, remschijven, remvloeistof verversen, remleidingen controleren op lekkage.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18M12 3v18"/></svg></div>
        <h3>Ophanging &amp; stuurwerk</h3>
        <p>Schokdempers, fuseekogels, stabilisatorstangen, draagarmen, stuurkogels - alles dat slijt.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h2l3-9 4 18 3-12 2 6h4"/></svg></div>
        <h3>Koelsysteem</h3>
        <p>Koelvloeistof verversen, thermostaat, waterpomp, radiateur, slangen op lekkage.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z"/></svg></div>
        <h3>Accu &amp; elektronica</h3>
        <p>Accu meten en zo nodig vervangen, dynamo-uitgang controleren, foutcodes opvragen.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg></div>
        <h3>Volgens fabrieksvoorschrift</h3>
        <p>We werken volgens de fabrieksvoorschriften en gebruiken passende onderdelen.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Hoe wij werken</span>
      <h2>Geen verrassingen - altijd vooraf afgestemd</h2>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Plan in</h3>
        <p>App, mail of plan online. We bespreken kort de klacht of het onderhoudsinterval.</p>
      </div>
      <div class="step">
        <h3>Ontvang offerte</h3>
        <p>Voor we beginnen weet je waar je aan toe bent. Eventueel meerwerk altijd in overleg.</p>
      </div>
      <div class="step">
        <h3>Wij voeren uit</h3>
        <p>Vakmanschap dat al sinds 2013 wordt opgebouwd, met onderdelen die bij je auto passen.</p>
      </div>
      <div class="step">
        <h3>Slijtagecheck</h3>
        <p>Aanvullende controle van slijtagepunten. Meerwerk altijd vooraf in overleg.</p>
      </div>
    </div>
    <p style="margin-top:24px;">Schakelt je auto stroef of schokt de automaat? Kijk bij <a href="/versnellingsbakolie-verversen">versnellingsbakolie verversen</a>. En de <a href="/distributieriem-vervangen">distributieriem</a> vervang je beter op tijd dan te laat. Koop je een tweedehands auto? Laat hem eerst nakijken bij de <a href="/aankoopkeuring">aankoopkeuring</a>.</p>
  </div>
</section>'''

# ---------- SPECIALISTISCH ----------
SPECIAL_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Specialistisch onderhoud</span>
        <h1>Auto-diagnose en specialistisch onderhoud in <span class="accent">Apeldoorn.</span></h1>
        <p class="lead">
          Auto-diagnose in Apeldoorn voor foutmeldingen die terugkomen, motormanagement-storingen
          en elektronica die zich niet &eacute;&eacute;n-twee-drie laat lezen. We zoeken eerst, vervangen daarna.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Maak een afspraak</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="two-col flipped">
      <div>
        <picture><source type="image/webp" srcset="/werkplaats-all-cars-specialist-419w.webp 419w, /werkplaats-all-cars-specialist-838w.webp 838w, /werkplaats-all-cars-specialist-1257w.webp 1257w" sizes="(max-width: 900px) 100vw, 50vw"><img src="/werkplaats-all-cars-specialist-838w.jpg" srcset="/werkplaats-all-cars-specialist-419w.jpg 419w, /werkplaats-all-cars-specialist-838w.jpg 838w, /werkplaats-all-cars-specialist-1257w.jpg 1257w" sizes="(max-width: 900px) 100vw, 50vw" alt="Diagnose-werkplek bij All-Cars Specialist Apeldoorn" loading="lazy" decoding="async" width="1749" height="1004"></picture>
      </div>
      <div>
        <span class="eyebrow">Voor wie</span>
        <h2>Klachten die wij vaak oppakken</h2>
        <p>Sommige problemen vragen om diagnose-apparatuur en methodisch zoeken in plaats van
        onderdelen-vervangen. Herken je iets uit deze lijst? App of mail ons.</p>
        <ul class="checks-list">
          <li><a href="/foutmelding-uitlezen">Foutmeldingen die niet weggaan</a></li>
          <li>Storingen in elektronica en motormanagement</li>
          <li>Veiligheidssysteem-meldingen (ABS, airbag, ESP)</li>
          <li>Vloeistof-lekkages</li>
          <li>Stroef schakelen of een schokkende automaat (vaak <a href="/versnellingsbakolie-verversen">de versnellingsbakolie</a>)</li>
          <li>Trillingen of geluiden zonder duidelijke oorzaak</li>
          <li>Onverklaarbaar verbruik of vermogensverlies</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Wat wij oppakken</span>
      <h2>Onze specialisaties</h2>
      <p>We werken met uitleesapparatuur en een gestructureerde aanpak: eerst zoeken,
      dan vervangen.</p>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 1-7 7M5 12a7 7 0 0 1 7-7"/></svg></div>
        <h3>Motormanagement</h3>
        <p>Inspuitsystemen, bobines, sensoren, uitlaatgasterugvoer (EGR), lambda - we lezen, meten en testen.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5h14v14H5z"/><path d="M5 12h14"/></svg></div>
        <h3>Elektronica &amp; CAN-bus</h3>
        <p>Storingen op de databus, modulen die niet communiceren, intermitterende fouten.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z"/></svg></div>
        <h3>Veiligheidssystemen</h3>
        <p>ABS, airbag en comfortsystemen die meldingen geven of niet meer goed werken.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h2l3-9 4 18 3-12 2 6h4"/></svg></div>
        <h3>Trillingen &amp; lekkages</h3>
        <p>Geluiden, trillingen en vloeistoflekkages methodisch lokaliseren en verhelpen.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Aanpak</span>
      <h2>Hoe wij werken</h2>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Uitlezen</h3>
        <p>OBD-uitlezen, foutcodes, live data. We weten waar de auto over piept.</p>
      </div>
      <div class="step">
        <h3>Meten</h3>
        <p>We meten met diagnose-apparatuur in plaats van te gokken.</p>
      </div>
      <div class="step">
        <h3>Diagnose</h3>
        <p>Een eerlijke conclusie wat er aan de hand is, met heldere offerte voor de oplossing.</p>
      </div>
      <div class="step">
        <h3>Herstel &amp; check</h3>
        <p>We voeren uit, controleren live data nogmaals en testrijden voor we afronden.</p>
      </div>
    </div>
  </div>
</section>

'''

# ---------- BANDEN ----------
BANDEN_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Banden &amp; wielen</span>
        <h1>Banden, balanceren <span class="accent">en uitlijnen</span> - onder één dak.</h1>
        <p class="lead">
          Van seizoenswissel tot nieuwe banden, balanceren en uitlijnen.
          We bestellen alleen wat past bij jouw auto en jouw rijgedrag.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Banden inplannen</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Wat we doen</span>
      <h2>Alles voor onder de auto</h2>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/></svg></div>
        <h3>Bandenwissel</h3>
        <p>Zomer naar winter en omgekeerd, met bandenspanning op de juiste waarde.</p>
      </article>

      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M3 12h18"/></svg></div>
        <h3>Balanceren</h3>
        <p>Trillingen in stuur of stoel? We balanceren elk wiel zodat je auto weer rustig stuurt.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18M3 17h18"/></svg></div>
        <h3>Uitlijnen</h3>
        <p>Trekt je auto naar één kant? Slijt je banden onregelmatig? Wij stellen wielgeometrie op fabriekswaarde.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        <h3>Nieuwe banden</h3>
        <p>We adviseren een set die past bij je auto, gebruik en kilometrage.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M5 12h14"/></svg></div>
        <h3>Schokdempers &amp; ophanging</h3>
        <p>Hoort eigenlijk bij banden - wij controleren bij elke wissel of de ophanging nog goed is.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">Veelgesteld</span>
      <h2>Bandenvragen die we vaak krijgen</h2>
    </div>
    <div class="faq">
      <details>
        <summary>Wanneer moet ik mijn banden wisselen?</summary>
        <div class="answer"><p>Bij een profieldiepte onder 1,6&nbsp;mm wettelijk verplicht, maar onder 3&nbsp;mm in de winter al onveilig. Wij meten gratis bij elke beurt en geven advies.</p></div>
      </details>
      <details>
        <summary>Heb ik per se winterbanden nodig?</summary>
        <div class="answer"><p>Niet wettelijk verplicht in Nederland, maar bij temperaturen onder 7&nbsp;°C presteren zomerbanden minder. Voor wie veel rijdt of in heuvelig gebied: aanrader. Allseason kan een goed compromis zijn.</p></div>
      </details>
      <details>
        <summary>Mijn auto trilt - wat kan dat zijn?</summary>
        <div class="answer"><p>Meestal ongebalanceerde wielen, soms een bobbel in een band of een verbogen velg. We meten op de balanceerbank en lossen het op.</p></div>
      </details>
    </div>
  </div>
</section>'''

# ---------- AIRCO ----------
AIRCO_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Airco-service</span>
        <h1>Airco-service in <span class="accent">Apeldoorn.</span></h1>
        <p class="lead">
          Vullen, controleren en reinigen. Een airco verliest jaarlijks koelmiddel;
          op tijd bijvullen voorkomt schade aan de compressor.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Airco-afspraak</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Wat we doen</span>
        <h2>Niet alleen vullen - ook controleren en reinigen</h2>
        <p>Een airco-service is meer dan koudemiddel bijvullen. We checken het hele systeem op lekkage,
        meten of de druk klopt, en kunnen het systeem reinigen tegen schimmel en muffe geuren.</p>
        <ul class="checks-list">
          <li>Aircosysteem doorblazen, vacumeren en bijvullen</li>
          <li>Lekkage-controle</li>
          <li>Werking compressor en circulatie controleren</li>
          <li>Interieurfilter vervangen indien nodig</li>
          <li>Reiniging op verzoek (tegen muffe geur)</li>
          <li>Functietest: temperatuur, druk en doorstroming</li>
        </ul>
        <a class="btn btn-primary" href="/contact">Plan airco-service →</a>
      </div>
      <div>
        <picture><source type="image/webp" srcset="/werkplaats-all-cars-specialist-419w.webp 419w, /werkplaats-all-cars-specialist-838w.webp 838w, /werkplaats-all-cars-specialist-1257w.webp 1257w" sizes="(max-width: 900px) 100vw, 50vw"><img src="/werkplaats-all-cars-specialist-838w.jpg" srcset="/werkplaats-all-cars-specialist-419w.jpg 419w, /werkplaats-all-cars-specialist-838w.jpg 838w, /werkplaats-all-cars-specialist-1257w.jpg 1257w" sizes="(max-width: 900px) 100vw, 50vw" alt="Airco-onderhoud bij All-Cars Specialist Apeldoorn" loading="lazy" decoding="async" width="1749" height="1004"></picture>
      </div>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">Wanneer onderhoud?</span>
      <h2>Tekenen dat je airco aandacht nodig heeft</h2>
    </div>
    <ul class="checks-list">
      <li>Hij koelt minder dan voorheen</li>
      <li>Vreemde geur als je hem aanzet</li>
      <li>Sissende of klikkende geluiden</li>
      <li>Vocht onder de auto na gebruik</li>
      <li>Het is meer dan twee jaar geleden dat je hem liet vullen</li>
    </ul>
    <p class="muted" style="margin-top:24px;">Vuistregel: laat je airco minimaal eens in de twee jaar nakijken,
    ook als hij nog koelt. Voorkomt grotere reparaties.</p>
  </div>
</section>'''

# ---------- SCHADEHERSTEL ----------
SCHADE_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Schadeherstel</span>
        <h1>Schadeherstel: <span class="accent">groot en klein.</span></h1>
        <p class="lead">
          Van een deuk of kras tot grotere schade na een aanrijding. Wij herstellen
          en maken op verzoek een schadebegroting voor je verzekering.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Schade melden</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Wat we behandelen</span>
      <h2>Klein, groot, en alles ertussenin</h2>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18"/></svg></div>
        <h3>Krassen &amp; kleine deuken</h3>
        <p>Parkeerschade, winkelwagenkrassen, kleine deuken - we herstellen lokaal zonder hele paneel-spuitwerk waar mogelijk.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18l-2 12H5L3 7z"/></svg></div>
        <h3>Bumper- en plaatwerk</h3>
        <p>Van bumperreparatie tot plaatwerk. We herstellen of vervangen, afhankelijk van wat het beste resultaat geeft.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z"/></svg></div>
        <h3>Schadebegroting</h3>
        <p>Wij maken een begroting voor herstel of voor je verzekering. Indienen regel je zelf.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
        <h3>Zonder verzekering</h3>
        <p>Liever niet via je verzekering? Vraag een offerte voor herstel uit eigen zak.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Hoe wij werken</span>
      <h2>Van melding tot afgehaalde auto</h2>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Meld de schade</h3>
        <p>Stuur foto's via WhatsApp. We bekijken meteen wat er nodig is.</p>
      </div>
      <div class="step">
        <h3>Schade-inspectie</h3>
        <p>Bij ons in de werkplaats maken we een precieze inschatting en offerte.</p>
      </div>
      <div class="step">
        <h3>Begroting</h3>
        <p>Wij geven een schadebegroting voor je verzekering of voor herstel uit eigen zak.</p>
      </div>
      <div class="step">
        <h3>Herstel &amp; oplevering</h3>
        <p>Wij herstellen, controleren en leveren je auto schoon en gecheckt op.</p>
      </div>
    </div>
  </div>
</section>'''

# ---------- AANKOOPKEURING ----------
AANKOOP_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Aankoopkeuring</span>
        <h1>Aankoopkeuring in <span class="accent">Apeldoorn.</span></h1>
        <p class="lead">
          Twijfel je over een tweedehands auto? Laat hem keuren voordat je koopt.
          Wij kijken naar de technische staat, naar verborgen gebreken en naar wat er
          op korte termijn aankomt, zodat je weet wat je in huis haalt.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Keuring inplannen</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Wat we controleren</span>
      <h2>Waar we naar kijken</h2>
      <p>Een keuring vóór de koop voorkomt dat je een dure verrassing meeneemt.</p>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l2-5 4 10 2-5h6"/></svg></div>
        <h3>Motor &amp; techniek</h3>
        <p>Motorloop, vloeistoffen, lekkages en sporen van eerder uitstel van onderhoud.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/></svg></div>
        <h3>Onderstel &amp; remmen</h3>
        <p>Remmen, schokdempers, ophanging en banden: wat is versleten, wat kan nog mee.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5h14v14H5z"/><path d="M9 9h6v6H9z"/></svg></div>
        <h3>Elektronica &amp; foutcodes</h3>
        <p>We lezen de boordcomputer uit (OBD) en checken of er foutcodes in het geheugen staan.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h18l-2 12H5L3 7z"/><path d="M9 7V4h6v3"/></svg></div>
        <h3>Carrosserie &amp; verleden</h3>
        <p>Sporen van schade of roest en aanwijzingen voor eerder plaatwerk.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Hoe het werkt</span>
      <h2>Van advertentie tot helder oordeel</h2>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Stuur de auto door</h3>
        <p>App ons de advertentie of het kenteken. We laten weten waar we op letten.</p>
      </div>
      <div class="step">
        <h3>Breng de auto langs</h3>
        <p>Maak met de verkoper een afspraak om de auto bij ons in de werkplaats te brengen.</p>
      </div>
      <div class="step">
        <h3>Wij keuren</h3>
        <p>Op de brug en met uitleesapparatuur lopen we de auto methodisch na.</p>
      </div>
      <div class="step">
        <h3>Je hoort het eerlijk</h3>
        <p>Een helder overzicht van de staat en wat er aankomt. Daarna beslis jij.</p>
      </div>
    </div>
    <p style="margin-top:24px;">Gaat het om een keuring in combinatie met een aankomende keuringsdatum? Bekijk ook onze <a href="/apk">APK-keuring</a>.</p>
  </div>
</section>'''

# ---------- DISTRIBUTIERIEM ----------
DISTRI_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Distributieriem</span>
        <h1>Distributieriem vervangen in <span class="accent">Apeldoorn.</span></h1>
        <p class="lead">
          De distributieriem moet je op tijd vervangen. Breekt hij tijdens het rijden,
          dan loopt de motor vaak zware schade op. Wij vervangen de riem volgens het
          voorschrift van jouw merk en model.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Interval laten checken</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Waarom op tijd</span>
      <h2>Een klein onderdeel met grote gevolgen</h2>
      <p>De distributieriem houdt de motor in de juiste timing. Hij slijt onzichtbaar,
      dus je merkt pas dat het mis is als het te laat is.</p>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="7" cy="12" r="3"/><circle cx="17" cy="12" r="3"/><path d="M7 9h10M7 15h10"/></svg></div>
        <h3>Wat de riem doet</h3>
        <p>De riem laat de kleppen precies op tijd open- en dichtgaan ten opzichte van de zuigers.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div>
        <h3>Wanneer vervangen</h3>
        <p>Meestal tussen 60.000 en 120.000 km of na vier tot zes jaar. Per merk verschilt het.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v6M12 16v6M2 12h6M16 12h6"/><circle cx="12" cy="12" r="3"/></svg></div>
        <h3>Waterpomp meteen mee</h3>
        <p>Bij veel auto's drijft de riem ook de waterpomp aan. Samen vervangen scheelt arbeidsloon.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h16M4 12h16M4 16h16"/></svg></div>
        <h3>Riem of ketting</h3>
        <p>Niet elke auto heeft een riem. Een ketting gaat langer mee, maar is niet onderhoudsvrij.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Hoe wij werken</span>
      <h2>Vervangen zonder verrassingen</h2>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Interval opzoeken</h3>
        <p>Geef je kenteken door. We zoeken het voorschrift voor jouw motor op.</p>
      </div>
      <div class="step">
        <h3>Offerte vooraf</h3>
        <p>Je krijgt een heldere prijs, inclusief advies over de waterpomp.</p>
      </div>
      <div class="step">
        <h3>Vervanging op voorschrift</h3>
        <p>We vervangen riem, spanrol en wat er volgens het merk bij hoort.</p>
      </div>
      <div class="step">
        <h3>Testrit &amp; controle</h3>
        <p>Na montage controleren we de werking en rijden we een rondje voor we afronden.</p>
      </div>
    </div>
    <p style="margin-top:24px;">Distributieriem combineren met een beurt? Kijk bij <a href="/onderhoud">onderhoud en reparatie</a>. Ook de <a href="/versnellingsbakolie-verversen">versnellingsbakolie</a> is bij veel auto's rond dit kilometrage aan vervanging toe.</p>
  </div>
</section>'''

# ---------- VERSNELLINGSBAKOLIE ----------
VERSNELLINGSBAK_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Versnellingsbakolie</span>
        <h1>Versnellingsbakolie verversen in <span class="accent">Apeldoorn.</span></h1>
        <p class="lead">
          Ook de olie in je versnellingsbak veroudert. Verse olie laat de bak weer licht
          schakelen en voorkomt dure slijtage - bij een handbak &eacute;n een automaat.
          Wij verversen met olie op fabrieksspecificatie, aan de Surinameweg in Apeldoorn-Zuid.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Interval laten checken</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">Waarom verversen</span>
      <h2>Wat doet versnellingsbakolie en waarom slijt hij?</h2>
    </div>
    <p>Versnellingsbakolie smeert de tandwielen, lagers en synchromeshringen in de bak en voert
    warmte af. Door die warmte en door fijne metaaldeeltjes van het schakelen loopt de smering
    terug. Bij de meeste auto's is de olie na 60.000 tot 120.000 kilometer zo ver versleten dat
    schakelen zwaarder gaat en de bak sneller slijt. Verversen kost een fractie van een
    bakrevisie of een vervangende automaat.</p>
    <p style="margin-top:12px;">Herken je een van deze klachten? Dan is de olie een logische eerste check:</p>
    <ul class="checks-list" style="margin-top:12px;">
      <li>Stroef of krakend schakelen, vooral met een koude motor</li>
      <li>Een automaat die schokt, aarzelt of te laat schakelt</li>
      <li>Brommend of zoemend geluid dat met de snelheid meeloopt</li>
      <li>Oliesporen onder de auto ter hoogte van de bak</li>
    </ul>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Per type bak</span>
      <h2>Handbak, automaat, DSG of CVT: elk z'n eigen olie</h2>
      <p>Het interval en de olie verschillen per type bak. Dit houden wij aan als richtlijn;
      het voorschrift van jouw merk en motor is altijd leidend.</p>
    </div>
    <div class="table-scroll">
      <table class="price-table interval-table">
        <thead>
          <tr><th>Type versnellingsbak</th><th>Wat de olie doet</th><th>Gangbaar interval</th></tr>
        </thead>
        <tbody>
          <tr><td>Handgeschakeld</td><td data-label="Wat de olie doet">Smeert tandwielen en synchromesh</td><td data-label="Gangbaar interval">Rond 100.000 km; eerder bij trekhaakgebruik of veel korte ritten</td></tr>
          <tr><td>Automaat (koppelomvormer)</td><td data-label="Wat de olie doet">Smeert &eacute;n stuurt het schakelen (ATF)</td><td data-label="Gangbaar interval">60.000 - 80.000 km, meestal inclusief filter</td></tr>
          <tr><td>DSG / dubbele koppeling</td><td data-label="Wat de olie doet">Smeert bak en natte koppelingen</td><td data-label="Gangbaar interval">Vast fabrieksinterval, vaak elke 60.000 km</td></tr>
          <tr><td>CVT</td><td data-label="Wat de olie doet">Speciale olie voor de duwband of ketting</td><td data-label="Gangbaar interval">Per merk verschillend, doorgaans 60.000 - 90.000 km</td></tr>
        </tbody>
      </table>
    </div>
    <p class="price-note">Richtlijnen op basis van gangbare fabrieksvoorschriften; laatst gecontroleerd augustus 2026. Geef je kenteken door, dan zoeken we het exacte voorschrift voor jouw auto op.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">In eigen werkplaats</span>
        <h2>Verversen op de juiste specificatie</h2>
        <p>Elke bak vraagt zijn eigen olie: verkeerde olie in een automaat of DSG geeft juist
        schakelproblemen. Wij hebben kwaliteitsolie op voorraad, onder meer van Xenum, en
        kiezen per auto de specificatie die de fabrikant voorschrijft.</p>
        <p>Bij automaten luistert ook de vulprocedure nauw: het oliepeil wordt op
        een voorgeschreven temperatuur afgesteld. Wij werken volgens die procedure en vervangen
        waar nodig het filter en de carterpakking.</p>
        <p>Blijft een schakelklacht na het verversen bestaan? Dan meten we verder via ons
        <a href="/specialistisch">specialistisch onderhoud en diagnose</a>. En combineren met een
        beurt kan altijd: kijk bij <a href="/onderhoud">onderhoud en reparatie</a>.</p>
      </div>
      <div>
        <img src="/versnellingsbakolie-verversen-apeldoorn-838w.jpg" srcset="/versnellingsbakolie-verversen-apeldoorn-419w.jpg 419w, /versnellingsbakolie-verversen-apeldoorn-838w.jpg 838w, /versnellingsbakolie-verversen-apeldoorn-1152w.jpg 1152w" sizes="(max-width: 900px) 100vw, 50vw" alt="Voorraad versnellingsbakolie van onder meer Xenum in de werkplaats van All-Cars Specialist in Apeldoorn" loading="lazy" decoding="async" width="1152" height="1552" style="border-radius:12px;">
      </div>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Hoe wij werken</span>
      <h2>Van kenteken naar soepel schakelen</h2>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Kenteken doorgeven</h3>
        <p>App of mail je kenteken. We zoeken op welke olie en welk interval jouw bak heeft.</p>
      </div>
      <div class="step">
        <h3>Offerte vooraf</h3>
        <p>Je hoort vooraf wat het verversen kost, inclusief olie en eventueel filter.</p>
      </div>
      <div class="step">
        <h3>Verversen op voorschrift</h3>
        <p>Aftappen, filter en pakking waar nodig, vullen op de juiste temperatuur.</p>
      </div>
      <div class="step">
        <h3>Proefrit &amp; controle</h3>
        <p>We rijden een rondje, controleren het peil en checken op lekkage.</p>
      </div>
    </div>
    <p style="margin-top:24px;">Ook de <a href="/distributieriem-vervangen">distributieriem</a> is zo'n onderdeel dat je beter op tijd vervangt dan te laat. Vraag ernaar bij je afspraak.</p>
  </div>
</section>'''

# ---------- FOUTMELDING UITLEZEN ----------
FOUT_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Foutmelding uitlezen</span>
        <h1>Foutmelding uitlezen in <span class="accent">Apeldoorn.</span></h1>
        <p class="lead">
          Brandt er een waarschuwingslampje of een melding op je dashboard? Wij lezen
          de foutcodes uit en vertellen je wat er aan de hand is, zonder meteen
          onderdelen te vervangen.
        </p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Laten uitlezen</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Rood of oranje</span>
      <h2>Wat zegt de kleur van het lampje?</h2>
      <p>Een rood lampje vraagt om direct stoppen. Een oranje lampje betekent meestal:
      laat het op korte termijn nakijken.</p>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19 12a7 7 0 0 1-7 7M5 12a7 7 0 0 1 7-7"/></svg></div>
        <h3>Motormanagement</h3>
        <p>Het oranje motorlampje. Kan van een sensor komen tot een echt motorprobleem.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8 12h8"/></svg></div>
        <h3>ABS &amp; remsysteem</h3>
        <p>Een melding van het remsysteem hoort altijd snel nagekeken te worden.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z"/></svg></div>
        <h3>Airbag</h3>
        <p>Het airbaglampje betekent dat de veiligheidssystemen niet zeker goed werken.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 7h10v6H7zM10 7V4h4v3M9 17h6"/></svg></div>
        <h3>Accu &amp; laadsysteem</h3>
        <p>Brandt het accusymbool tijdens het rijden? Dan laadt de auto mogelijk niet bij.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">Uitlezen is het begin</span>
      <h2>Een code wijst de richting, niet de hele oplossing</h2>
    </div>
    <p>Uitlezen via de OBD-poort geeft een foutcode. Die code wijst naar een systeem,
    maar zegt niet altijd precies wat er kapot is. Een code voor "te arm mengsel" kan
    bijvoorbeeld van een sensor komen, maar ook van een lek of een vervuild onderdeel.
    Daarom vervangen we niet op de gok: we lezen uit, duiden de code en meten door waar dat nodig is.</p>
    <p>Komt een melding steeds terug of is de storing lastig te pakken? Dan pakken we het op
    via ons <a href="/specialistisch">specialistisch onderhoud en diagnose</a>.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Hoe wij werken</span>
      <h2>Van lampje naar duidelijkheid</h2>
    </div>
    <div class="steps">
      <div class="step">
        <h3>Uitlezen</h3>
        <p>We lezen de foutcodes en de live data uit via de OBD-poort.</p>
      </div>
      <div class="step">
        <h3>Code duiden</h3>
        <p>We vertalen de code naar wat er in jouw auto speelt.</p>
      </div>
      <div class="step">
        <h3>Meten waar nodig</h3>
        <p>Bij twijfel meten we door in plaats van te gokken.</p>
      </div>
      <div class="step">
        <h3>Uitleg &amp; offerte</h3>
        <p>Je hoort in gewone taal wat er aan de hand is en wat herstel kost.</p>
      </div>
    </div>
  </div>
</section>'''

# ---------- BUURPLAATS-PAGINA'S (regio) ----------
# Gedeeld diensten-blok dat naar de hoofd-dienstpagina's linkt.
REGIO_SERVICES_GRID = '''<section class="section-tight">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Waarvoor je langskomt</span>
      <h2>Alles voor je auto onder &eacute;&eacute;n dak</h2>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <h3><a href="/onderhoud">Onderhoud &amp; reparatie</a></h3>
        <p>Periodieke beurten en reparaties volgens fabrieksvoorschrift, voor alle merken.</p>
      </article>
      <article class="service-card">
        <h3><a href="/apk">APK-keuring</a></h3>
        <p>We regelen de keuring via een vast station en pakken benodigd onderhoud meteen mee.</p>
      </article>
      <article class="service-card">
        <h3><a href="/specialistisch">Diagnose &amp; specialistisch werk</a></h3>
        <p>Storingen die andere garages laten liggen: wij zoeken en meten eerst.</p>
      </article>
      <article class="service-card">
        <h3><a href="/banden">Banden &amp; uitlijnen</a></h3>
        <p>Bandenwissel, nieuwe banden, balanceren en uitlijnen.</p>
      </article>
      <article class="service-card">
        <h3><a href="/airco">Airco-service</a></h3>
        <p>Vullen, controleren en op verzoek reinigen.</p>
      </article>
      <article class="service-card">
        <h3><a href="/schadeherstel">Schadeherstel</a></h3>
        <p>Van kras of parkeerdeuk tot bumper- en plaatwerk.</p>
      </article>
    </div>
  </div>
</section>'''

def regio_body(eyebrow, h1, lead, why_title, why_html, local_title="", local_html=""):
    # local_title/local_html: uniek blok per plaats, zodat de regiopagina's niet
    # als kopie&euml;n van hetzelfde sjabloon lezen (indexatie-signaal).
    local_section = ""
    if local_html:
        local_section = f'''
<section class="section-tight">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">De rit ernaartoe</span>
      <h2>{local_title}</h2>
    </div>
    {local_html}
  </div>
</section>
'''
    return f'''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
        <div class="hero-cta">
          <a class="btn btn-primary btn-lg" href="/contact">Maak een afspraak</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>
{local_section}
{REGIO_SERVICES_GRID}

<section class="section-tight section-alt">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">Waarom hierheen</span>
      <h2>{why_title}</h2>
    </div>
    {why_html}
  </div>
</section>'''

BEEKBERGEN_BODY = regio_body(
    "Regio &middot; Beekbergen",
    'Garage voor <span class="accent">Beekbergen.</span>',
    'Woon je in Beekbergen en zoek je een garage die niet vastzit aan &eacute;&eacute;n merk? '
    'Vanaf Beekbergen rijd je in ongeveer tien minuten naar onze werkplaats aan de Surinameweg '
    'in Apeldoorn-Zuid. Een universele garage voor onderhoud, APK, banden en diagnose.',
    "Een vaste garage net buiten het dorp",
    '<p>Veel klanten uit Beekbergen komen voor onze manier van werken: we vervangen niet op de gok, '
    'maar zoeken en meten eerst. Dat scheelt onnodige kosten en voorkomt dat een storing blijft '
    'terugkomen. Of het nu om een gewone beurt gaat of om een klacht die elders niet opgelost raakte, '
    'je krijgt vooraf te horen wat er nodig is en wat het kost.</p>'
    '<p style="margin-top:12px;">We werken voor alle merken en plannen je op afspraak in. '
    'Geef je kenteken door via <a href="/contact">WhatsApp of het contactformulier</a>, dan zoeken we '
    'bijvoorbeeld meteen je APK-datum op.</p>',
    "Vanuit Beekbergen ben je er zo",
    '<p>Beekbergen ligt pal onder Apeldoorn: je rijdt binnendoor naar de Surinameweg en hoeft daarvoor '
    'het centrum van Apeldoorn niet in. De meeste klanten brengen de auto aan het begin van de ochtend '
    'en halen hem dezelfde dag weer op.</p>'
    '<p style="margin-top:12px;">Wat we bij auto\'s uit het dorp vaak zien: veel korte ritten. De motor '
    'komt dan zelden goed op temperatuur, waardoor olie sneller veroudert dan de kilometerstand doet '
    'vermoeden. Bij een beurt houden we daar rekening mee.</p>'
    '<p style="margin-top:12px;">Korte ritten kosten ook de accu: die laadt op zo\'n stukje zelden '
    'helemaal vol, en dat merk je in de winter aan het starten. Bij een <a href="/onderhoud">'
    'onderhoudsbeurt</a> nemen we de accuspanning daarom mee in de controle. Blijft er daarna toch een '
    'lampje branden, dan gaat de auto eerst aan de <a href="/foutmelding-uitlezen">uitleesapparatuur</a> '
    'voordat er iets vervangen wordt.</p>'
)

TWELLO_BODY = regio_body(
    "Regio &middot; Twello",
    'Garage voor <span class="accent">Twello.</span>',
    'Vanuit Twello ben je via de A1 in ongeveer twintig minuten bij onze werkplaats aan de Surinameweg '
    'in Apeldoorn-Zuid. Een universele garage voor onderhoud, APK en diagnose, voor wie verder kijkt '
    'dan de garage om de hoek.',
    "De rit waard voor onderhoud en diagnose",
    '<p>Klanten uit Twello rijden vaak naar ons toe voor de diagnose-aanpak: eerst uitlezen en meten, '
    'dan pas vervangen. Juist bij storingen die steeds terugkomen, is dat het verschil tussen gokken '
    'en oplossen. Voor gewoon onderhoud, APK en banden ben je net zo goed op het juiste adres.</p>'
    '<p style="margin-top:12px;">Plannen we de afspraak in? Stuur een appje met je kenteken en je '
    'klacht of wens via <a href="/contact">de contactpagina</a>. Je hoort wat je kunt verwachten '
    'voordat je langskomt.</p>',
    "E&eacute;n afrit over de A1, of binnendoor langs Teuge",
    '<p>Twello ligt in de gemeente Voorst, tussen Deventer en Apeldoorn in. Via de A1 sta je in zo\'n '
    'twintig minuten voor onze deur; wie liever binnendoor rijdt, neemt de weg langs Teuge.</p>'
    '<p style="margin-top:12px;">Omdat je er even voor rijdt, plannen we scherp: je weet vooraf wat we '
    'gaan doen en wat het kost, zodat je nooit voor niets komt. De auto een dagje laten staan is geen '
    'probleem.</p>'
    '<p style="margin-top:12px;">Rijd je vanuit Twello dagelijks over de A1 naar Deventer of Apeldoorn, '
    'dan maak je vooral snelwegkilometers. De teller loopt hard op terwijl de motor weinig koude starts '
    'maakt: het omgekeerde van stadsgebruik. Onderhoudsvoorschriften kennen meestal een termijn in jaren '
    'en een in kilometers, en bij dit rijgedrag is de kilometergrens bijna altijd als eerste aan de '
    'beurt. Dat geldt zeker voor de <a href="/distributieriem-vervangen">distributieriem</a>: geef je '
    'kilometerstand door bij het inplannen, dan zoeken we het voorschrift voor jouw motor op.</p>'
)

VAASSEN_BODY = regio_body(
    "Regio &middot; Vaassen",
    'Garage voor <span class="accent">Vaassen.</span>',
    'Vanuit Vaassen rijd je in ongeveer twintig minuten naar onze werkplaats aan de Surinameweg '
    'in Apeldoorn-Zuid. Een universele garage voor onderhoud, APK, banden en diagnose, voor alle merken.',
    "Een onafhankelijke garage zonder merkbinding",
    '<p>Omdat we niet aan &eacute;&eacute;n merk of keten vastzitten, kiezen we steeds wat het beste is voor '
    'jouw auto. Geen verplichte dealertarieven, geen verkooppraatjes: je hoort eerlijk wat er nodig is en '
    'wat het kost. Dat geldt voor een gewone beurt net zo goed als voor een hardnekkige storing.</p>'
    '<p style="margin-top:12px;">Plannen we je in? Geef je kenteken door via <a href="/contact">WhatsApp of het '
    'contactformulier</a>, dan zoeken we bijvoorbeeld meteen je APK-datum op.</p>',
    "Via de A50 of binnendoor via Wenum-Wiesel",
    '<p>Vaassen, bekend van kasteel De Cannenburch, ligt boven Apeldoorn in de gemeente Epe. Naar '
    'Apeldoorn-Zuid rijd je via de A50 of binnendoor via Wenum-Wiesel; beide routes komen op ongeveer '
    'twintig minuten uit.</p>'
    '<p style="margin-top:12px;">Geef bij het inplannen je kenteken door. We zoeken dan vooraf het '
    'onderhoudsschema en je APK-datum op, zodat de afspraak in &eacute;&eacute;n bezoek klaar is.</p>'
    '<p style="margin-top:12px;">Twintig minuten is te ver om voor elk klusje heen en weer te rijden. '
    'Werk voor klanten uit Vaassen combineren we daarom zo veel mogelijk in &eacute;&eacute;n bezoek: de '
    '<a href="/apk">APK</a> en de beurt op dezelfde dag, of de <a href="/banden">seizoenswissel</a> er '
    'meteen bij. Loopt er daarnaast een klacht waarvan de oorzaak onduidelijk is, meld die dan bij het '
    'maken van de afspraak, zodat we er tijd voor inruimen om eerst te meten.</p>'
)

LOENEN_BODY = regio_body(
    "Regio &middot; Loenen",
    'Garage voor <span class="accent">Loenen.</span>',
    'Vanaf Loenen ben je in ongeveer een kwartier bij onze werkplaats aan de Surinameweg in '
    'Apeldoorn-Zuid. Onderhoud, APK, banden en diagnose onder &eacute;&eacute;n dak, voor alle merken.',
    "Bekend met diagnose en hardnekkige storingen",
    '<p>Klanten uit Loenen komen vaak voor onze diagnose-aanpak: eerst uitlezen en meten, dan pas '
    'vervangen. Juist bij een storing die steeds terugkomt, scheelt dat onnodige kosten. Voor gewoon '
    'onderhoud, APK en banden ben je hier net zo goed op je plek.</p>'
    '<p style="margin-top:12px;">Een afspraak maken gaat het snelst via <a href="/contact">'
    'WhatsApp</a>. Vertel je kenteken en je klacht, dan laten we weten wat je kunt verwachten.</p>',
    "Een kwartier langs de rand van de Veluwe",
    '<p>Loenen ligt aan de oostkant van de Veluwe, bekend van de Loenense waterval. De rit naar de '
    'Surinameweg gaat langs Beekbergen en duurt ongeveer een kwartier; vanuit Eerbeek is het maar een '
    'paar minuten meer.</p>'
    '<p style="margin-top:12px;">Uitlezen en doormeten doen we in eigen werkplaats, dus ook met een vage '
    'storing hoef je maar &eacute;&eacute;n keer te rijden. Voor een beurt of bandenwissel geldt '
    'hetzelfde adres.</p>'
    '<p style="margin-top:12px;">Wie veel over de Veluwe rijdt, vraagt meer van de remmen dan iemand die '
    'alleen vlak terrein onder de wielen heeft: bij afdalingen rem je waar je anders zou uitrollen. Hoor '
    'je een pieper of voel je een trilling in het pedaal, meld het dan bij het maken van de afspraak. '
    'Remschijven en remblokken nemen we bij een <a href="/onderhoud">onderhoudsbeurt</a> sowieso mee in '
    'de controle.</p>'
)

KLARENBEEK_BODY = regio_body(
    "Regio &middot; Klarenbeek",
    'Garage voor <span class="accent">Klarenbeek.</span>',
    'Vanuit Klarenbeek rijd je in ongeveer een kwartier naar de Surinameweg in Apeldoorn-Zuid. '
    'Een vaste, onafhankelijke garage voor onderhoud, APK, banden en reparatie.',
    "Eerlijk vakmanschap op een vaste plek",
    '<p>We zitten sinds 2013 op dezelfde plek met dezelfde aanpak: doen wat nodig is, en niet meer dan dat. '
    'Geen merkbinding, geen keten, wel een werkplaats die is ingericht op zowel dagelijks onderhoud als op '
    'het zoekwerk bij lastige klachten.</p>'
    '<p style="margin-top:12px;">Wil je langskomen? Stuur een appje via <a href="/contact">de '
    'contactpagina</a> met je kenteken en je wens, dan plannen we je in.</p>',
    "Rustige route, geen stadsverkeer",
    '<p>Klarenbeek ligt op de grens van de gemeenten Apeldoorn en Voorst, tussen Apeldoorn en Zutphen '
    'in. De route naar Apeldoorn-Zuid is een rustige rit van rond het kwartier, zonder druk '
    'centrumverkeer.</p>'
    '<p style="margin-top:12px;">Bij de werkplaats is ruime parkeermogelijkheid en we werken op '
    'afspraak: je weet dus wanneer je terecht kunt en hoeft niet te wachten tot er plek is.</p>'
    '<p style="margin-top:12px;">Tussen Klarenbeek en Apeldoorn rijd je vooral over rustige buitenwegen: '
    'weinig optrekken en afremmen, veel constante snelheid. Slijtage door stadsverkeer valt daardoor mee, '
    'maar juist bij dat gelijkmatige rijden vallen een trilling in het stuur of een auto die naar '
    '&eacute;&eacute;n kant trekt eerder op. Vaak is dat een kwestie van <a href="/banden">balanceren of '
    'uitlijnen</a>. Merk je zoiets, geef het door bij het inplannen, dan kijken we er meteen naar.</p>'
)

# ---------- OVER ONS ----------
OVER_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Over ons</span>
        <h1>All-Cars Specialist B.V. <span class="accent">in Apeldoorn-Zuid.</span></h1>
        <p class="lead">
          Onafhankelijke universele garage. Geen merkdealer, geen keten.
          Sinds 2013 op de Surinameweg.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Wie wij zijn</span>
        <h2>Garage sinds 2013</h2>
        <p>All-Cars Specialist B.V. is een onafhankelijke universele garage aan de Surinameweg in Apeldoorn-Zuid.
        Sinds 2013 doen we hier onderhoud, reparatie, APK, banden, airco, schadeherstel en specialistisch
        diagnosewerk, in eigen werkplaats en voor alle merken.</p>
        <p>Onafhankelijk betekent dat we niet aan &eacute;&eacute;n merk of keten vastzitten. We kiezen wat
        het beste is voor jouw auto en je portemonnee, en we vertellen eerlijk wat er nodig is. Niet meer dan dat.</p>
        <p>We werken voor particulieren en kleine zakelijke klanten uit Apeldoorn en de omliggende plaatsen,
        van <a href="/garage-beekbergen">Beekbergen</a> en <a href="/garage-loenen">Loenen</a> tot
        <a href="/garage-vaassen">Vaassen</a>, <a href="/garage-klarenbeek">Klarenbeek</a> en
        <a href="/garage-twello">Twello</a>.</p>
      </div>
      <div>
        <picture><source type="image/webp" srcset="/werkplaats-all-cars-specialist-419w.webp 419w, /werkplaats-all-cars-specialist-838w.webp 838w, /werkplaats-all-cars-specialist-1257w.webp 1257w" sizes="(max-width: 900px) 100vw, 50vw"><img src="/werkplaats-all-cars-specialist-838w.jpg" srcset="/werkplaats-all-cars-specialist-419w.jpg 419w, /werkplaats-all-cars-specialist-838w.jpg 838w, /werkplaats-all-cars-specialist-1257w.jpg 1257w" sizes="(max-width: 900px) 100vw, 50vw" alt="Werkplaats All-Cars Specialist Apeldoorn" loading="lazy" decoding="async" width="1749" height="1004"></picture>
      </div>
    </div>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">Onze aanpak</span>
      <h2>Eerst zoeken, dan vervangen</h2>
    </div>
    <p>Onze manier van werken draait om diagnose. We lezen uit, meten en zoeken de oorzaak
    voordat we onderdelen vervangen. Dat klinkt vanzelfsprekend, maar het is precies waar het
    vaak misgaat: onderdelen wisselen tot een storing toevallig weg is, kost veel geld en lost
    zelden het echte probleem op.</p>
    <p style="margin-top:12px;">Daardoor krijgen we regelmatig auto's binnen met een klacht die
    elders bleef terugkomen. Een foutmelding die niet weggaat, een trilling zonder duidelijke
    oorzaak, een elektronisch probleem dat niemand kon plaatsen. Juist dat werk ligt ons. Lees meer
    over ons <a href="/specialistisch">specialistisch onderhoud en diagnose</a>.</p>
  </div>
</section>

<section class="section-tight">
  <div class="container container-narrow">
    <div class="section-header left">
      <span class="eyebrow">De werkplaats</span>
      <h2>Ingericht op onderhoud &eacute;n zoekwerk</h2>
    </div>
    <p>Onze werkplaats aan de Surinameweg is geschikt voor zowel dagelijks onderhoud als voor de
    klussen die wat meer uitzoekwerk vragen.</p>
    <ul class="checks-list" style="margin-top:12px;">
      <li>Drie hefbruggen, zodat we meerdere auto's tegelijk kunnen aanpakken</li>
      <li>Uitleesapparatuur voor foutcodes, live data en metingen</li>
      <li>Ruime parkeergelegenheid; geen druk centrumverkeer</li>
      <li>Werken op afspraak, met spoed in overleg</li>
    </ul>
  </div>
</section>

<section class="section-tight section-alt">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">Waar we voor staan</span>
      <h2>Vier kernwaarden - niet meer en niet minder</h2>
    </div>
    <div class="services-grid">
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>
        <h3>Eerlijk</h3>
        <p>Wat er aan de hand is, vertellen we - ook als het niet is wat je hoopt.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 2 3 7 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1z"/></svg></div>
        <h3>Vakkundig</h3>
        <p>Eerst zoeken, dan vervangen. Onderdelen-wisselen-tot-het-werkt is duur en niet nodig.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        <h3>Op afspraak</h3>
        <p>We plannen je zo snel mogelijk in. Spoed in overleg.</p>
      </article>
      <article class="service-card">
        <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 6v6c0 5 3.5 9 8 10 4.5-1 8-5 8-10V6l-8-4z"/></svg></div>
        <h3>Vast adres</h3>
        <p>Sinds 2013 op dezelfde plek, dezelfde aanpak.</p>
      </article>
    </div>
  </div>
</section>'''

# ---------- CONTACT ----------
CONTACT_BODY = '''<section class="hero hero-compact">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="hero-eyebrow">Contact</span>
        <h1>Plan een afspraak <span class="accent">- of app direct.</span></h1>
        <p class="lead">
          Een appje via WhatsApp gaat het snelst. Het formulier invullen of mailen kan ook -
          we nemen zo snel mogelijk contact met je op.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="two-col">
      <div>
        <span class="eyebrow">Plan online</span>
        <h2>Stuur ons je gegevens</h2>
        <p>We nemen zo snel mogelijk contact met je op. Met spoed? Stuur een appje.</p>
        <form class="form-grid" action="https://formsubmit.co/info@all-cars-specialist.nl" method="post" style="margin-top:24px;"><input type="hidden" name="_next" value="https://all-cars-specialist.nl/contact"><input type="hidden" name="_subject" value="Nieuwe afspraakaanvraag via website"><input type="hidden" name="_captcha" value="false">
          <div class="field">
            <label for="naam">Naam *</label>
            <input id="naam" name="naam" type="text" required>
          </div>
          <div class="field">
            <label for="telefoon">Telefoon *</label>
            <input id="telefoon" name="telefoon" type="tel" required>
          </div>
          <div class="field full">
            <label for="email">E-mailadres</label>
            <input id="email" name="email" type="email">
          </div>
          <div class="field">
            <label for="kenteken">Kenteken</label>
            <input id="kenteken" name="kenteken" type="text" placeholder="AB-12-CD">
          </div>
          <div class="field">
            <label for="dienst">Voor welke dienst?</label>
            <select id="dienst" name="dienst">
              <option value="">Kies een dienst...</option>
              <option>APK-keuring</option>
              <option>Onderhoudsbeurt</option>
              <option>Versnellingsbakolie verversen</option>
              <option>Specialistisch onderhoud / diagnose</option>
              <option>Banden &amp; wielen</option>
              <option>Airco-service</option>
              <option>Schadeherstel</option>
              <option>Anders / weet ik niet</option>
            </select>
          </div>
          <div class="field full">
            <label for="bericht">Toelichting / klacht</label>
            <textarea id="bericht" name="bericht" placeholder="Beschrijf kort wat er aan de hand is..."></textarea>
            <span class="hint">Bij een storing helpt het als je schrijft wanneer en hoe vaak het optreedt.</span>
          </div>
          <div class="field full">
            <button type="submit" class="btn btn-primary btn-lg">Verstuur afspraakverzoek →</button>
          </div>
        </form>
      </div>
      <div>
        <div class="contact-card">
          <h3>Direct contact</h3>
          <dl>
            <dt>WhatsApp</dt>
            <dd><a href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">06 33 93 57 20</a></dd>

            <dt>E-mail</dt>
            <dd><a href="mailto:info@all-cars-specialist.nl">info@all-cars-specialist.nl</a></dd>

            <dt id="openingstijden">Openingstijden</dt>
            <dd>Maandag t/m vrijdag - 09:00 – 17:00<br/>Zaterdag &amp; zondag - gesloten</dd>

            <dt>Adres</dt>
            <dd>Surinameweg 33<br/>7333 PC Apeldoorn (Zuid)</dd>

            <dt>KvK</dt>
            <dd>56939485</dd>
          </dl>
        </div>

        <div class="maps-embed" style="margin-top:24px;">
          <iframe src="https://www.google.com/maps?q=Surinameweg+33,+7333+PC+Apeldoorn&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Locatie All-Cars Specialist Apeldoorn"></iframe>
        </div>
        <p style="margin-top:16px; font-size:14px; color:var(--muted);">Kom je van buiten Apeldoorn?
        Lees hoe we werken als <a href="/garage-beekbergen">garage in Beekbergen</a>,
        <a href="/garage-loenen">garage in Loenen</a>, <a href="/garage-klarenbeek">garage in Klarenbeek</a>,
        <a href="/garage-vaassen">garage in Vaassen</a> en <a href="/garage-twello">garage in Twello</a>.</p>
      </div>
    </div>
  </div>
</section>'''

# ---------- PRIVACYVERKLARING ----------
PRIVACY_BODY = '<section class="hero hero-compact">\n  <div class="container">\n    <div class="hero-grid">\n      <div>\n        <span class="hero-eyebrow">Juridisch</span>\n        <h1>Privacyverklaring.</h1>\n        <p class="lead">\n          Hoe wij omgaan met je persoonsgegevens als je gebruikmaakt van onze diensten of contact met ons opneemt.\n          Versie: mei 2026.\n        </p>\n      </div>\n    </div>\n  </div>\n</section>\n\n<section class="section-tight">\n  <div class="container container-narrow">\n    <h2>Wie is verantwoordelijk?</h2>\n    <p>All-Cars Specialist B.V., gevestigd aan Surinameweg 33, 7333&nbsp;PC Apeldoorn,\n    is de verwerkingsverantwoordelijke voor de verwerking van persoonsgegevens\n    zoals beschreven in deze verklaring. Voor vragen over privacy kun je contact\n    opnemen via <a href="mailto:info@all-cars-specialist.nl">info@all-cars-specialist.nl</a>\n    of via <a href="https://wa.me/31633935720">WhatsApp (06 33 93 57 20)</a>.</p>\n\n    <h2>Welke gegevens verwerken wij?</h2>\n    <p>Wij verwerken persoonsgegevens die je zelf aan ons verstrekt of die nodig zijn om\n    onze diensten goed uit te voeren:</p>\n    <ul>\n      <li>Contactgegevens: naam, adres, telefoonnummer, e-mailadres</li>\n      <li>Voertuiggegevens: kenteken, merk, model, kilometerstand, onderhoudshistorie</li>\n      <li>Klacht- of opdrachtomschrijving</li>\n      <li>Factuur- en betalingsgegevens</li>\n      <li>Communicatie: e-mails, app-berichten, telefoonnotities</li>\n    </ul>\n\n    <h2>Waarvoor gebruiken wij die gegevens?</h2>\n    <ul>\n      <li>Het maken en bevestigen van afspraken</li>\n      <li>Het uitvoeren van de overeengekomen werkzaamheden</li>\n      <li>Het opstellen en versturen van offertes en facturen</li>\n      <li>Communicatie over de status van je auto of een lopende reparatie</li>\n      <li>Het voldoen aan wettelijke verplichtingen (zoals de fiscale bewaarplicht)</li>\n      <li>Het verbeteren van onze dienstverlening</li>\n    </ul>\n\n    <h2>Op welke grond verwerken wij je gegevens?</h2>\n    <p>De verwerking gebeurt op basis van &eacute;&eacute;n of meer van de volgende grondslagen:</p>\n    <ul>\n      <li>De uitvoering van de overeenkomst die je met ons hebt</li>\n      <li>Het voldoen aan een wettelijke verplichting (bijvoorbeeld bewaartermijnen)</li>\n      <li>Een gerechtvaardigd belang, zoals administratie, beveiliging en bedrijfsvoering</li>\n      <li>Jouw expliciete toestemming, waar die nodig is</li>\n    </ul>\n\n    <h2>Met wie delen wij gegevens?</h2>\n    <p>We delen alleen wat nodig is, alleen met partijen die zelf voldoen aan de AVG en\n    waarmee wij waar vereist verwerkersovereenkomsten hebben:</p>\n    <ul>\n      <li><strong>RDW-erkend partner-keuringsstation</strong>: voor de uitvoering van de APK-keuring (kenteken en voertuiggegevens)</li>\n      <li><strong>Onderdelen-leveranciers</strong>: voor het bestellen van specifieke onderdelen voor jouw auto</li>\n      <li><strong>Onze boekhouder en accountant</strong>: voor verplichte financi&euml;le administratie</li>\n      <li><strong>Verzekeraar of expert</strong>: alleen bij schadeherstel en alleen wanneer jij dat zelf wilt</li>\n      <li><strong>Bevoegde overheidsinstanties</strong>: wanneer wij daartoe wettelijk verplicht zijn</li>\n    </ul>\n    <p>Wij verkopen je gegevens niet aan derden voor commercieel gebruik.</p>\n\n    <h2>Hoe lang bewaren wij je gegevens?</h2>\n    <p>Persoonsgegevens worden niet langer bewaard dan nodig is. Voor financi&euml;le administratie\n    geldt de wettelijke bewaartermijn van zeven jaar. Klant- en voertuiggegevens bewaren wij\n    zo lang als zinvol is voor de dienstverlening, en daarna verwijderen of anonimiseren wij ze.</p>\n\n    <h2>Beveiliging</h2>\n    <p>Wij nemen passende technische en organisatorische maatregelen om je gegevens te beschermen\n    tegen verlies of onrechtmatig gebruik. Heb je het vermoeden dat er iets misgaat met je\n    gegevens? Mail of app ons direct.</p>\n\n    <h2>Cookies en website-analyse</h2>\n    <p>Op deze website worden alleen functionele middelen gebruikt om de site goed te laten werken.\n    Externe scripts zijn beperkt tot het laden van lettertypen (Google Fonts) en een eventuele\n    Google Maps-kaart op de contactpagina. Wij plaatsen geen tracking- of advertentie-cookies.</p>\n\n    <h2>Jouw rechten</h2>\n    <p>Op grond van de AVG heb je de volgende rechten over de persoonsgegevens die wij verwerken:</p>\n    <ul>\n      <li>Recht op inzage in je gegevens</li>\n      <li>Recht op rectificatie (correctie) van onjuiste gegevens</li>\n      <li>Recht op verwijdering, mits dat niet in strijd is met wettelijke bewaartermijnen</li>\n      <li>Recht op beperking van de verwerking</li>\n      <li>Recht op bezwaar tegen de verwerking</li>\n      <li>Recht op gegevensoverdraagbaarheid (dataportabiliteit)</li>\n      <li>Recht om een gegeven toestemming weer in te trekken</li>\n    </ul>\n    <p>Wil je een van deze rechten uitoefenen? Stuur een bericht naar\n    <a href="mailto:info@all-cars-specialist.nl">info@all-cars-specialist.nl</a>.\n    Wij reageren binnen de wettelijke termijn zoals voorzien in de AVG.</p>\n\n    <h2>Klacht indienen</h2>\n    <p>Vind je dat wij niet goed met je gegevens omgaan? Laat het ons eerst weten,\n    dan zoeken we het samen uit. Je hebt daarnaast het recht om een klacht in te dienen\n    bij de Autoriteit Persoonsgegevens (autoriteitpersoonsgegevens.nl).</p>\n\n    <h2>Wijzigingen in deze verklaring</h2>\n    <p>Deze verklaring kan worden aangepast als onze dienstverlening of regelgeving daartoe\n    aanleiding geeft. Op deze pagina vind je de actuele versie.</p>\n\n    <p class="muted" style="margin-top:32px; font-size:13.5px;">\n      <em>Op deze tekst zijn wijzigingen voorbehouden. De op deze pagina gepubliceerde versie is de actuele versie; aan eerdere of afwijkende formuleringen kunnen geen rechten worden ontleend. Voor de specifieke voorwaarden van een opdracht gelden de schriftelijke afspraken die per opdracht worden gemaakt.</em>\n    </p>\n  </div>\n</section>'

# ---------- ALGEMENE VOORWAARDEN ----------
AV_BODY = '<section class="hero hero-compact">\n  <div class="container">\n    <div class="hero-grid">\n      <div>\n        <span class="hero-eyebrow">Juridisch</span>\n        <h1>Algemene voorwaarden.</h1>\n        <p class="lead">\n          De voorwaarden die gelden bij offertes, opdrachten en werkzaamheden die wij voor je uitvoeren.\n          Versie: mei 2026.\n        </p>\n      </div>\n    </div>\n  </div>\n</section>\n\n<section class="section-tight">\n  <div class="container container-narrow">\n\n    <h2>1. Definities</h2>\n    <ul>\n      <li><strong>Garage</strong>: All-Cars Specialist B.V., gevestigd aan Surinameweg 33, 7333&nbsp;PC Apeldoorn (KvK 56939485).</li>\n      <li><strong>Opdrachtgever</strong>: de partij die de garage opdracht geeft tot werkzaamheden of een offerte aanvraagt.</li>\n      <li><strong>Voertuig</strong>: het door de opdrachtgever aangeboden motorvoertuig of onderdeel daarvan.</li>\n      <li><strong>Werkzaamheden</strong>: alle door de garage uit te voeren of uitgevoerde diensten en/of leveringen, waaronder onderhoud, reparatie, diagnose, banden, airco-service, schadeherstel en de coordinatie van de APK-keuring.</li>\n    </ul>\n\n    <h2>2. Toepasselijkheid</h2>\n    <p>Deze voorwaarden zijn van toepassing op alle aanbiedingen, offertes en overeenkomsten tussen\n    de garage en de opdrachtgever, tenzij schriftelijk anders is overeengekomen. Eventuele inkoop-\n    of andere voorwaarden van de opdrachtgever zijn niet van toepassing.</p>\n\n    <h2>3. Offertes en totstandkoming overeenkomst</h2>\n    <p>Offertes zijn vrijblijvend en gebaseerd op de op het moment van uitbrengen bekende informatie.\n    Een overeenkomst komt tot stand zodra de opdrachtgever de offerte mondeling of schriftelijk\n    accepteert, dan wel een opdracht tot werkzaamheden geeft. Wij behouden ons het recht voor\n    een opdracht te weigeren.</p>\n\n    <h2>4. Uitvoering van werkzaamheden</h2>\n    <p>De garage voert de werkzaamheden uit naar beste vakkennis en inzicht.\n    De afgesproken oplevertermijn is een streefdatum en niet bindend, tenzij uitdrukkelijk\n    schriftelijk anders is overeengekomen. Vertragingen die buiten onze macht liggen\n    (bijvoorbeeld levertijden van onderdelen) verlengen de termijn met de duur daarvan.</p>\n\n    <h2>5. Onderdelen</h2>\n    <p>Wij gebruiken onderdelen die geschikt zijn voor het voertuig, in onze keuze tussen origineel,\n    A-merk en gelijkwaardig. Op verzoek van de opdrachtgever kunnen specifieke onderdelen\n    worden gebruikt; daarvoor kunnen aanvullende kosten gelden. Vervangen onderdelen worden\n    eigendom van de garage tenzij de opdrachtgever vooraf om teruggave vraagt.</p>\n\n    <h2>6. Meerwerk</h2>\n    <p>Als tijdens de uitvoering blijkt dat aanvullende werkzaamheden nodig of wenselijk zijn,\n    nemen wij eerst contact op met de opdrachtgever. Meerwerk wordt alleen uitgevoerd na\n    akkoord van de opdrachtgever. Klein meerwerk dat nodig is om de opdracht af te ronden pakken we\n    direct op; grotere afwijkingen leggen we altijd eerst aan je voor.</p>\n\n    <h2>7. Prijzen en betaling</h2>\n    <p>Tenzij anders aangegeven zijn prijzen inclusief btw. De factuur wordt opgesteld na\n    afronding van de werkzaamheden en dient te worden betaald binnen de op de factuur vermelde betalingstermijn. Bij overschrijding van de betalingstermijn is de opdrachtgever wettelijke\n    rente en redelijke incassokosten verschuldigd. Wij hebben het recht het voertuig\n    onder ons te houden totdat het verschuldigde bedrag is voldaan (retentierecht).</p>\n\n    <h2>8. Ophalen van het voertuig</h2>\n    <p>De opdrachtgever is verplicht het voertuig op te halen op het door ons aangegeven moment.\n    Indien het voertuig na gereedmelding niet binnen redelijke termijn wordt opgehaald, kunnen wij stallingskosten in rekening brengen. Voertuigen die bij ons achterblijven, staan op ons terrein; verzekering daarvan\n    is de verantwoordelijkheid van de opdrachtgever.</p>\n\n    <h2>9. Garantie</h2>\n    <p>Eventuele garantie op uitgevoerde werkzaamheden wordt per opdracht schriftelijk afgestemd.\n    Op nieuwe onderdelen geldt, voor zover van toepassing, de garantie van de fabrikant of leverancier.\n    Op gebruikte onderdelen wordt geen garantie gegeven, tenzij dat uitdrukkelijk schriftelijk is\n    overeengekomen. Garantie is in alle gevallen uitgesloten voor gebreken die het gevolg zijn\n    van slijtage, oneigenlijk gebruik, gebrekkig onderhoud, of wijzigingen aan het voertuig\n    die door derden zijn aangebracht na onze werkzaamheden.</p>\n\n    <h2>10. Aansprakelijkheid</h2>\n    <p>De aansprakelijkheid van de garage is beperkt tot het bedrag dat onze aansprakelijkheids-\n    verzekering in het betreffende geval uitkeert, dan wel tot maximaal het factuurbedrag van\n    de betreffende werkzaamheden. Wij zijn niet aansprakelijk voor indirecte schade, gevolgschade,\n    omzetderving, gederfde winst of schade aan zaken die zich in het voertuig bevinden.\n    Aansprakelijkheid voor opzet of bewuste roekeloosheid is hiervan uitgesloten.</p>\n\n    <h2>11. Klachten</h2>\n    <p>Klachten over de uitgevoerde werkzaamheden of de factuur dienen binnen redelijke termijn\n    na constatering schriftelijk aan ons te worden gemeld, in beginsel binnen veertien dagen.\n    Wij beoordelen de klacht en streven naar een reactie binnen redelijke termijn.</p>\n\n    <h2>12. APK-keuring</h2>\n    <p>De wettelijke APK-keuring wordt uitgevoerd door een RDW-erkend keuringsstation waarmee\n    wij samenwerken. Wij coordineren de afspraak en kunnen reparaties uitvoeren die uit de\n    keuring volgen. Voor de keuring zelf gelden de voorwaarden en procedures van het keuringsstation;\n    wij zijn niet aansprakelijk voor de uitkomst van de keuring zelf.</p>\n\n    <h2>13. Toepasselijk recht en geschillen</h2>\n    <p>Op deze voorwaarden en op alle overeenkomsten is uitsluitend Nederlands recht van toepassing.\n    Geschillen worden voorgelegd aan de bevoegde rechter in het arrondissement waar de garage\n    is gevestigd, tenzij de wet dwingend anders bepaalt.</p>\n\n    <p class="muted" style="margin-top:32px; font-size:13.5px;">\n      <em>Op deze tekst zijn wijzigingen voorbehouden. De op deze pagina gepubliceerde versie is de actuele versie; aan eerdere of afwijkende formuleringen kunnen geen rechten worden ontleend. Voor de specifieke voorwaarden van een opdracht gelden de schriftelijke afspraken die per opdracht worden gemaakt.</em>\n    </p>\n  </div>\n</section>'

# ============================================================
# Build & write
# ============================================================
def write(slug, html):
    """
    'index' en '404' blijven .html op de root (Vercel error-routing).
    Alle andere slugs krijgen hun eigen directory met index.html
    -> URLs eindigen nergens op .html
    """
    if slug in ("index", "404"):
        path = os.path.join(OUT, f"{slug}.html")
    else:
        dirpath = os.path.join(OUT, slug)
        os.makedirs(dirpath, exist_ok=True)
        path = os.path.join(dirpath, "index.html")
    with open(path, "w") as f:
        f.write(html)
    rel = os.path.relpath(path, OUT)
    print(f"  wrote {rel} ({len(html):,} bytes)")

PAGES = [
    ("index",          "Garage Apeldoorn-Zuid - Onderhoud, APK en diagnose | All-Cars Specialist",
                       "Universele garage in Apeldoorn-Zuid (Surinameweg). Auto-onderhoud, APK, banden, airco, schadeherstel en diagnose voor alle merken. Sinds 2013.",
                       HOME_BODY, "home"),
    ("apk",            "APK-keuring Apeldoorn-Zuid - All-Cars Specialist Apeldoorn",
                       "APK in Apeldoorn-Zuid via RDW-erkend partner-station. Wij regelen de keuring en pakken benodigd onderhoud meteen mee. Surinameweg, Apeldoorn.",
                       APK_BODY, "apk"),
    ("onderhoud",      "Auto-onderhoud en reparatie in Apeldoorn-Zuid - All-Cars Specialist",
                       "Auto-onderhoud en reparatie in Apeldoorn-Zuid voor alle merken. Periodieke beurten, distributie, remmen, ophanging - volgens fabrieksvoorschrift.",
                       ONDERHOUD_BODY, "onderhoud"),
    ("specialistisch", "Specialistisch onderhoud en diagnose in Apeldoorn - All-Cars Specialist",
                       "Auto-diagnose in Apeldoorn voor foutmeldingen, motormanagement en elektronica. Specialistisch onderhoud bij All-Cars Specialist, Apeldoorn-Zuid.",
                       SPECIAL_BODY, "specialistisch"),
    ("banden",         "Banden, balanceren en uitlijnen - All-Cars Specialist Apeldoorn-Zuid",
                       "Banden, balanceren en uitlijnen in Apeldoorn-Zuid. Bandenwissel, nieuwe banden en advies - voor alle merken. Surinameweg, Apeldoorn.",
                       BANDEN_BODY, "banden"),
    ("airco",          "Airco-service in Apeldoorn - All-Cars Specialist",
                       "Airco vullen, controleren, reinigen en interieurfilter vervangen. Voor frisse lucht en een airco die het blijft doen.",
                       AIRCO_BODY, "home"),
    ("schadeherstel",  "Schadeherstel Apeldoorn-Zuid - All-Cars Specialist",
                       "Schadeherstel in Apeldoorn-Zuid: krassen, deuken, bumper- en plaatwerk. Op verzoek een schadebegroting voor je verzekering.",
                       SCHADE_BODY, "home"),
    ("aankoopkeuring", "Aankoopkeuring tweedehands auto in Apeldoorn - All-Cars Specialist",
                       "Aankoopkeuring in Apeldoorn-Zuid voordat je een tweedehands auto koopt. Wij checken techniek, onderstel, elektronica en schadeverleden. Surinameweg.",
                       AANKOOP_BODY, "apk"),
    ("distributieriem-vervangen", "Distributieriem vervangen in Apeldoorn - All-Cars Specialist",
                       "Distributieriem vervangen in Apeldoorn-Zuid volgens fabrieksvoorschrift, waterpomp op verzoek mee. Geef je kenteken door voor het juiste interval.",
                       DISTRI_BODY, "onderhoud"),
    ("versnellingsbakolie-verversen", "Versnellingsbakolie verversen in Apeldoorn - All-Cars Specialist",
                       "Versnellingsbakolie verversen in Apeldoorn-Zuid: handbak, automaat, DSG en CVT. Olie op fabrieksspecificatie, prijs vooraf. Surinameweg, Apeldoorn.",
                       VERSNELLINGSBAK_BODY, "onderhoud"),
    ("foutmelding-uitlezen", "Foutmelding uitlezen in Apeldoorn - All-Cars Specialist",
                       "Waarschuwingslampje of foutmelding op je dashboard? Wij lezen de foutcodes uit in Apeldoorn-Zuid en vertellen wat er aan de hand is. Surinameweg.",
                       FOUT_BODY, "specialistisch"),
    ("garage-beekbergen", "Garage in Beekbergen - All-Cars Specialist Apeldoorn-Zuid",
                       "Universele garage voor Beekbergen, op tien minuten in Apeldoorn-Zuid. Onderhoud, APK, banden en diagnose voor alle merken. Surinameweg, Apeldoorn.",
                       BEEKBERGEN_BODY, "home"),
    ("garage-twello",  "Garage voor Twello - All-Cars Specialist Apeldoorn-Zuid",
                       "Universele garage voor Twello, via de A1 op zo'n twintig minuten in Apeldoorn-Zuid. Onderhoud, APK, banden en auto-diagnose voor alle merken.",
                       TWELLO_BODY, "home"),
    ("garage-vaassen", "Garage voor Vaassen - All-Cars Specialist Apeldoorn-Zuid",
                       "Universele garage voor Vaassen, op ongeveer twintig minuten in Apeldoorn-Zuid. Onderhoud, APK, banden en diagnose voor alle merken. Surinameweg.",
                       VAASSEN_BODY, "home"),
    ("garage-loenen",  "Garage voor Loenen - All-Cars Specialist Apeldoorn-Zuid",
                       "Universele garage voor Loenen, op een kwartier in Apeldoorn-Zuid. Onderhoud, APK, banden en auto-diagnose voor alle merken. Surinameweg, Apeldoorn.",
                       LOENEN_BODY, "home"),
    ("garage-klarenbeek", "Garage voor Klarenbeek - All-Cars Specialist Apeldoorn-Zuid",
                       "Universele garage voor Klarenbeek, op een kwartier in Apeldoorn-Zuid. Onderhoud, APK, banden en reparatie voor alle merken. Surinameweg, Apeldoorn.",
                       KLARENBEEK_BODY, "home"),
    ("over-ons",       "Over All-Cars Specialist B.V. - sinds 2013 in Apeldoorn-Zuid",
                       "Onafhankelijke universele garage in Apeldoorn-Zuid. Sinds 2013. Vakmanschap, eerlijk advies en moderne diagnose-apparatuur.",
                       OVER_BODY, "home"),
    ("contact",        "Contact en afspraak - All-Cars Specialist Apeldoorn",
                       "Plan online een afspraak of app direct. Surinameweg 33, Apeldoorn-Zuid. We nemen snel contact met je op.",
                       CONTACT_BODY, "contact"),
    ("privacyverklaring",     "Privacyverklaring - All-Cars Specialist Apeldoorn",
                              "Privacyverklaring van All-Cars Specialist B.V. - hoe wij omgaan met je persoonsgegevens.",
                              PRIVACY_BODY, "home"),
    ("algemene-voorwaarden",  "Algemene voorwaarden - All-Cars Specialist Apeldoorn",
                              "Algemene voorwaarden van All-Cars Specialist B.V. voor offertes, opdrachten en werkzaamheden.",
                              AV_BODY, "home"),
]

print("Building pages...")
BUILT_HTML = {}
SERVICE_SCHEMAS = {
    "apk":            service_schema("APK-keuring",                 "APK-keuring via RDW-erkend partner-station in Apeldoorn-Zuid. Wij coordineren de afspraak en pakken benodigd onderhoud meteen mee.", "apk"),
    "onderhoud":      service_schema("Onderhoud en reparatie",      "Periodieke onderhoudsbeurten, kleine en grote reparaties volgens fabrieksvoorschriften.", "onderhoud"),
    "specialistisch": service_schema("Specialistisch onderhoud",    "Diagnose en specialistisch werk voor moderne auto-elektronica en motormanagement.", "specialistisch"),
    "banden":         service_schema("Banden, balanceren en uitlijnen", "Bandenwissel, balanceren, uitlijnen en advies bij nieuwe banden.", "banden"),
    "airco":          service_schema("Airco-service",                "Airco vullen, controleren en op verzoek reinigen.", "airco"),
    "schadeherstel":  service_schema("Schadeherstel",                "Herstel van krassen, deuken, bumper- en plaatwerk; op verzoek schadebegroting.", "schadeherstel"),
    "aankoopkeuring": service_schema("Aankoopkeuring",               "Aankoopkeuring van een tweedehands auto: techniek, onderstel, elektronica en schadeverleden.", "aankoopkeuring"),
    "distributieriem-vervangen": service_schema("Distributieriem vervangen", "Distributieriem vervangen volgens fabrieksvoorschrift, met waterpomp op verzoek.", "distributieriem-vervangen"),
    "versnellingsbakolie-verversen": service_schema("Versnellingsbakolie verversen", "Versnellingsbakolie verversen voor handbak, automaat, DSG en CVT, met olie op fabrieksspecificatie.", "versnellingsbakolie-verversen"),
    "foutmelding-uitlezen": service_schema("Foutmelding uitlezen",   "Foutcodes uitlezen via OBD en duiden welke storing er speelt, zonder onnodig vervangen.", "foutmelding-uitlezen"),
}
PAGE_LABELS = {
    "apk": "APK-keuring", "onderhoud": "Onderhoud", "specialistisch": "Specialistisch onderhoud",
    "banden": "Banden", "airco": "Airco-service", "schadeherstel": "Schadeherstel",
    "aankoopkeuring": "Aankoopkeuring", "distributieriem-vervangen": "Distributieriem vervangen",
    "versnellingsbakolie-verversen": "Versnellingsbakolie verversen",
    "foutmelding-uitlezen": "Foutmelding uitlezen",
    "garage-beekbergen": "Garage Beekbergen", "garage-twello": "Garage Twello",
    "garage-vaassen": "Garage Vaassen", "garage-loenen": "Garage Loenen",
    "garage-klarenbeek": "Garage Klarenbeek",
    "over-ons": "Over ons", "contact": "Contact",
    "algemene-voorwaarden": "Algemene voorwaarden", "privacyverklaring": "Privacyverklaring",
}
for slug, title, desc, body, active in PAGES:
    extra = ""
    if slug == "apk":
        extra = SERVICE_SCHEMAS["apk"] + "\n" + FAQ_APK_SCHEMA
    elif slug in SERVICE_SCHEMAS:
        extra = SERVICE_SCHEMAS[slug]
    # FAQ: zichtbaar blok + FAQPage-schema voor dienstpagina's zonder eigen FAQ
    if slug in FAQS:
        eyebrow, heading, qas = FAQS[slug]
        body = body + faq_html(eyebrow, heading, qas)
        extra += "\n" + faq_schema(qas)
    elif slug == "banden":
        # banden heeft de FAQ al zichtbaar in de body; alleen schema toevoegen
        extra += "\n" + faq_schema(BANDEN_FAQ)
    if slug in PAGE_LABELS:
        extra += "\n" + breadcrumb_schema(slug, PAGE_LABELS[slug])
    html = page(title, desc, body, slug=slug, active=active, extra_schema=extra)
    BUILT_HTML[slug] = html
    write(slug, html)

# ---------- 404 ----------
not_found_body = '''<section class="hero hero-compact" style="text-align:center;">
  <div class="container">
    <div class="hero-grid">
      <div style="margin: 0 auto;">
        <span class="hero-eyebrow">404</span>
        <h1>Pagina <span class="accent">niet gevonden.</span></h1>
        <p class="lead" style="margin-left:auto;margin-right:auto;">Ga terug naar de homepage of stuur ons een appje.</p>
        <div class="hero-cta" style="justify-content:center;">
          <a class="btn btn-primary btn-lg" href="/">Naar homepage</a>
          <a class="btn btn-ghost btn-lg" href="https://wa.me/31633935720" target="_blank" rel="noopener noreferrer">WhatsApp ons</a>
        </div>
      </div>
    </div>
  </div>
</section>'''
write("404", page("Pagina niet gevonden - All-Cars Specialist", "Pagina niet gevonden.", not_found_body, slug="404", active="home"))

# ---------- vercel.json ----------
vercel_cfg = {
    "cleanUrls": True,
    "trailingSlash": False,
    "redirects": [
        {"source": "/diensten", "destination": "/onderhoud", "permanent": False},
        {"source": "/airco-vullen-in-apeldoorn", "destination": "/airco", "permanent": True},
        {"source": "/index.html", "destination": "/", "permanent": True},
        {"source": "/apk.html", "destination": "/apk", "permanent": True},
        {"source": "/onderhoud.html", "destination": "/onderhoud", "permanent": True},
        {"source": "/specialistisch.html", "destination": "/specialistisch", "permanent": True},
        {"source": "/banden.html", "destination": "/banden", "permanent": True},
        {"source": "/airco.html", "destination": "/airco", "permanent": True},
        {"source": "/schadeherstel.html", "destination": "/schadeherstel", "permanent": True},
        {"source": "/over-ons.html", "destination": "/over-ons", "permanent": True},
        {"source": "/contact.html", "destination": "/contact", "permanent": True},
        {"source": "/privacyverklaring.html", "destination": "/privacyverklaring", "permanent": True},
        {"source": "/algemene-voorwaarden.html", "destination": "/algemene-voorwaarden", "permanent": True}
    ],
    "headers": [
        {
            "source": "/(.*)",
            "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"}
            ]
        },
        {
            "source": "/(.*)\\.(png|jpg|jpeg|webp|svg|css|js)",
            "headers": [
                {"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}
            ]
        }
    ]
}
with open(os.path.join(OUT, "vercel.json"), "w") as f:
    json.dump(vercel_cfg, f, indent=2)
print("  wrote vercel.json")

# ---------- robots.txt + sitemap.xml ----------
import datetime
TODAY = datetime.date.today().isoformat()
PRIORITIES = {
    "index": "1.0",
    "apk": "0.9",
    "onderhoud": "0.9",
    "specialistisch": "0.95",  # SEO-prio
    "banden": "0.8",
    "airco": "0.7",
    "schadeherstel": "0.8",
    "aankoopkeuring": "0.85",
    "distributieriem-vervangen": "0.8",
    "versnellingsbakolie-verversen": "0.8",
    "foutmelding-uitlezen": "0.85",
    "garage-beekbergen": "0.7",
    "garage-twello": "0.7",
    "garage-vaassen": "0.7",
    "garage-loenen": "0.7",
    "garage-klarenbeek": "0.7",
    "over-ons": "0.6",
    "contact": "0.85",
    "privacyverklaring": "0.3",
    "algemene-voorwaarden": "0.3",
}
# Lastmod per pagina: alleen bijwerken wanneer de inhoud echt wijzigt.
# Google negeert lastmod zodra hij onbetrouwbaar blijkt (elke build dezelfde
# datum voor alles), dus we hashen de pagina-inhoud (zonder de css-versie)
# en bewaren de datum van de laatste echte wijziging in sitemap-lastmod.json.
import hashlib as _hashlib, re as _re
LASTMOD_FILE = os.path.join(OUT, "sitemap-lastmod.json")
try:
    with open(LASTMOD_FILE) as _f:
        _lastmod_state = json.load(_f)
except (OSError, ValueError):
    _lastmod_state = {}

def _page_lastmod(slug):
    normalized = _re.sub(r'styles\.css\?v=[a-f0-9]+', 'styles.css', BUILT_HTML[slug])
    h = _hashlib.md5(normalized.encode()).hexdigest()
    entry = _lastmod_state.get(slug)
    if not entry or entry.get("hash") != h:
        entry = {"hash": h, "lastmod": TODAY}
        _lastmod_state[slug] = entry
    return entry["lastmod"]

sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
for slug, *_ in PAGES:
    url = "/" if slug == "index" else f"/{slug}"
    pr = PRIORITIES.get(slug, "0.5")
    cf = "weekly" if slug in ("index", "specialistisch") else "monthly"
    sitemap += f'  <url><loc>{BASE_URL}{url}</loc><lastmod>{_page_lastmod(slug)}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>\n'
sitemap += '</urlset>\n'
with open(LASTMOD_FILE, "w") as _f:
    json.dump(_lastmod_state, _f, indent=1)
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write(sitemap)
print("  wrote sitemap.xml")

robots = f'''User-agent: *
Allow: /
Disallow: /api/

# AI-crawlers expliciet toelaten (GEO): zonder eigen regel lezen sommige bots
# het ontbreken ervan als een blokkade.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: CCBot
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
'''
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(robots)
print("  wrote robots.txt")

# ---------- llms.txt (GEO: korte, citeerbare samenvatting voor AI-crawlers) ----------
llms = f'''# All-Cars Specialist B.V.

> Universele autogarage in Apeldoorn-Zuid, sinds 2013. Onderhoud, APK, diagnose en reparatie voor alle merken, met nadruk op het oplossen van complexe storingen en elektronicaproblemen die andere garages laten liggen.

## Bedrijfsgegevens
- Naam: All-Cars Specialist B.V.
- Adres: Surinameweg 33, 7333 PC Apeldoorn (Apeldoorn-Zuid)
- Telefoon: 06 33 93 57 20
- E-mail: info@all-cars-specialist.nl
- KvK: 56939485
- Opgericht: 2013
- Openingstijden: maandag t/m vrijdag 09:00-17:00, zaterdag en zondag gesloten
- Werkgebied: Apeldoorn, Apeldoorn-Zuid, Beekbergen, Loenen, Vaassen, Klarenbeek, Twello

## Diensten
- Auto-onderhoud en reparatie: {BASE_URL}/onderhoud
- APK-keuring: {BASE_URL}/apk
- Specialistisch onderhoud en diagnose: {BASE_URL}/specialistisch
- Banden, balanceren en uitlijnen: {BASE_URL}/banden
- Airco-service: {BASE_URL}/airco
- Schadeherstel: {BASE_URL}/schadeherstel
- Aankoopkeuring tweedehands auto: {BASE_URL}/aankoopkeuring
- Distributieriem vervangen: {BASE_URL}/distributieriem-vervangen
- Versnellingsbakolie verversen (handbak, automaat, DSG, CVT): {BASE_URL}/versnellingsbakolie-verversen
- Foutmelding uitlezen (diagnose): {BASE_URL}/foutmelding-uitlezen

## Werkgebied
- Garage voor Beekbergen, op tien minuten rijden: {BASE_URL}/garage-beekbergen
- Garage voor Twello, via de A1 op zo'n twintig minuten: {BASE_URL}/garage-twello
- Garage voor Vaassen, op ongeveer twintig minuten: {BASE_URL}/garage-vaassen
- Garage voor Loenen, op een kwartier: {BASE_URL}/garage-loenen
- Garage voor Klarenbeek, op een kwartier: {BASE_URL}/garage-klarenbeek

## Bedrijf
- Over ons: {BASE_URL}/over-ons
- Contact en afspraak: {BASE_URL}/contact
'''
with open(os.path.join(OUT, "llms.txt"), "w") as f:
    f.write(llms)
print("  wrote llms.txt")

# ---------- README.md ----------
readme = '''# All-Cars Specialist B.V. - Website

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
'''
with open(os.path.join(OUT, "README.md"), "w") as f:
    f.write(readme)
print("  wrote README.md")

# ---------- .gitignore ----------
gitignore = '''.DS_Store
node_modules/
.vercel/
.env
.env.local
*.log
'''
with open(os.path.join(OUT, ".gitignore"), "w") as f:
    f.write(gitignore)
print("  wrote .gitignore")

print()
print("=== BUILD COMPLEET ===")
print(f"Output map: {OUT}")
