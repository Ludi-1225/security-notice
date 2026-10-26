# -*- coding: utf-8 -*-
import re
NB = '\u00a0'
s = open('index.html', encoding='utf-8').read()
fails = []
def sub(pat, new, tag):
    global s
    s2, k = re.compile(pat, re.S).subn(lambda m: new, s, count=1)
    if k != 1:
        fails.append(tag); return
    s = s2

# ---------- hero ----------
sub(r"<h1>N'importe qui peut envoyer des e-mails à vos clients en se faisant passer pour vous</h1>",
    "<h1>N'importe qui peut écrire à vos clients en se faisant passer pour vous</h1>", 'h1_fr')

sub(r'<p class="lead">Aucun enregistrement DMARC.*?règlent aujourd\'hui\.</p>',
 "      <p class=\"lead\">Aucun enregistrement DMARC n'est publié sur votre domaine, et\n"
 "      votre SPF se termine par un échec modéré. Rien n'empêche donc un inconnu\n"
 "      d'adresser à vos clients des e-mails qui semblent venir de votre adresse de\n"
 "      réservation"+NB+": demande d'acompte, confirmation de table, lien. Vous n'en\n"
 "      êtes jamais averti. Le second point, un menu qui ne s'affiche plus, se remarque\n"
 "      davantage mais se corrige plus vite. Les deux se règlent aujourd'hui.</p>", 'lead_fr')

# ---------- 01 DMARC ----------
sub(r'<p class="lede">Deux enregistrements DNS décident.*?constituent une invitation\.</p>',
 "  <p class=\"lede\">Deux enregistrements DNS déterminent si un message émis depuis\n"
 "  votre domaine est authentique"+NB+": SPF et DMARC. Le premier est publié, mais\n"
 "  permissif"+NB+"; le second est absent. Aucun des deux n'empêche à lui seul une\n"
 "  falsification, et leur combinaison actuelle revient à une invitation.</p>", 'lede01_fr')

sub(r'<p style="color:var\(--ink-2\);font-size:16px;margin:0">Un message arrivant de\s*\n\s*<span class="mono">reservations@aftereightsousse\.tn</span>.*?c\'est arrivé\.</p>',
 '        <p style="color:var(--ink-2);font-size:16px;margin:0">Un e-mail arrive de\n'
 '        <span class="mono">reservations@aftereightsousse.tn</span>. Il atteint la\n'
 '        boîte de réception, résiste à un premier coup d\'œil et demande à un client de\n'
 '        confirmer une réservation en versant un acompte sur un compte qui n\'est pas le\n'
 '        vôtre. Sans DMARC, le serveur destinataire n\'a reçu aucune consigne pour le\n'
 '        rejeter ou le mettre en quarantaine, et aucun rapport ne vous parvient\n'
 '        ensuite.</p>', 'panel01_fr')

sub(r'<p class="lede" style="margin-top:var\(--s5\);margin-bottom:0">Un enregistrement DMARC\s*\n\s*d\'une ligne.*?quatre semaines\.</p>',
 "  <p class=\"lede\" style=\"margin-top:var(--s5);margin-bottom:0\">Un enregistrement\n"
 "  DMARC d'une seule ligne, en mode surveillance, ne coûte rien et ne peut pas casser\n"
 "  votre messagerie"+NB+": à <span class=\"mono\">p=none</span>, il ne demande à aucun\n"
 "  serveur de bloquer quoi que ce soit. Il commence simplement à vous envoyer des\n"
 "  rapports. Passez à <span class=\"mono\">p=quarantine</span> lorsque ces rapports\n"
 "  reviennent propres, en général au bout de deux à quatre semaines.</p>", 'lede01b_fr')

