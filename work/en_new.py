# -*- coding: utf-8 -*-
import re, sys
s = open('index.html', encoding='utf-8').read()
fails = []
def sub(pat, new, tag):
    global s
    rx = re.compile(pat, re.S)
    s2, k = rx.subn(lambda m: new, s, count=1)
    if k != 1:
        fails.append(tag)
        return
    s = s2

# ---------- hero ----------
sub(r'<h1>Anyone can send emails to your customers pretending to be you</h1>',
    '<h1>Anyone can email your customers and pose as you</h1>', 'h1')

sub(r'<p class="lead">Your domain publishes no DMARC record.*?closed today\.</p>',
 '      <p class="lead">Your domain publishes no DMARC record, and its SPF policy\n'
 '      ends in a soft fail. A stranger can therefore send email to your customers\n'
 '      that appears to come from your reservations address: a deposit request, a\n'
 '      table confirmation, a link. Nothing alerts you when it happens. The second\n'
 '      finding, a menu page that never loads, is easier to see but easier to fix.\n'
 '      Both can be resolved today.</p>', 'lead')

sub(r'<p class="kicker">Security and availability review · aftereightsousse\.tn · 26 October 2026</p>',
 '<p class="kicker">Security and availability review · aftereightsousse.tn · 26 October 2026</p>', 'kicker')

# ---------- 01 DMARC ----------
sub(r'<p class="lede">Your domain\'s SPF record ends in <span class="mono">~all</span>.*?Together they are an invitation\.</p>',
 '  <p class="lede">Two DNS records determine whether a message from your domain is\n'
 '  authentic: SPF and DMARC. The first is published but permissive; the second is\n'
 '  absent. Neither prevents forgery on its own, and together they constitute an\n'
 '  invitation.</p>', 'lede01')

sub(r'<p style="color:var\(--ink-2\);font-size:16px;margin:0">A message arriving\s*\n\s*from <span class="mono">reservations@aftereightsousse\.tn</span>.*?telling you it happened\.</p>',
 '        <p style="color:var(--ink-2);font-size:16px;margin:0">An email arrives\n'
 '        from <span class="mono">reservations@aftereightsousse.tn</span>. It reaches\n'
 '        the inbox, survives a first glance, and asks a customer to confirm a booking\n'
 '        by paying a deposit into an account that is not yours. Without DMARC, the\n'
 '        receiving server has no instruction to reject or quarantine it, and no report\n'
 '        reaches you afterwards.</p>', 'panel01')

sub(r'<p class="lede" style="margin-top:var\(--s5\);margin-bottom:0">A one-line DMARC\s*\n\s*record in monitor mode.*?two to four weeks\.</p>',
 '  <p class="lede" style="margin-top:var(--s5);margin-bottom:0">A single-line DMARC\n'
 '  record in monitor mode costs nothing and cannot break your mail, because at\n'
 '  <span class="mono">p=none</span> it instructs no server to block anything. It\n'
 '  simply starts sending you reports. Move to\n'
 '  <span class="mono">p=quarantine</span> once those reports come back clean,\n'
 '  typically after two to four weeks.</p>', 'lede01b')

# ---------- 02 menu ----------
sub(r'<p style="font:400 1\.3rem/1\.35 var\(--serif\);margin:0 0 var\(--s3\)">Every dish,\s*\n\s*every price, unreachable\. The page is not broken — it is waiting\.</p>',
 '      <p style="font:400 1.3rem/1.35 var(--serif);margin:0 0 var(--s3)">Every dish,\n'
 '      every price, unreachable. The page is not broken. It is waiting.</p>', 'menu_lead')

sub(r'<p style="color:var\(--ink-2\);font-size:16px;margin:0">The site is a React\s*\n\s*app\. It loads a single JSON file from a Heroku app.*?The spinner\s*\n\s*stays\.</p>',
 '        <p style="color:var(--ink-2);font-size:16px;margin:0">The site is a React\n'
 '        application. It loads one JSON file from a Heroku app and draws the menu only\n'
 '        once that file arrives. The Heroku app answers <span class="mono">503</span>,\n'
 '        so the request fails, and the code that draws the menu has no error branch.\n'
 '        The spinner remains.</p>', 'menu_panel')

