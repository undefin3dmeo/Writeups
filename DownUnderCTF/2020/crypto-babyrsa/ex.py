from Crypto.Util.number import *

n = 19574201286059123715221634877085223155972629451020572575626246458715199192950082143183900970133840359007922584516900405154928253156404028820410452946729670930374022025730036806358075325420793866358986719444785030579682635785758091517397518826225327945861556948820837789390500920096562699893770094581497500786817915616026940285194220703907757879335069896978124429681515117633335502362832425521219599726902327020044791308869970455616185847823063474157292399830070541968662959133724209945293515201291844650765335146840662879479678554559446535460674863857818111377905454946004143554616401168150446865964806314366426743287
s = 3737620488571314497417090205346622993399153545806108327860889306394326129600175543006901543011761797780057015381834670602598536525041405700999041351402341132165944655025231947620944792759658373970849932332556577226700342906965939940429619291540238435218958655907376220308160747457826709661045146370045811481759205791264522144828795638865497066922857401596416747229446467493237762035398880278951440472613839314827303657990772981353235597563642315346949041540358444800649606802434227470946957679458305736479634459353072326033223392515898946323827442647800803732869832414039987483103532294736136051838693397106408367097
c = 7000985606009752754441861235720582603834733127613290649448336518379922443691108836896703766316713029530466877153379023499681743990770084864966350162010821232666205770785101148479008355351759336287346355856788865821108805833681682634789677829987433936120195058542722765744907964994170091794684838166789470509159170062184723590372521926736663314174035152108646055156814533872908850156061945944033275433799625360972646646526892622394837096683592886825828549172814967424419459087181683325453243145295797505798955661717556202215878246001989162198550055315405304235478244266317677075034414773911739900576226293775140327580
e = 0x10001

inv_s = pow(s, -1, n)
print(inv_s)

# pq = n 
# 557p - 127q = inv_s
# 1. Use sage math to find p, q
# 2. Use below algorithm
# https://github.com/DownUnderCTF/Challenges_2020_public/blob/master/crypto/babyrsa/exploit/writeup.md
# https://rkm0959.tistory.com/162

l = 2 ** 1023
r = 2 ** 1025
while l <= r:
    m = (l + r) // 2
    p = m 
    q = (557 * p - inv_s) // 127
    if p * q >= n:
        res = m
        r = m - 1
    else:
        l = m + 1

p = res 
q = n // p 
phi = (p - 1) * (q - 1) 
d = pow(e, -1, phi)
m = pow(c, d, n)

print(long_to_bytes(m).decode())
# DUCTF{e4sy_RSA_ch4ll_t0_g3t_st4rt3d}