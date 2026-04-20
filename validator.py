from command_ir import CommandIR


# ─── Action Category Sets ─────────────────────────────────────────────────────

# actions where a numeric 'level' parameter is relevant
LEVEL_ACTIONS = {
    "increase_brightness", "decrease_brightness", "set_brightness",
    "increase_volume",     "decrease_volume",     "set_volume",
}

# subset of LEVEL_ACTIONS where missing level is NOT an error (no default needed)
INR_DCR_LEVEL_ACTIONS = {
    "increase_brightness", "decrease_brightness",
    "increase_volume",     "decrease_volume",
}

# actions that open or close a single application / website
APPLICATION_ACTIONS = {
    "open_application",
    "close_application",
}


# ─── URL Targets ─────────────────────────────────────────────────────────────
# Maps user-friendly name → full URL.
# Used when the target is a website rather than an installed app.
# To add a new site: add one entry in the correct section below.

URL_TARGETS = {

    # ── Search Engines ──────────────────────────────────────────────────────────
    "google":               "https://www.google.com",
    "bing":                 "https://www.bing.com",
    "duckduckgo":           "https://www.duckduckgo.com",
    "yahoo":                "https://www.yahoo.com",
    "baidu":                "https://www.baidu.com",
    "ecosia":               "https://www.ecosia.org",
    "brave search":         "https://search.brave.com",
    "startpage":            "https://www.startpage.com",
    "yandex":               "https://www.yandex.com",
    "ask":                  "https://www.ask.com",

    # ── Social Media ────────────────────────────────────────────────────────────
    "instagram":            "https://www.instagram.com",
    "facebook":             "https://www.facebook.com",
    "twitter":              "https://www.twitter.com",
    "x":                    "https://www.x.com",
    "linkedin":             "https://www.linkedin.com",
    "snapchat":             "https://www.snapchat.com",
    "pinterest":            "https://www.pinterest.com",
    "reddit":               "https://www.reddit.com",
    "quora":                "https://www.quora.com",
    "tumblr":               "https://www.tumblr.com",
    "threads":              "https://www.threads.net",
    "koo":                  "https://www.kooapp.com",
    "sharechat":            "https://www.sharechat.com",
    "moj":                  "https://www.mojapp.in",
    "josh":                 "https://www.josh.in",

    # ── Video & Streaming ───────────────────────────────────────────────────────
    "youtube":              "https://www.youtube.com",
    "netflix":              "https://www.netflix.com",
    "hotstar":              "https://www.hotstar.com",
    "disney hotstar":       "https://www.hotstar.com",
    "disney plus":          "https://www.hotstar.com",
    "amazon prime":         "https://www.primevideo.com",
    "prime video":          "https://www.primevideo.com",
    "jiocinema":            "https://www.jiocinema.com",
    "sonyliv":              "https://www.sonyliv.com",
    "zee5":                 "https://www.zee5.com",
    "voot":                 "https://www.voot.com",
    "mxplayer":             "https://www.mxplayer.in",
    "aha":                  "https://www.aha.video",
    "sun nxt":              "https://www.sunnxt.com",
    "twitch":               "https://www.twitch.tv",
    "vimeo":                "https://www.vimeo.com",
    "dailymotion":          "https://www.dailymotion.com",
    "curiositystream":      "https://www.curiositystream.com",
    "crunchyroll":          "https://www.crunchyroll.com",
    "funimation":           "https://www.funimation.com",
    "peacock":              "https://www.peacocktv.com",
    "hulu":                 "https://www.hulu.com",
    "apple tv":             "https://tv.apple.com",
    "paramount plus":       "https://www.paramountplus.com",
    "discovery plus":       "https://www.discoveryplus.com",

    # ── Music ───────────────────────────────────────────────────────────────────
    "spotify":              "https://open.spotify.com",
    "gaana":                "https://www.gaana.com",
    "jiosaavn":             "https://www.jiosaavn.com",
    "saavn":                "https://www.jiosaavn.com",
    "wynk":                 "https://www.wynk.in",
    "hungama":              "https://www.hungama.com",
    "soundcloud":           "https://www.soundcloud.com",
    "apple music":          "https://music.apple.com",
    "youtube music":        "https://music.youtube.com",
    "amazon music":         "https://music.amazon.in",
    "tidal":                "https://www.tidal.com",
    "deezer":               "https://www.deezer.com",

    # ── Messaging ───────────────────────────────────────────────────────────────
    "whatsapp":             "https://web.whatsapp.com",
    "telegram":             "https://web.telegram.org",
    "discord":              "https://www.discord.com",
    "slack":                "https://www.slack.com",
    "teams":                "https://teams.microsoft.com",
    "microsoft teams":      "https://teams.microsoft.com",
    "signal":               "https://signal.org",
    "messenger":            "https://www.messenger.com",
    "skype":                "https://www.skype.com",
    "zoom":                 "https://www.zoom.us",
    "google meet":          "https://meet.google.com",
    "meet":                 "https://meet.google.com",
    "webex":                "https://www.webex.com",
    "matrix":               "https://app.element.io",

    # ── Email ───────────────────────────────────────────────────────────────────
    "gmail":                "https://mail.google.com",
    "outlook":              "https://outlook.live.com",
    "yahoo mail":           "https://mail.yahoo.com",
    "protonmail":           "https://mail.proton.me",
    "proton":               "https://mail.proton.me",
    "tutanota":             "https://www.tutanota.com",
    "zoho mail":            "https://mail.zoho.in",
    "rediffmail":           "https://mail.rediff.com",
    "fastmail":             "https://www.fastmail.com",
    "icloud mail":          "https://www.icloud.com/mail",

    # ── Shopping ────────────────────────────────────────────────────────────────
    "amazon":               "https://www.amazon.in",
    "flipkart":             "https://www.flipkart.com",
    "meesho":               "https://www.meesho.com",
    "myntra":               "https://www.myntra.com",
    "ajio":                 "https://www.ajio.com",
    "snapdeal":             "https://www.snapdeal.com",
    "nykaa":                "https://www.nykaa.com",
    "tata cliq":            "https://www.tatacliq.com",
    "croma":                "https://www.croma.com",
    "reliance digital":     "https://www.reliancedigital.in",
    "jiomart":              "https://www.jiomart.com",
    "bigbasket":            "https://www.bigbasket.com",
    "blinkit":              "https://www.blinkit.com",
    "zepto":                "https://www.zeptonow.com",
    "swiggy instamart":     "https://www.swiggy.com/instamart",
    "instamart":            "https://www.swiggy.com/instamart",
    "ebay":                 "https://www.ebay.in",
    "shopsy":               "https://www.shopsy.in",
    "lenskart":             "https://www.lenskart.com",
    "pepperfry":            "https://www.pepperfry.com",
    "firstcry":             "https://www.firstcry.com",
    "mamaearth":            "https://www.mamaearth.in",
    "boat":                 "https://www.boat-lifestyle.com",
    "bewakoof":             "https://www.bewakoof.com",
    "decathlon":            "https://www.decathlon.in",
    "ikea":                 "https://www.ikea.com/in",

    # ── Food & Delivery ─────────────────────────────────────────────────────────
    "swiggy":               "https://www.swiggy.com",
    "zomato":               "https://www.zomato.com",
    "dunzo":                "https://www.dunzo.com",

    # ── Travel ──────────────────────────────────────────────────────────────────
    "irctc":                "https://www.irctc.co.in",
    "makemytrip":           "https://www.makemytrip.com",
    "goibibo":              "https://www.goibibo.com",
    "cleartrip":            "https://www.cleartrip.com",
    "ixigo":                "https://www.ixigo.com",
    "yatra":                "https://www.yatra.com",
    "redbus":               "https://www.redbus.in",
    "booking":              "https://www.booking.com",
    "airbnb":               "https://www.airbnb.co.in",
    "agoda":                "https://www.agoda.com",
    "tripadvisor":          "https://www.tripadvisor.in",
    "oyo":                  "https://www.oyorooms.com",
    "uber":                 "https://www.uber.com",
    "ola":                  "https://www.olacabs.com",
    "rapido":               "https://www.rapido.bike",
    "google flights":       "https://www.google.com/flights",
    "indigo":               "https://www.goindigo.in",
    "air india":            "https://www.airindia.com",
    "spicejet":             "https://www.spicejet.com",

    # ── Finance & Banking ───────────────────────────────────────────────────────
    "paytm":                "https://www.paytm.com",
    "phonepe":              "https://www.phonepe.com",
    "gpay":                 "https://pay.google.com",
    "google pay":           "https://pay.google.com",
    "bhim":                 "https://www.bhimupi.org.in",
    "zerodha":              "https://www.zerodha.com",
    "groww":                "https://www.groww.in",
    "upstox":               "https://www.upstox.com",
    "angelone":             "https://www.angelone.in",
    "smallcase":            "https://www.smallcase.com",
    "coin":                 "https://coin.zerodha.com",
    "nse":                  "https://www.nseindia.com",
    "bse":                  "https://www.bseindia.com",
    "moneycontrol":         "https://www.moneycontrol.com",
    "economictimes":        "https://economictimes.indiatimes.com",
    "bankbazaar":           "https://www.bankbazaar.com",
    "policybazaar":         "https://www.policybazaar.com",
    "cred":                 "https://www.cred.club",
    "mobikwik":             "https://www.mobikwik.com",
    "sbi":                  "https://www.onlinesbi.sbi",
    "hdfc":                 "https://www.hdfcbank.com",
    "icici":                "https://www.icicibank.com",
    "axis bank":            "https://www.axisbank.com",
    "kotak":                "https://www.kotak.com",
    "yes bank":             "https://www.yesbank.in",
    "fi money":             "https://fi.money",
    "jupiter":              "https://www.jupitermoney.com",
    "niyo":                 "https://www.goniyo.com",
    "robinhood":            "https://www.robinhood.com",
    "etoro":                "https://www.etoro.com",

    # ── News ────────────────────────────────────────────────────────────────────
    "times of india":       "https://timesofindia.indiatimes.com",
    "toi":                  "https://timesofindia.indiatimes.com",
    "hindustan times":      "https://www.hindustantimes.com",
    "the hindu":            "https://www.thehindu.com",
    "ndtv":                 "https://www.ndtv.com",
    "india today":          "https://www.indiatoday.in",
    "aaj tak":              "https://www.aajtak.in",
    "zee news":             "https://zeenews.india.com",
    "news18":               "https://www.news18.com",
    "republic world":       "https://www.republicworld.com",
    "the wire":             "https://www.thewire.in",
    "scroll":               "https://scroll.in",
    "the print":            "https://theprint.in",
    "livemint":             "https://www.livemint.com",
    "business standard":    "https://www.business-standard.com",
    "financial express":    "https://www.financialexpress.com",
    "bbc":                  "https://www.bbc.com",
    "cnn":                  "https://www.cnn.com",
    "reuters":              "https://www.reuters.com",
    "bloomberg":            "https://www.bloomberg.com",
    "al jazeera":           "https://www.aljazeera.com",
    "wion":                 "https://www.wionews.com",
    "firstpost":            "https://www.firstpost.com",
    "deccan herald":        "https://www.deccanherald.com",
    "indian express":       "https://indianexpress.com",
    "the guardian":         "https://www.theguardian.com",
    "new york times":       "https://www.nytimes.com",
    "nyt":                  "https://www.nytimes.com",
    "washington post":      "https://www.washingtonpost.com",
    "cricbuzz":             "https://www.cricbuzz.com",
    "espncricinfo":         "https://www.espncricinfo.com",
    "cricinfo":             "https://www.espncricinfo.com",

    # ── Education ───────────────────────────────────────────────────────────────
    "wikipedia":            "https://www.wikipedia.org",
    "byjus":                "https://www.byjus.com",
    "unacademy":            "https://www.unacademy.com",
    "vedantu":              "https://www.vedantu.com",
    "khan academy":         "https://www.khanacademy.org",
    "coursera":             "https://www.coursera.org",
    "udemy":                "https://www.udemy.com",
    "edx":                  "https://www.edx.org",
    "skillshare":           "https://www.skillshare.com",
    "duolingo":             "https://www.duolingo.com",
    "w3schools":            "https://www.w3schools.com",
    "geeksforgeeks":        "https://www.geeksforgeeks.org",
    "javatpoint":           "https://www.javatpoint.com",
    "tutorialspoint":       "https://www.tutorialspoint.com",
    "nptel":                "https://www.nptel.ac.in",
    "swayam":               "https://www.swayam.gov.in",
    "mit opencourseware":   "https://www.ocw.mit.edu",
    "brilliant":            "https://www.brilliant.org",
    "codecademy":           "https://www.codecademy.com",
    "freecodecamp":         "https://www.freecodecamp.org",

    # ── Productivity & Cloud ─────────────────────────────────────────────────────
    "google drive":         "https://drive.google.com",
    "drive":                "https://drive.google.com",
    "google docs":          "https://docs.google.com",
    "docs":                 "https://docs.google.com",
    "google sheets":        "https://sheets.google.com",
    "sheets":               "https://sheets.google.com",
    "google slides":        "https://slides.google.com",
    "slides":               "https://slides.google.com",
    "google forms":         "https://forms.google.com",
    "google calendar":      "https://calendar.google.com",
    "calendar":             "https://calendar.google.com",
    "google photos":        "https://photos.google.com",
    "photos":               "https://photos.google.com",
    "onedrive":             "https://onedrive.live.com",
    "dropbox":              "https://www.dropbox.com",
    "notion":               "https://www.notion.so",
    "trello":               "https://www.trello.com",
    "asana":                "https://www.asana.com",
    "jira":                 "https://www.atlassian.com/software/jira",
    "confluence":           "https://www.atlassian.com/software/confluence",
    "monday":               "https://www.monday.com",
    "airtable":             "https://www.airtable.com",
    "evernote":             "https://www.evernote.com",
    "obsidian":             "https://www.obsidian.md",      # web fallback for obsidian
    "linear":               "https://www.linear.app",
    "clickup":              "https://www.clickup.com",
    "basecamp":             "https://www.basecamp.com",
    "miro":                 "https://www.miro.com",
    "loom":                 "https://www.loom.com",

    # ── AI Tools ────────────────────────────────────────────────────────────────
    "chatgpt":              "https://www.chatgpt.com",
    "claude":               "https://www.claude.ai",
    "gemini":               "https://gemini.google.com",
    "copilot":              "https://copilot.microsoft.com",
    "perplexity":           "https://www.perplexity.ai",
    "midjourney":           "https://www.midjourney.com",
    "canva":                "https://www.canva.com",
    "grammarly":            "https://www.grammarly.com",
    "deepl":                "https://www.deepl.com",
    "hugging face":         "https://www.huggingface.co",
    "stable diffusion":     "https://stablediffusionweb.com",
    "runway":               "https://www.runwayml.com",
    "suno":                 "https://www.suno.ai",
    "udio":                 "https://www.udio.com",

    # ── Developer Tools ─────────────────────────────────────────────────────────
    "github":               "https://www.github.com",
    "gitlab":               "https://www.gitlab.com",
    "stackoverflow":        "https://www.stackoverflow.com",
    "stack overflow":       "https://www.stackoverflow.com",
    "codepen":              "https://www.codepen.io",
    "replit":               "https://www.replit.com",
    "colab":                "https://colab.research.google.com",
    "google colab":         "https://colab.research.google.com",
    "kaggle":               "https://www.kaggle.com",
    "leetcode":             "https://www.leetcode.com",
    "hackerrank":           "https://www.hackerrank.com",
    "codeforces":           "https://www.codeforces.com",
    "npm":                  "https://www.npmjs.com",
    "pypi":                 "https://pypi.org",
    "docker hub":           "https://hub.docker.com",
    "vercel":               "https://www.vercel.com",
    "netlify":              "https://www.netlify.com",
    "heroku":               "https://www.heroku.com",
    "aws":                  "https://aws.amazon.com",
    "azure":                "https://azure.microsoft.com",
    "gcp":                  "https://cloud.google.com",
    "google cloud":         "https://cloud.google.com",
    "digitalocean":         "https://www.digitalocean.com",
    "cloudflare":           "https://www.cloudflare.com",
    "postman":              "https://www.postman.com",
    "figma":                "https://www.figma.com",
    "bitbucket":            "https://www.bitbucket.org",
    "jsfiddle":             "https://www.jsfiddle.net",
    "codesandbox":          "https://codesandbox.io",
    "stackblitz":           "https://stackblitz.com",
    "render":               "https://www.render.com",
    "railway":              "https://railway.app",
    "supabase":             "https://supabase.com",
    "firebase":             "https://firebase.google.com",
    "mongodb atlas":        "https://www.mongodb.com/atlas",

    # ── Government ──────────────────────────────────────────────────────────────
    "digilocker":           "https://www.digilocker.gov.in",
    "aadhaar":              "https://www.uidai.gov.in",
    "uidai":                "https://www.uidai.gov.in",
    "pan":                  "https://www.incometax.gov.in",
    "income tax":           "https://www.incometax.gov.in",
    "gst":                  "https://www.gst.gov.in",
    "epfo":                 "https://www.epfindia.gov.in",
    "passport":             "https://www.passportindia.gov.in",
    "umang":                "https://web.umang.gov.in",
    "india gov":            "https://www.india.gov.in",
    "mca":                  "https://www.mca.gov.in",

    # ── Jobs ────────────────────────────────────────────────────────────────────
    "naukri":               "https://www.naukri.com",
    "linkedin jobs":        "https://www.linkedin.com/jobs",
    "indeed":               "https://www.indeed.co.in",
    "shine":                "https://www.shine.com",
    "monster":              "https://www.monsterindia.com",
    "internshala":          "https://www.internshala.com",
    "instahyre":            "https://www.instahyre.com",
    "wellfound":            "https://www.wellfound.com",
    "angel list":           "https://www.wellfound.com",
    "glassdoor":            "https://www.glassdoor.co.in",

    # ── Health ──────────────────────────────────────────────────────────────────
    "practo":               "https://www.practo.com",
    "1mg":                  "https://www.1mg.com",
    "netmeds":              "https://www.netmeds.com",
    "pharmeasy":            "https://www.pharmeasy.in",
    "apollo pharmacy":      "https://www.apollopharmacy.in",
    "healthkart":           "https://www.healthkart.com",
    "tata 1mg":             "https://www.1mg.com",

    # ── Maps & Local ────────────────────────────────────────────────────────────
    "google maps":          "https://maps.google.com",
    "maps":                 "https://maps.google.com",
    "ola maps":             "https://www.olamaps.io",
    "mapmy india":          "https://www.mapmyindia.com",
    "justdial":             "https://www.justdial.com",
    "sulekha":              "https://www.sulekha.com",
    "urban company":        "https://www.urbancompany.com",
    "openstreetmap":        "https://www.openstreetmap.org",

    # ── Miscellaneous ───────────────────────────────────────────────────────────
    "wayback machine":      "https://web.archive.org",
    "archive":              "https://web.archive.org",
    "wolframalpha":         "https://www.wolframalpha.com",
    "translate":            "https://translate.google.com",
    "google translate":     "https://translate.google.com",
    "pastebin":             "https://www.pastebin.com",
    "typeform":             "https://www.typeform.com",
    "surveymonkey":         "https://www.surveymonkey.com",
    "linktree":             "https://www.linktr.ee",
    "medium":               "https://www.medium.com",
    "substack":             "https://www.substack.com",
    "wordpress":            "https://www.wordpress.com",
    "blogger":              "https://www.blogger.com",
    "wix":                  "https://www.wix.com",
    "squarespace":          "https://www.squarespace.com",
    "godaddy":              "https://www.godaddy.com",
    "namecheap":            "https://www.namecheap.com",
    "producthunt":          "https://www.producthunt.com",
    "hacker news":          "https://news.ycombinator.com",
    "hn":                   "https://news.ycombinator.com",
    "devto":                "https://www.dev.to",
    "hashnode":             "https://www.hashnode.com",
    "goodreads":            "https://www.goodreads.com",
    "imdb":                 "https://www.imdb.com",
    "letterboxd":           "https://www.letterboxd.com",
}