sub(r'<figcaption><b>What works\.</b> <span class="mono">/</span> — the landing\s*\n\s*route.*?check the site\.</figcaption>',
 '      <figcaption><b>What works.</b> <span class="mono">/</span>, the landing route,\n'
 '      which needs no data. Photograph, heading, two buttons. This is what the owner\n'
 '      sees when checking the site.</figcaption>', 'fig1')

sub(r'<figcaption><b>What does not\.</b> <span class="mono">/#/menu</span> — the\s*\n\s*route one click to the right\..*?Nothing else ever renders\.</figcaption>',
 '      <figcaption><b>What does not.</b> <span class="mono">/#/menu</span>, the route\n'
 '      one click further in. The green mark is the loading spinner\n'
 '      <span class="mono">loader.89ba5735….png</span>, still turning after six\n'
 '      seconds. Nothing else renders.</figcaption>', 'fig2')

sub(r'<p class="src">Both captured 26 October 2026, 01:00 Africa/Tunis, in a clean\s*\n\s*browser profile at 1240×800, six seconds after load\. The menu capture is\s*\n\s*unedited apart from cropping the empty margins\.</p>',
 '  <p class="src">Both captured on 26 October 2026 at 01:00 Africa/Tunis, in a clean\n'
 '  browser profile at 1240×800, six seconds after load. The menu capture is unedited\n'
 '  apart from a crop of the empty margins.</p>', 'src')

sub(r'<p style="margin:0"><strong>The landing page is fine\.</strong> It is a separate\s*\n\s*route with no data dependency\. That is also why the failure is easy to miss.*?door, and it sits one click behind it\.</p>',
 '    <p style="margin:0"><strong>The landing page is unaffected.</strong> It is a\n'
 '    separate route with no data dependency, which is precisely why the fault is easy\n'
 '    to overlook. The site looks healthy from the front door, and the failure waits one\n'
 '    click behind it.</p>', 'note_menu')

# ---------- 03 diagram ----------
sub(r'<p class="lede">Four steps succeed and the fifth has nowhere to go\. The missing\s*\n\s*arrow is the whole bug\. Compare the two paths out of the backend call\.</p>',
 '  <p class="lede">Four steps succeed and the fifth has nowhere to go. The absent\n'
 '  arrow is the entire defect. Compare the two possible outcomes of the backend\n'
 '  call.</p>', 'lede03')

sub(r'<figcaption><b>The failure branch, and the branch that never existed\.</b>\s*\n\s*<span class="mono">Home\.js</span> renders the spinner when its <span class="mono">data</span>\s*\n\s*state is still <span class="mono">null</span>.*?Read from the published source map, 26 Oct 2026\.</figcaption>',
 '    <figcaption><b>The failure branch, and the branch that was never written.</b>\n'
 '    <span class="mono">Home.js</span> renders the spinner while its\n'
 '    <span class="mono">data</span> state is still <span class="mono">null</span>, and\n'
 '    only a resolved promise ever sets it. Because <span class="mono">App.js</span>\n'
 '    chains <span class="mono">.then()</span> with no\n'
 '    <span class="mono">.catch()</span>, a 503 leaves the state untouched rather than\n'
 '    raising anything visible. Read from the published source map, 26 October\n'
 '    2026.</figcaption>', 'fig03')

sub(r'<p style="margin:0"><strong>Two ways out, and the cheap one is better\.</strong>\s*\n\s*Restart the Heroku dyno.*?503, and the bill at once\.</p>',
 '    <p style="margin:0"><strong>Two ways out, and the cheaper one is better.</strong>\n'
 '    Restarting the Heroku dyno brings the menu back within minutes, but the failure\n'
 '    returns the moment the app sleeps or the free hours are exhausted. Moving the menu\n'
 '    JSON into the GitHub Pages repository as a static file removes the backend, the\n'
 '    503 and the bill in one move.</p>', 'note03')

