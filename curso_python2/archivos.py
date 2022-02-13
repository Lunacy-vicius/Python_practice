def read():
    archivos = []
    with open("./archivos/archivos.txt", "r", encoding="utf-8") as f:
        for line in f:
            archivos.append(int(line))
    print(archivos)

def write():
    names = ["Facundo", "Miguel", "Ricardo", "Gerardo", "Rocío"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()


if __name__ == "__main__":
    run()
