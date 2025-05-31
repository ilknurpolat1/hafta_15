import threading

def coder(a, b, c, sayac):
    print(f'Coder ID: ({a}, {b}, {c}),{sayac}')

threads = []
sayac = 0

for a in range(3):
    for b in range(3):
        for c in range(3):
            sayac += 1
            t = threading.Thread(target=coder, args=(a, b, c, sayac))
            threads.append(t)
            t.start()

