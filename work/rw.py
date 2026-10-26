# -*- coding: utf-8 -*-
import re
s = open('index.html', encoding='utf-8').read()

# strip existing nbsp; re-applied at the end to text nodes only
s = s.replace('\u00a0', ' ')

RB = r'<(p|li|figcaption|h1|h2)\b([^>]*)>(.*?)</\1>'

def blocks(blk):
    return list(re.finditer(RB, blk, re.S))

def apply(blk, repl):
    ms = blocks(blk)
    out = blk
    for idx in sorted(repl, reverse=True):
        m = ms[idx]
        out = out[:m.start()] + f'<{m.group(1)}{m.group(2)}>{repl[idx]}</{m.group(1)}>' + out[m.end():]
    return out

# ============================== ENGLISH ==============================
EN = {}
EN[2] = ('Your domain has no DMARC record, and its SPF policy ends in a soft fail.\n'
 '      A stranger can therefore send email to your customers that appears to come from\n'
 '      your reservations address: a deposit request, a table confirmation, a link.\n'
 '      Nothing warns you when it happens. The second problem, a menu page that never\n'
 '      loads, is easier to notice and easier to fix. Both can be dealt with today.')

EN[4] = ('Two DNS records decide whether a message sent from your domain is genuine:\n'
 '  SPF and DMARC. The first is published but permissive, and the second is missing.\n'
 '  Neither one prevents forgery by itself. Together, as they stand, they amount to an\n'
 '  open invitation.')

EN[6] = ('An email arrives from <span class="mono">reservations@aftereightsousse.tn</span>.\n'
 '        It reaches the inbox, survives a quick look, and asks a customer to confirm a\n'
 '        booking by paying a deposit into an account you do not control. Without DMARC,\n'
 '        the receiving server has no instruction to reject or quarantine it, and no\n'
 '        report reaches you afterwards.')

EN[7] = ('A one-line DMARC record in monitor mode costs nothing and cannot break your\n'
 '  mail, because at <span class="mono">p=none</span> it asks no server to block\n'
 '  anything. It only starts sending you reports. Move to\n'
 '  <span class="mono">p=quarantine</span> once those reports come back clean, usually\n'
 '  after two to four weeks.')

EN[9] = 'Probably known already · this is how it works'

EN[10] = ('Every dish and every price is out of reach, because the menu never\n'
 '      arrives. Nothing on the page is broken. It is waiting for data that never\n'
 '      comes.')

EN[11] = ('The site is a React application. It loads a single JSON file from a Heroku\n'
 '        app and draws the menu only once that file arrives. The Heroku app answers\n'
 '        <span class="mono">503</span>, so the request fails, and the code that draws\n'
 '        the menu has no error branch. The spinner stays on screen.')

EN[12] = ('<b>What works.</b> The landing route <span class="mono">/</span>, which needs\n'
 '      no data: a photograph, a heading and two buttons. This is what the owner sees\n'
 '      when checking the site.')

EN[13] = ('<b>What does not.</b> The route <span class="mono">/#/menu</span>, one click\n'
 '      further in. The green mark is the loading spinner\n'
 '      <span class="mono">loader.89ba5735….png</span>, still turning after six\n'
 '      seconds. Nothing else ever renders.')

EN[14] = ('Both screenshots were taken on 26 October 2026 at 01:00 Africa/Tunis, in a\n'
 '  clean browser profile at 1240×800, six seconds after load. The menu capture is\n'
 '  unedited apart from a crop of the empty margins.')

EN[15] = ('<strong>The landing page is unaffected.</strong> It is a separate route with\n'
 '    no data dependency, which is exactly why the fault is easy to miss. The site looks\n'
 '    healthy from the front door, and the failure waits one click behind it.')

EN[16] = 'Why the spinner appears, in one drawing'

EN[17] = ('Four steps succeed and the fifth has nowhere to go. The missing arrow is the\n'
 '  whole fault. Compare the two possible outcomes of the backend call.')