# ---------- 04 table ----------
sub(r'<p class="lede">Severity here is business impact, not CVSS theatre.*?this column is severity\s*\n\s*only\.</p>',
 '  <p class="lede">Severity here means business impact, not CVSS theatre. A forged\n'
 '  email outranks a dead menu page: the menu costs you sales, whereas the email can\n'
 '  cost your customers money, and it damages your reputation as well as your takings.\n'
 '  Section 07 carries the schedule for each fix; this column records severity\n'
 '  alone.</p>', 'lede04')

# ---------- 05 subdomain ----------
sub(r'<p class="lede">This is the finding that looks alarming and is the least urgent\s*\n\s*of the three\. It matters for one specific reason: the address would be real, and\s*\n\s*the certificate would be valid\.</p>',
 '  <p class="lede">This finding looks the most alarming and is the least urgent of the\n'
 '  three. It matters for one specific reason: the address would be real, and the\n'
 '  certificate would be valid.</p>', 'lede05')

sub(r'<li><span><b>Your DNS still points two names at GitHub\.</b>.*?</span></li>',
 '<li><span><b>Your DNS still points two names at GitHub.</b> <span class="mono">mail.</span>\n'
 '    and <span class="mono">ftp.aftereightsousse.tn</span> both resolve to\n'
 '    <span class="mono">185.199.108.153</span>, a GitHub Pages address. Nothing of\n'
 '    yours is hosted there.</span></li>', 'step1')

sub(r'<li><span><b>GitHub answers with its own placeholder\.</b>.*?</span></li>',
 '<li><span><b>GitHub answers with its own placeholder.</b> Request either name and you\n'
 '    get <span class="mono">Site not found · GitHub Pages</span>, which proves GitHub is\n'
 '    listening and that no repository claims the name.</span></li>', 'step2')

sub(r'<li><span><b>The ownership check was never done\.</b>.*?</span></li>',
 '<li><span><b>The ownership check was never performed.</b> GitHub refuses to host a\n'
 '    stranger\'s page on your domain only if you have published a\n'
 '    <span class="mono">_github-pages-challenge-</span> TXT record proving the domain is\n'
 '    yours. No such record exists in your zone.</span></li>', 'step3')

sub(r'<li><span><b>So a stranger can claim it without touching anything of yours\.</b>.*?</span></li>',
 '<li><span><b>A stranger can therefore claim it without touching anything of\n'
 '    yours.</b> They point their own repository at\n'
 '    <span class="mono">mail.aftereightsousse.tn</span>; GitHub sees that DNS already\n'
 '    points at it and begins serving. Your DNS is never modified. The page appears\n'
 '    within minutes, on your domain, behind a\n'
 '    <span class="mono">CN=*.github.io</span> certificate that browsers accept.</span></li>', 'step4')

sub(r'<p style="margin:0"><strong>What it is worth, and what it is not\.</strong>.*?to notice anything\.</p>',
 '    <p style="margin:0"><strong>What it is worth, and what it is not.</strong> No\n'
 '    password and no customer data are exposed, because the site has no login and sets\n'
 '    no cookies. The prize is your name: a link people already half-trust, announcing\n'
 '    that the menu has moved and asking for a card number. That is why it ranks below\n'
 '    the dead menu. It needs someone to notice you; the menu needs nobody to notice\n'
 '    anything.</p>', 'note05')

sub(r'<p class="lede" style="margin-top:var\(--s5\);margin-bottom:0">The fix is to\s*\n\s*delete both DNS records.*?protects every subdomain at once\.</p>',
 '  <p class="lede" style="margin-top:var(--s5);margin-bottom:0">The fix is to delete\n'
 '  both DNS records, since nothing lives at either address. If they are needed later,\n'
 '  re-add them together with the verification TXT record, which protects every\n'
 '  subdomain at once.</p>', 'lede05b')

