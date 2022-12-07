with open("./input.txt") as file:
    data = file.read().splitlines()


class Directory:
    sizes = []

    def __init__(self, parent):
        self.files = {}
        self.dirs = {}
        self.parent = parent

    def cd_dir(self, name):
        if name not in self.dirs:
            self.dirs[name] = Directory(self)
        return self.dirs[name]

    def calc_size(self):
        size = 0
        for folder in self.dirs.values():
            size += folder.calc_size()
        for file in self.files.values():
            size += file
        Directory.sizes.append(size)
        return size


root = Directory(None)
current = root
for line in data:
    if line.startswith("$ cd "):
        new_dir = line[5:]
        if new_dir == "..":
            if current.parent is not None:
                current = current.parent
        elif new_dir == "/":
            current = root
        else:
            current = current.cd_dir(new_dir)
    elif line.startswith("$ ls") or line.startswith("dir"):
        continue
    else:
        size, file_name = line.split()
        current.files[file_name] = int(size)

root.calc_size()
print(sum(s for s in Directory.sizes if s < 100000))