EN[18] = ('<b>The failure branch, and the branch that was never written.</b>\n'
 '    <span class="mono">Home.js</span> renders the spinner while its\n'
 '    <span class="mono">data</span> state is still <span class="mono">null</span>, and\n'
 '    only a resolved promise ever sets it. Because <span class="mono">App.js</span>\n'
 '    chains <span class="mono">.then()</span> without a\n'
 '    <span class="mono">.catch()</span>, a 503 leaves the state untouched instead of\n'
 '    raising anything visible. Read from the published source map, 26 October 2026.')

EN[23] = ('<strong>Two ways out, and the cheaper one is better.</strong> Restarting the\n'
 '    Heroku dyno brings the menu back within minutes, but the failure returns as soon as\n'
 '    the app sleeps or the free hours run out. Moving the menu JSON into the GitHub\n'
 '    Pages repository as a static file removes the backend, the 503 and the bill at\n'
 '    once.')

EN[25] = ('Severity here means business impact, not CVSS theatre. A forged email\n'
 '  outranks a dead menu page: the menu costs you sales, while the email can cost your\n'
 '  customers money, and it damages your reputation as well as your takings. Section 07\n'
 '  gives the schedule for each fix. This column records severity only.')

EN[26] = 'Two of your subdomains can be claimed by a stranger'

EN[27] = ('This finding looks the most alarming of the three and is the least urgent.\n'
 '  It matters for one specific reason: the address would be real, and the certificate\n'
 '  would be valid.')

EN[32] = ('<strong>What this is worth, and what it is not.</strong> No passwords and no\n'
 '    customer data are exposed, because the site has no login and sets no cookies. What\n'
 '    is at stake is your name: a link people already half-trust, announcing that the\n'
 '    menu has moved and asking for a card number. That is why it ranks below the dead\n'
 '    menu. It only works if somebody notices you, whereas nobody has to notice that a\n'
 '    menu will not load.')

EN[34] = 'Three smaller problems'

EN[35] = ('None of these exposes your data to anyone. The source map is notable in the\n'
 '  other direction: it is how I read every file on this page without touching your\n'
 '  server. That is a fair trade for a brochure site and a poor habit for anything with a\n'
 '  login behind it. If you leave it published, be aware that the backend URL and the\n'
 '  full routing logic are public.')

EN[38] = ('Steps 1 and 2 each take under an hour, and neither needs a developer. Step 1\n'
 '  is the only one that changes a number you can see.')

# ============================== FRENCH ==============================
FR = {}
FR[2] = ("Aucun enregistrement DMARC n'est publié sur votre domaine, et votre politique\n"
 "      SPF se termine par un échec modéré. Un inconnu peut donc envoyer à vos clients des\n"
 "      e-mails qui semblent provenir de votre adresse de réservation : demande d'acompte,\n"
 "      confirmation de table, lien. Rien ne vous avertit lorsque cela se produit. Le\n"
 "      second problème, un menu qui ne s'affiche jamais, se remarque plus facilement et\n"
 "      se corrige plus vite. Les deux peuvent être réglés aujourd'hui.")

FR[4] = ("Deux enregistrements DNS déterminent si un message envoyé depuis votre domaine\n"
 "  est authentique : SPF et DMARC. Le premier est publié mais permissif, et le second\n"
 "  est absent. Aucun des deux n'empêche à lui seul une falsification. Tels qu'ils sont,\n"
 "  ils reviennent ensemble à une invitation ouverte.")

FR[6] = ("Un e-mail arrive de <span class=\"mono\">reservations@aftereightsousse.tn</span>.\n"
 "        Il atteint la boîte de réception, résiste à un examen rapide et demande à un\n"
 "        client de confirmer une réservation en versant un acompte sur un compte que\n"
 "        vous ne contrôlez pas. Sans DMARC, le serveur destinataire n'a reçu aucune\n"
 "        consigne pour le rejeter ou le mettre en quarantaine, et aucun rapport ne vous\n"
 "        parvient ensuite.")

