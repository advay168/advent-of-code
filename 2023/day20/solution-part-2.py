from math import lcm

with open("./input.txt") as file:
    data = file.read().splitlines()

types = {}
modules = {}
states = {}
for module in data:
    t = module[0]
    name, connected = module[1:].split(" -> ")
    connected = connected.split(", ")
    match t:
        case "%":
            states[name] = False
        case "&":
            states[name] = {}
    types[name] = t
    modules[name] = connected

prime_conjs = []
for name, connected in modules.items():
    for con in connected:
        if con in types and types[con] == "&":
            states[con][name] = False
        if con == "rx":
            prime_conjs.append(name)


def step(changed):
    new_changed = []
    for module, src, signal in changed:
        match module in types and types[module]:
            case "%":
                if not signal:
                    states[module] = not states[module]
                    for conn in modules[module]:
                        new_changed.append((conn, module, states[module]))
            case "&":
                states[module][src] = signal
                sig = not all(states[module].values())
                for conn in modules[module]:
                    new_changed.append((conn, module, sig))
    return new_changed


def do_round():
    changed = [(to, "broadcasted", False) for to in modules["broadcaster"[1:]]]
    while changed:
        for name, fro, sig in changed:
            if name in prime_conjs and sig:
                if fro not in done[name]:
                    done[name][fro] = i
                if all(
                    done[prime_conj].keys() == states[prime_conj].keys()
                    for prime_conj in prime_conjs
                ):
                    return True
        changed = step(changed)
    return False


i = 1
done = {k: {} for k in prime_conjs}
while not do_round():
    i += 1
print(lcm(*(lcm(*completed.values()) for completed in done.values())))