# ---------- 02 menu ----------
sub(r'<p style="font:400 1\.3rem/1\.35 var\(--serif\);margin:0 0 var\(--s3\)">Chaque plat,\s*\n\s*chaque prix, inaccessibles\. La page n\'est pas cassée\. Elle attend\.</p>',
 '      <p style="font:400 1.3rem/1.35 var(--serif);margin:0 0 var(--s3)">Chaque plat,\n'
 '      chaque prix, inaccessibles. La page n\'est pas cassée. Elle attend.</p>', 'menu_lead_fr')

sub(r'<p style="color:var\(--ink-2\);font-size:16px;margin:0">Le site est une\s*\n\s*application React\. Elle charge un unique fichier JSON.*?L\'indicateur reste\.</p>',
 '        <p style="color:var(--ink-2);font-size:16px;margin:0">Le site est une\n'
 '        application React. Il charge un unique fichier JSON depuis une application\n'
 '        Heroku et ne dessine le menu qu\'une fois ce fichier reçu. L\'application Heroku\n'
 '        répond <span class="mono">503</span>'+NB+': la requête échoue, et le code qui\n'
 '        affiche le menu ne comporte aucune branche d\'erreur. L\'indicateur\n'
 '        subsiste.</p>', 'menu_panel_fr')

sub(r'<figcaption><b>Ce qui fonctionne\.</b>.*?vérifie son site\.</figcaption>',
 '      <figcaption><b>Ce qui fonctionne.</b> <span class="mono">/</span>, la page\n'
 '      d\'accueil, qui ne dépend d\'aucune donnée. Une photographie, un titre, deux\n'
 '      boutons. C\'est ce que voit le propriétaire lorsqu\'il consulte son site.</figcaption>', 'fig1_fr')

sub(r'<figcaption><b>Ce qui ne fonctionne pas\.</b>.*?Rien d\'autre ne s\'affiche\.</figcaption>',
 '      <figcaption><b>Ce qui ne fonctionne pas.</b>\n'
 '      <span class="mono">/#/menu</span>, la page située un clic plus loin. La marque\n'
 '      verte est l\'indicateur de chargement\n'
 '      <span class="mono">loader.89ba5735….png</span>, toujours en rotation après six\n'
 '      secondes. Rien d\'autre ne s\'affiche.</figcaption>', 'fig2_fr')

sub(r'<p class="src">Les deux captures ont été prises.*?marges vides\.</p>',
 "  <p class=\"src\">Les deux captures ont été prises le 26 octobre 2026 à 01"+NB+":00\n"
 "  (Africa/Tunis), dans un profil de navigateur vierge, en 1240×800, six secondes\n"
 "  après le chargement. La capture du menu n'est pas retouchée, hormis un recadrage\n"
 "  des marges vides.</p>", 'src_fr')

sub(r'<p style="margin:0"><strong>La page d\'accueil, elle, va bien\.</strong>.*?un clic plus loin\.</p>',
 "    <p style=\"margin:0\"><strong>La page d'accueil n'est pas affectée.</strong>\n"
 "    C'est une route distincte, sans dépendance à des données, et c'est précisément\n"
 "    pour cela que la panne se remarque peu"+NB+": le site paraît sain depuis la porte\n"
 "    d'entrée, et la panne attend un clic plus loin.</p>", 'note_menu_fr')

# ---------- 03 diagram ----------
sub(r'<p class="lede">Quatre étapes réussissent.*?l\'appel au backend\.</p>',
 "  <p class=\"lede\">Quatre étapes aboutissent, et la cinquième n'a nulle part où\n"
 "  aller. La flèche absente, c'est le défaut tout entier. Comparez les deux issues\n"
 "  possibles de l'appel au backend.</p>", 'lede03_fr')

