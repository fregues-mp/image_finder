import base

c = 0

while True:
    if not base.PN(r'data\1.png', 'teste', c):
        c += 1

    if base.EI('reset'):
        c = 0
        break