# ---------- 06 minor ----------
sub(r'<p class="lede" style="margin-top:var\(--s5\)">None of these hands anyone your\s*\n\s*data\. The source map is the notable one in the other direction.*?routing logic are\s*\n\s*public\.</p>',
 '  <p class="lede" style="margin-top:var(--s5)">None of these hands anyone your data.\n'
 '  The source map is notable in the other direction: it is how I read every file on\n'
 '  this page without touching your server. That is a fair trade for a brochure site and\n'
 '  a poor habit for anything with a login behind it. If you leave it published, be\n'
 '  aware that the backend URL and the full routing logic are public.</p>', 'lede06')

sub(r'<p style="margin:0"><strong>The bare domain, for completeness\.</strong>.*?see a warning and leave\.</p>',
 '    <p style="margin:0"><strong>The bare domain, for completeness.</strong>\n'
 '    <span class="mono">https://aftereightsousse.tn</span> fails its certificate check,\n'
 '    because only <span class="mono">www</span> has a matching one. Visiting\n'
 '    <span class="mono">http://</span> works: it redirects to\n'
 '    <span class="mono">https://www.</span> and the site loads. So this affects only the\n'
 '    visitor who types the bare domain and meets an https attempt first. Some will see\n'
 '    a warning and leave.</p>', 'note06')

# ---------- 07 reco ----------
sub(r'<div class="row"><span class="k">6 · Then, if the mood takes you:.*?</span><span class="v">whenever</span></div>',
 '<div class="row"><span class="k">6 · Beyond the repairs: the site is a single page\n'
 '      with no way to order, and it was built to last an afternoon. If you ever want to\n'
 '      discuss what it could become, I would be glad to.</span><span class="v">whenever</span></div>', 'reco6')

sub(r'<p class="lede" style="margin-top:var\(--s5\);margin-bottom:0">Steps 1 and 2 are\s*\n\s*both under an hour of work and neither needs a developer\. Step 1 is the only one\s*\n\s*that changes a number you can see\.</p>',
 '  <p class="lede" style="margin-top:var(--s5);margin-bottom:0">Steps 1 and 2 each take\n'
 '  under an hour of work, and neither requires a developer. Step 1 is the only one that\n'
 '  changes a number you can observe.</p>', 'lede07')

sub(r'<p class="lede" style="margin-top:var\(--s4\);margin-bottom:0">The first five steps\s*\n\s*repair what is broken\. The sixth is not a repair:.*?It is a front\s*\n\s*door, not yet a room\.</p>',
 '  <p class="lede" style="margin-top:var(--s4);margin-bottom:0">The first five steps\n'
 '  repair what is broken. The sixth is not a repair. The site is short, a single page,\n'
 '  with no way to reserve online, and it was built to hold together for an afternoon. It\n'
 '  does its job. It is a front door, not yet a room.</p>', 'lede07b')

# ---------- footer ----------
sub(r'<p style="margin:0 0 var\(--s3\)"><b>How this was tested\.</b> Passive review only,\s*\n\s*on 26 October 2026 between 00:45 and 01:05 Africa/Tunis\..*?run against the live site\.</p>',
 '  <p style="margin:0 0 var(--s3)"><b>How this was tested.</b> Passive review only, on\n'
 '  26 October 2026 between 00:45 and 01:05 Africa/Tunis. DNS was queried directly; HTTP\n'
 '  responses and headers were read with curl; the application source was read from the\n'
 '  site\'s own published source map; the menu failure was observed in a clean browser\n'
 '  profile. No exploitation was attempted, no credentials were used, and no destructive\n'
 '  test was run against the live site.</p>', 'foot1')

sub(r'<p style="margin:0 0 var\(--s3\)"><b>What I did not verify\.</b>.*?not proven\.</p>',
 '  <p style="margin:0 0 var(--s3)"><b>What I did not verify.</b> That the subdomain\n'
 '  claim described in section 05 would actually succeed. I did not attempt it, because\n'
 '  attempting it means taking control of content on someone else\'s domain. The\n'
 '  reasoning rests on GitHub\'s documented behaviour and on the OWASP subdomain-takeover\n'
 '  guide, not on a live attempt. Treat it as well evidenced rather than proven.</p>', 'foot2')

open('index.html','w',encoding='utf-8').write(s)
print('EN rewritten; failures:', fails if fails else 'none')
