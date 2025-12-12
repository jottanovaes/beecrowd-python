# -*- coding: utf-8 -*-

values = []

for x in range(6):
    value = float(input())
    if value > 0:
        values.append(value)

avg = sum(values) / len(values)

print(f"{len(values)} valores positivos")
print(f"{avg:.1f}")