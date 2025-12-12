# -*- coding: utf-8 -*-

v = input().split()

h0 = int(v[0])
m0 = int(v[1])
h1 = int(v[2])
m1 = int(v[3])

start = m0 + (h0 * 60)
end = m1 + (h1 * 60)

elapsed_time = end - start

if end <= start:
    elapsed_time += 24 * 60

h_total = elapsed_time // 60
m_total = elapsed_time % 60

print(f"O JOGO DUROU {h_total} HORA(S) E {m_total} MINUTO(S)")