FR[7] = ("Un enregistrement DMARC d'une seule ligne, en mode surveillance, ne coûte rien\n"
 "  et ne peut pas casser votre messagerie, car à <span class=\"mono\">p=none</span> il\n"
 "  ne demande à aucun serveur de bloquer quoi que ce soit. Il commence simplement à vous\n"
 "  envoyer des rapports. Passez à <span class=\"mono\">p=quarantine</span> lorsque ces\n"
 "  rapports reviennent propres, en général après deux à quatre semaines.")

FR[9] = 'Probablement déjà connu · voici comment cela fonctionne'

FR[10] = ("Le menu ne se charge jamais, donc chaque plat et chaque prix restent hors de\n"
 "      portée. Rien n'est cassé dans la page. Elle attend des données qui n'arrivent\n"
 "      pas.")

FR[11] = ("Le site est une application React. Il charge un unique fichier JSON depuis une\n"
 "        application Heroku et ne dessine le menu qu'une fois ce fichier reçu.\n"
 "        L'application Heroku répond <span class=\"mono\">503</span>, la requête échoue,\n"
 "        et le code qui affiche le menu ne comporte aucune branche d'erreur. L'indicateur\n"
 "        reste à l'écran.")

FR[12] = ("<b>Ce qui fonctionne.</b> La page d'accueil <span class=\"mono\">/</span>, qui ne\n"
 "      dépend d'aucune donnée : une photographie, un titre et deux boutons. C'est ce que\n"
 "      voit le propriétaire lorsqu'il consulte son site.")

FR[13] = ("<b>Ce qui ne fonctionne pas.</b> La page <span class=\"mono\">/#/menu</span>,\n"
 "      située un clic plus loin. La marque verte est l'indicateur de chargement\n"
 "      <span class=\"mono\">loader.89ba5735….png</span>, toujours en rotation après six\n"
 "      secondes. Rien d'autre ne s'affiche.")

FR[14] = ("Les deux captures ont été prises le 26 octobre 2026 à 01:00 (Africa/Tunis),\n"
 "  dans un profil de navigateur vierge, en 1240×800, six secondes après le chargement.\n"
 "  La capture du menu n'est pas retouchée, hormis un recadrage des marges vides.")

FR[15] = ("<strong>La page d'accueil n'est pas affectée.</strong> C'est une route\n"
 "    distincte, sans dépendance à des données, et c'est précisément pour cela que la\n"
 "    panne se remarque peu. Le site paraît sain depuis la porte d'entrée, et la panne\n"
 "    attend un clic plus loin.")

FR[16] = 'Pourquoi cet indicateur apparaît, en un schéma'

FR[17] = ("Quatre étapes aboutissent, et la cinquième n'a nulle part où aller. La flèche\n"
 "  manquante, c'est le défaut tout entier. Comparez les deux issues possibles de l'appel\n"
 "  au backend.")

FR[18] = ("<b>La branche d'échec, et celle qui n'a jamais été écrite.</b>\n"
 "    <span class=\"mono\">Home.js</span> affiche l'indicateur tant que son état\n"
 "    <span class=\"mono\">data</span> vaut <span class=\"mono\">null</span>, et seule une\n"
 "    promesse résolue le renseigne. Comme <span class=\"mono\">App.js</span> enchaîne un\n"
 "    <span class=\"mono\">.then()</span> sans aucun\n"
 "    <span class=\"mono\">.catch()</span>, un 503 laisse l'état intact au lieu de lever\n"
 "    quoi que ce soit de visible. Lu dans le fichier source publié, le 26 octobre 2026.")