sub(r'<figcaption><b>La branche d\'échec, et la branche qui n\'a jamais existé\.</b>.*?le\s*\n\s*26 octobre 2026\.</figcaption>',
 "    <figcaption><b>La branche d'échec, et celle qui n'a jamais été écrite.</b>\n"
 "    <span class=\"mono\">Home.js</span> affiche l'indicateur tant que son état\n"
 "    <span class=\"mono\">data</span> vaut <span class=\"mono\">null</span>, et seule\n"
 "    une promesse résolue le renseigne. Comme <span class=\"mono\">App.js</span>\n"
 "    enchaîne un <span class=\"mono\">.then()</span> sans aucun\n"
 "    <span class=\"mono\">.catch()</span>, un 503 laisse l'état intact au lieu de lever\n"
 "    quoi que ce soit de visible. Lu dans le fichier source publié, le 26 octobre\n"
 "    2026.</figcaption>", 'fig03_fr')

sub(r'<p style="margin:0"><strong>Deux issues, et la moins chère est la meilleure\.</strong>.*?le 503 et la facture\.</p>',
 "    <p style=\"margin:0\"><strong>Deux issues, et la moins coûteuse est la\n"
 "    meilleure.</strong> Redémarrer le dyno Heroku ramène le menu en quelques minutes,\n"
 "    mais la panne réapparaîtra dès que l'application s'endormira ou que les heures\n"
 "    gratuites seront épuisées. Déplacer le JSON du menu dans le dépôt GitHub Pages, en\n"
 "    fichier statique, supprime d'un même geste le backend, le 503 et la facture.</p>", 'note03_fr')

# ---------- 04 table ----------
sub(r'<p class="lede">La gravité, ici, c\'est un impact commercial.*?que la gravité\.</p>',
 "  <p class=\"lede\">La gravité, ici, désigne un impact commercial et non du théâtre\n"
 "  autour d'un score CVSS. Un e-mail falsifié primerait sur un menu mort"+NB+": le menu\n"
 "  vous coûte des ventes, tandis que l'e-mail peut coûter de l'argent à vos clients et\n"
 "  entame votre réputation autant que votre chiffre d'affaires. La section 07 précise\n"
 "  le calendrier de chaque correction"+NB+"; cette colonne-ci n'indique que la\n"
 "  gravité.</p>", 'lede04_fr')

# ---------- 05 subdomain ----------
sub(r'<p class="lede">C\'est le constat qui paraît alarmant.*?certificat serait valide\.</p>',
 "  <p class=\"lede\">C'est le constat le plus alarmant en apparence et le moins urgent\n"
 "  des trois. Il compte pour une raison précise"+NB+": l'adresse serait réelle, et le\n"
 "  certificat serait valide.</p>", 'lede05_fr')

sub(r'<li><span><b>Votre DNS pointe encore deux noms vers GitHub\.</b>.*?</span></li>',
 '<li><span><b>Votre DNS pointe encore deux noms vers GitHub.</b>\n'
 '    <span class="mono">mail.</span> et\n'
 '    <span class="mono">ftp.aftereightsousse.tn</span> résolvent tous deux vers\n'
 '    <span class="mono">185.199.108.153</span>, une adresse de GitHub Pages. Rien de ce\n'
 '    qui vous appartient n\'y est hébergé.</span></li>', 'step1_fr')

sub(r'<li><span><b>GitHub répond par sa propre page de remplacement\.</b>.*?</span></li>',
 '<li><span><b>GitHub répond par sa propre page de remplacement.</b> Demandez l\'un ou\n'
 '    l\'autre nom et vous obtenez\n'
 '    <span class="mono">Site not found · GitHub Pages</span>'+NB+', ce qui prouve que\n'
 '    GitHub écoute et qu\'aucun dépôt ne revendique ce nom.</span></li>', 'step2_fr')

sub(r'<li><span><b>La vérification de propriété n\'a jamais été faite\.</b>.*?</span></li>',
 '<li><span><b>La vérification de propriété n\'a jamais été effectuée.</b> GitHub ne\n'
 '    refuse d\'héberger la page d\'un inconnu sur votre domaine que si vous avez publié\n'
 '    un enregistrement TXT <span class="mono">_github-pages-challenge-</span> prouvant\n'
 '    que le domaine est le vôtre. Aucun enregistrement de ce type n\'existe dans votre\n'
 '    zone.</span></li>', 'step3_fr')

