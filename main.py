# main.py
import json
from pathlib import Path

DATAFILE = Path("data/tasks.json")
DATAFILE.parent.mkdir(exist_ok=True)

def load():
    if not DATAFILE.exists(): return []
    return json.loads(DATAFILE.read_text())

def save(tasks):
    DATAFILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2))

def main():
    tasks = load()
    while True:
        cmd = input("Команда (add/list/remove/exit): ").strip()
        if cmd == "add":
            text = input("Текст задачи: ")
            tasks.append({"text": text})
            save(tasks)
            print("Добавлено")
        elif cmd == "list":
            for i,t in enumerate(tasks,1):
                print(i, t["text"])
        elif cmd == "remove":
            n = int(input("Номер: ")) - 1
            if 0 <= n < len(tasks):
                tasks.pop(n)
                save(tasks)
                print("Удалено")
        elif cmd == "exit":
            break

if __name__ == "__main__":
    main()