FR[23] = ("<strong>Deux issues, et la moins coûteuse est la meilleure.</strong> Redémarrer\n"
 "    le dyno Heroku ramène le menu en quelques minutes, mais la panne reviendra dès que\n"
 "    l'application s'endormira ou que les heures gratuites seront épuisées. Déplacer le\n"
 "    JSON du menu dans le dépôt GitHub Pages, en fichier statique, supprime d'un même\n"
 "    geste le backend, le 503 et la facture.")

FR[25] = ("La gravité, ici, désigne un impact commercial et non du théâtre autour d'un\n"
 "  score CVSS. Un e-mail falsifié primerait sur un menu mort : le menu vous coûte des\n"
 "  ventes, tandis que l'e-mail peut coûter de l'argent à vos clients et entame votre\n"
 "  réputation autant que votre chiffre d'affaires. La section 07 précise le calendrier de\n"
 "  chaque correction. Cette colonne n'indique que la gravité.")

FR[26] = 'Deux de vos sous-domaines peuvent être revendiqués par un inconnu'

FR[27] = ("C'est le constat le plus alarmant des trois en apparence, et le moins urgent.\n"
 "  Il compte pour une raison précise : l'adresse serait réelle, et le certificat serait\n"
 "  valide.")

FR[32] = ("<strong>Ce que cela vaut, et ce que cela ne vaut pas.</strong> Aucun mot de\n"
 "    passe ni donnée client n'est exposé, car le site ne comporte pas de connexion et ne\n"
 "    dépose aucun cookie. Ce qui est en jeu, c'est votre nom : un lien auquel on accorde\n"
 "    déjà une demi-confiance, annonçant que le menu a déménagé et réclamant un numéro de\n"
 "    carte. C'est pourquoi il passe après le menu mort. Il ne fonctionne que si\n"
 "    quelqu'un vous remarque, alors que personne n'a besoin de remarquer qu'un menu ne se\n"
 "    charge pas.")

FR[34] = 'Trois problèmes plus mineurs'

FR[35] = ("Aucun de ces points ne livre vos données à quiconque. Le fichier source est\n"
 "  remarquable en sens inverse : c'est par lui que j'ai lu chaque fichier de cette page\n"
 "  sans toucher à votre serveur. Le compromis est raisonnable pour un site vitrine, et\n"
 "  fâcheux pour tout ce qui cache une connexion derrière. Si vous le laissez en ligne,\n"
 "  sachez que l'adresse du backend et toute la logique de routage sont publiques.")

FR[38] = ("Les étapes 1 et 2 demandent chacune moins d'une heure, et aucune ne nécessite\n"
 "  de développeur. L'étape 1 est la seule qui fasse évoluer un chiffre que vous pouvez\n"
 "  constater.")

FR[39] = ("Les cinq premières étapes réparent ce qui est cassé. La sixième relève d'une\n"
 "  suggestion, pas d'une réparation. Le site tient sur une seule page, sans réservation\n"
 "  en ligne, construit pour tenir une après-midi, et il fait ce pour quoi il a été fait.\n"
 "  C'est une porte d'entrée, pas encore une salle.")

# apply per language block
i = s.index('class="i18n fr"')
j = s.index('class="i18n en"')
fr_blk, en_blk = s[i:j], s[j:]

new_fr = apply(fr_blk, FR)
new_en = apply(en_blk, EN)
s = s[:i] + new_fr + new_en

# re-apply French nbsp to text nodes of the FR block only
i = s.index('class="i18n fr"'); j = s.index('class="i18n en"')
fr = s[i:j]
parts = re.split(r'(<[^>]*>)', fr)
for k, p in enumerate(parts):
    if p.startswith('<'):
        continue
    p = re.sub(r' ([:;!?])', '\u00a0\\1', p)
    p = p.replace('« ', '«\u00a0').replace(' »', '\u00a0»')
    parts[k] = p
s = s[:i] + ''.join(parts) + s[j:]

open('index.html', 'w', encoding='utf-8').write(s)
print('rewritten by index. nbsp in FR:', s[i:s.index('class="i18n en"')].count('\u00a0'))