sub(r'<li><span><b>Un inconnu peut donc le revendiquer sans rien toucher chez vous\.</b>.*?</span></li>',
 '<li><span><b>Un inconnu peut donc le revendiquer sans rien modifier chez\n'
 '    vous.</b> Il fait pointer son propre dépôt sur\n'
 '    <span class="mono">mail.aftereightsousse.tn</span>'+NB+'; GitHub constate que le\n'
 '    DNS pointe déjà vers lui et commence à servir. Votre DNS n\'est jamais modifié. La\n'
 '    page apparaît en quelques minutes, sur votre domaine, derrière un certificat\n'
 '    <span class="mono">CN=*.github.io</span> que les navigateurs acceptent.</span></li>', 'step4_fr')

sub(r'<p style="margin:0"><strong>Ce que cela vaut, et ce que cela ne vaut pas\.</strong>.*?n\'a besoin de personne\.</p>',
 "    <p style=\"margin:0\"><strong>Ce que cela vaut, et ce que cela ne vaut pas.</strong>\n"
 "    Aucun mot de passe ni donnée client n'est exposé, car le site ne comporte pas de\n"
 "    connexion et ne dépose aucun cookie. L'enjeu, c'est votre nom"+NB+": un lien\n"
 "    auquel on accorde déjà une demi-confiance, annonçant que le menu a déménagé et\n"
 "    réclamant un numéro de carte. C'est pourquoi il passe après le menu mort. Il faut\n"
 "    que quelqu'un vous remarque"+NB+"; le menu, lui, n'a besoin de personne.</p>", 'note05_fr')

sub(r'<p class="lede" style="margin-top:var\(--s5\);margin-bottom:0">La correction\s*\n\s*consiste à supprimer les deux enregistrements DNS.*?d\'un coup\.</p>',
 "  <p class=\"lede\" style=\"margin-top:var(--s5);margin-bottom:0\">La correction\n"
 "  consiste à supprimer les deux enregistrements DNS, puisque rien ne réside à aucune\n"
 "  de ces deux adresses. S'ils redeviennent nécessaires, rajoutez-les en même temps que\n"
 "  l'enregistrement TXT de vérification, qui protège tous les sous-domaines d'un seul\n"
 "  coup.</p>", 'lede05b_fr')

# ---------- 06 minor ----------
sub(r'<p class="lede" style="margin-top:var\(--s5\)">Aucun de ces points ne livre vos\s*\n\s*données.*?sont publiques\.</p>',
 "  <p class=\"lede\" style=\"margin-top:var(--s5)\">Aucun de ces points ne livre vos\n"
 "  données à quiconque. Le fichier source est remarquable en sens inverse"+NB+": c'est\n"
 "  par lui que j'ai lu chaque fichier de cette page sans toucher à votre serveur. Le\n"
 "  compromis est raisonnable pour un site vitrine et fâcheux pour tout ce qui cache une\n"
 "  connexion derrière. Si vous le laissez en ligne, sachez que l'adresse du backend et\n"
 "  toute la logique de routage sont publiques.</p>", 'lede06_fr')

sub(r'<p style="margin:0"><strong>Le domaine nu, pour être complet\.</strong>.*?repartiront\.</p>',
 "    <p style=\"margin:0\"><strong>Le domaine nu, pour être complet.</strong>\n"
 "    <span class=\"mono\">https://aftereightsousse.tn</span> échoue au contrôle du\n"
 "    certificat, car seul <span class=\"mono\">www</span> en possède un qui corresponde.\n"
 "    En passant par <span class=\"mono\">http://</span>, tout fonctionne"+NB+": la\n"
 "    redirection mène à <span class=\"mono\">https://www.</span> et le site s'affiche.\n"
 "    Cela ne pénalise donc que le visiteur qui saisit le domaine nu et rencontre\n"
 "    d'abord une tentative https. Certains verront un avertissement et repartiront.</p>", 'note06_fr')

