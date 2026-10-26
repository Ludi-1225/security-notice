# -*- coding: utf-8 -*-
import re
s = open('index.html', encoding='utf-8').read()
n = [0]
def sub(pat, new, flags=re.S):
    global s
    rx = re.compile(pat, flags)
    s2, k = rx.subn(new, s, count=1)
    assert k == 1, f'NO MATCH: {pat[:70]}'
    s = s2; n[0] += 1

# ============================ ENGLISH ============================
sub(r'<p class="lead">Your domain publishes no DMARC record.*?closed today\.</p>',
 'PLACEHOLDER_LEAD_EN')

open('index.html','w',encoding='utf-8').write(s)
print('probe ok')
