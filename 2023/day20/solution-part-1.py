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

for name, connected in modules.items():
    for con in connected:
        if con in types and types[con] == "&":
            states[con][name] = False


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
    l, h = 1, 0
    changed = [(to, "broadcasted", False) for to in modules["broadcaster"[1:]]]
    while changed:
        for _, _, sig in changed:
            l += not sig
            h += sig
        changed = step(changed)
    return l, h


l, h = 0, 0
for _ in range(1000):
    ll, hh = do_round()
    l += ll
    h += hh
print(l * h)