# ---------- 07 reco ----------
sub(r'<div class="row"><span class="k">6 · Puis, si l\'envie vous prend.*?</span><span class="v">quand vous voulez</span></div>',
 "<div class=\"row\"><span class=\"k\">6 · Au-delà des réparations"+NB+": le site tient\n"
 "      sur une page, sans possibilité de commander, et il a été conçu pour tenir une\n"
 "      après-midi. Si vous souhaitez un jour en discuter, j'en serais ravi.</span><span class=\"v\">quand vous voulez</span></div>", 'reco6_fr')

sub(r'<p class="lede" style="margin-top:var\(--s5\);margin-bottom:0">Les étapes 1 et 2\s*\n\s*demandent chacune moins d\'une heure.*?vous pouvez constater\.</p>',
 "  <p class=\"lede\" style=\"margin-top:var(--s5);margin-bottom:0\">Les étapes 1 et 2\n"
 "  demandent chacune moins d'une heure de travail, et aucune ne requiert de\n"
 "  développeur. L'étape 1 est la seule qui fasse évoluer un chiffre que vous pouvez\n"
 "  constater.</p>", 'lede07_fr')

sub(r'<p class="lede" style="margin-top:var\(--s4\);margin-bottom:0">Les cinq premières étapes.*?pas encore une salle\.</p>',
 "  <p class=\"lede\" style=\"margin-top:var(--s4);margin-bottom:0\">Les cinq premières\n"
 "  étapes réparent ce qui est cassé. La sixième n'est pas une réparation. Le site est\n"
 "  court, réduit à une page, sans réservation en ligne, et il a été construit pour tenir\n"
 "  une après-midi. Il remplit son rôle. C'est une porte d'entrée, pas encore une\n"
 "  salle.</p>", 'lede07b_fr')

# ---------- footer ----------
sub(r'<p style="margin:0 0 var\(--s3\)"><b>Comment ceci a été testé\.</b>.*?contre\s*\n\s*le site en ligne\.</p>',
 "  <p style=\"margin:0 0 var(--s3)\"><b>Comment ceci a été vérifié.</b> Revue passive\n"
 "  uniquement, le 26 octobre 2026 entre 00"+NB+":45 et 01"+NB+":05 (Africa/Tunis). Le\n"
 "  DNS a été interrogé directement"+NB+"; les réponses HTTP et les en-têtes ont été lus\n"
 "  avec curl"+NB+"; le code de l'application a été lu depuis le fichier source que le\n"
 "  site publie lui-même"+NB+"; la panne du menu a été observée dans un profil de\n"
 "  navigateur vierge. Aucune exploitation n'a été tentée, aucun identifiant n'a été\n"
 "  employé, et aucun test destructeur n'a été lancé contre le site en ligne.</p>", 'foot1_fr')

sub(r'<p style="margin:0 0 var\(--s3\)"><b>Ce que je n\'ai pas vérifié\.</b>.*?comme prouvé\.</p>',
 "  <p style=\"margin:0 0 var(--s3)\"><b>Ce que je n'ai pas vérifié.</b> Que la\n"
 "  revendication de sous-domaine décrite en section 05 réussirait réellement. Je ne\n"
 "  l'ai pas tentée, car la tenter revient à prendre le contrôle d'un contenu sur le\n"
 "  domaine d'autrui. Le raisonnement s'appuie sur le comportement documenté par GitHub\n"
 "  et sur le guide de l'OWASP consacré à la reprise de sous-domaine, non sur une\n"
 "  tentative réelle. À considérer comme bien étayé, non comme prouvé.</p>", 'foot2_fr')

open('index.html','w',encoding='utf-8').write(s)
print('FR rewritten; failures:', fails if fails else 'none')