# ─── App Targets ─────────────────────────────────────────────────────────────
# Maps user-friendly name → Windows executable name.
# Used when the target is an installed application.
# To add a new app: add one entry in the correct section below.

APP_TARGETS = {

    # ── Browsers ────────────────────────────────────────────────────────────────
    "chrome":               "chrome",
    "google chrome":        "chrome",
    "firefox":              "firefox",
    "mozilla firefox":      "firefox",
    "edge":                 "msedge",
    "microsoft edge":       "msedge",
    "opera":                "opera",
    "brave":                "brave",
    "brave browser":        "brave",
    "vivaldi":              "vivaldi",
    "tor":                  "tor browser",

    # ── Code Editors & IDEs ─────────────────────────────────────────────────────
    "vs code":              "code",
    "vscode":               "code",
    "visual studio code":   "code",
    "visual studio":        "devenv",
    "pycharm":              "pycharm64",
    "intellij":             "idea64",
    "intellij idea":        "idea64",
    "webstorm":             "webstorm64",
    "android studio":       "studio64",
    "eclipse":              "eclipse",
    "sublime":              "sublime_text",
    "sublime text":         "sublime_text",
    "notepad++":            "notepad++",
    "notepad plus plus":    "notepad++",
    "atom":                 "atom",
    "cursor":               "cursor",
    "windsurf":             "windsurf",
    "zed":                  "zed",

    # ── Terminals ───────────────────────────────────────────────────────────────
    "terminal":             "wt",
    "windows terminal":     "wt",
    "cmd":                  "cmd",
    "command prompt":       "cmd",
    "powershell":           "powershell",
    "git bash":             "git-bash",

    # ── Microsoft Office ────────────────────────────────────────────────────────
    "word":                 "winword",
    "microsoft word":       "winword",
    "excel":                "excel",
    "microsoft excel":      "excel",
    "powerpoint":           "powerpnt",
    "microsoft powerpoint": "powerpnt",
    "outlook":              "outlook",
    "microsoft outlook":    "outlook",
    "onenote":              "onenote",
    "microsoft onenote":    "onenote",
    "teams":                "ms-teams",
    "microsoft teams":      "ms-teams",
    "access":               "msaccess",
    "publisher":            "mspub",

    # ── Notes & PKM ─────────────────────────────────────────────────────────────
    "obsidian":             "obsidian",         # installed app — NOT a URL
    "logseq":               "logseq",
    "notion":               "notion",
    "typora":               "typora",

    # ── Communication ───────────────────────────────────────────────────────────
    "discord":              "discord",
    "slack":                "slack",
    "zoom":                 "zoom",
    "skype":                "skype",
    "telegram":             "telegram",
    "whatsapp":             "whatsapp",
    "signal":               "signal",

    # ── Media & Entertainment ───────────────────────────────────────────────────
    "vlc":                  "vlc",
    "vlc player":           "vlc",
    "media player":         "wmplayer",
    "windows media player": "wmplayer",
    "spotify":              "spotify",
    "itunes":               "itunes",
    "mpv":                  "mpv",
    "potplayer":            "potplayer",
    "obs":                  "obs64",
    "obs studio":           "obs64",
    "foobar":               "foobar2000",
    "foobar2000":           "foobar2000",
    "audacity":             "audacity",
    "handbrake":            "handbrake",
    "kdenlive":             "kdenlive",
    "davinci resolve":      "resolve",
    "davinci":              "resolve",
    "capcut":               "capcut",

    # ── System & Utilities ──────────────────────────────────────────────────────
    "notepad":              "notepad",
    "paint":                "mspaint",
    "ms paint":             "mspaint",
    "calculator":           "calc",
    "task manager":         "taskmgr",
    "file explorer":        "explorer",
    "explorer":             "explorer",
    "control panel":        "control",
    "registry editor":      "regedit",
    "device manager":       "devmgmt.msc",
    "disk management":      "diskmgmt.msc",
    "snipping tool":        "snippingtool",
    "sticky notes":         "stikynot",
    "clock":                "clock",
    "settings":             "ms-settings:",
    "windows settings":     "ms-settings:",
    "windows defender":     "windowsdefender:",

    # ── Design & Creative ───────────────────────────────────────────────────────
    "photoshop":            "photoshop",
    "adobe photoshop":      "photoshop",
    "illustrator":          "illustrator",
    "adobe illustrator":    "illustrator",
    "premiere":             "premiere",
    "adobe premiere":       "premiere",
    "after effects":        "afterfx",
    "adobe after effects":  "afterfx",
    "lightroom":            "lightroom",
    "adobe lightroom":      "lightroom",
    "figma":                "figma",
    "blender":              "blender",
    "gimp":                 "gimp-2",
    "inkscape":             "inkscape",

    # ── File & Cloud ────────────────────────────────────────────────────────────
    "winrar":               "winrar",
    "7zip":                 "7zfm",
    "7-zip":                "7zfm",
    "dropbox":              "dropbox",
    "onedrive":             "onedrive",
    "everything":           "everything",
    "total commander":      "totalcmd",

    # ── Games & Gaming ──────────────────────────────────────────────────────────
    "steam":                "steam",
    "epic games":           "epicgameslauncher",
    "epic":                 "epicgameslauncher",
    "minecraft":            "minecraft",
    "origin":               "origin",
    "battle.net":           "battle.net",
    "ubisoft connect":      "ubisoftconnect",
    "uplay":                "ubisoftconnect",
    "gog galaxy":           "gogalaxy",
    "xbox":                 "xboxapp",

    # ── Security & VPN ──────────────────────────────────────────────────────────
    "nordvpn":              "nordvpn",
    "expressvpn":           "expressvpn",
    "malwarebytes":         "malwarebytes",
    "avast":                "avast",
    "kaspersky":            "kaspersky",
    "bitwarden":            "bitwarden",

    # ── Database Tools ──────────────────────────────────────────────────────────
    "postman":              "postman",
    "mysql workbench":      "mysqlworkbench",
    "pgadmin":              "pgadmin4",
    "mongodb compass":      "mongodbcompass",
    "dbeaver":              "dbeaver",
    "tableplus":            "tableplus",
    "insomnia":             "insomnia",
    "docker":               "docker desktop",
    "docker desktop":       "docker desktop",

    # ── Other Dev ───────────────────────────────────────────────────────────────
    "filezilla":            "filezilla",
    "putty":                "putty",
    "winscp":               "winscp",
    "virtualbox":           "virtualbox",
    "vmware":               "vmware",
}


