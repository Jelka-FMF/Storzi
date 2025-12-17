import os

lucke = []
with open(os.environ["JELKA_POSITIONS"]) as f:
    for line in f.readlines():
        line = line.strip().split(",")
        lucke.append([int(line[0]), float(line[1]), float(line[2]), float(line[3])])

n = len(lucke)

print(f'#{{"version": 0, "led_count": {n}, "fps": 60}}')

state = ["000000"] * n
while True:
    state = ["000000"] * n
    print("#" + "".join(state), flush=True)
    for lucka in sorted(lucke, key=lambda x: x[1]):
        state[lucka[0]] = "ff0000"
        print("#" + "".join(state), flush=True)
    state = ["000000"] * n
    print("#" + "".join(state), flush=True)
    for lucka in sorted(lucke, key=lambda y: y[2]):
        state[lucka[0]] = "00ff00"
        print("#" + "".join(state), flush=True)
    state = ["000000"] * n
    print("#" + "".join(state), flush=True)
    for lucka in sorted(lucke, key=lambda z: z[3]):
        state[lucka[0]] = "0000ff"
        print("#" + "".join(state), flush=True)
