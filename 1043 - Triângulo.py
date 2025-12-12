# -*- coding: utf-8 -*-
v = input().split()

a = float(v[0])
b = float(v[1])
c = float(v[2])

if a + b > c and a + c > b and c + b > a:
    print(f"Perimetro = {a + b + c:.1f}")
else:
    print(f"Area = {(((a + b) * c) / 2):.1f}")