# ─── Validator Function ───────────────────────────────────────────────────────

def validator(command_ir: CommandIR) -> CommandIR:

    # ── Level parameter validation ────────────────────────────────────────────
    if command_ir.action in LEVEL_ACTIONS:
        level = command_ir.parameters.get("level")

        if level is None and command_ir.action not in INR_DCR_LEVEL_ACTIONS:
            command_ir.parameters["level"] = 50
            command_ir.warnings.append("No level provided. Defaulted to 50.")

        elif level is not None:
            if level > 100:
                command_ir.parameters["level"] = 100
                command_ir.warnings.append("Level provided greater than 100. Capped down to 100.")
            if level < 0:
                command_ir.parameters["level"] = 0
                command_ir.warnings.append("Level provided less than 0. Set to 0.")

    # ── Application target validation ─────────────────────────────────────────
    target = command_ir.target
    if command_ir.action in APPLICATION_ACTIONS and target is not None:

        force_web = command_ir.parameters.get("force_web", False)

        # force_web: skip installed-app lookup entirely, go straight to URL
        if force_web:
            if target in URL_TARGETS:
                command_ir.parameters["fallback_url"] = URL_TARGETS[target]
            else:
                command_ir.parameters["fallback_url"] = "https://www." + target + ".com"
            return command_ir

        # normal flow: try installed app first
        if target in APP_TARGETS:
            command_ir.target = APP_TARGETS[target]
            # use the ORIGINAL name for URL fallback lookup, not the resolved executable
            command_ir.parameters["fallback_url"] = URL_TARGETS.get(target, None)

        # not an installed app — try as a website
        elif target in URL_TARGETS:
            command_ir.target = URL_TARGETS[target]
            command_ir.parameters["fallback_url"] = None

        # unknown target — pass as-is and attempt to open directly
        else:
            command_ir.parameters["fallback_url"] = None

    return command_ir
