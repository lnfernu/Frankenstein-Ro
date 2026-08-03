import re

with open("db/re/mob_db.yml", "r", encoding="utf-8") as f:
    lines = f.readlines()

result = []
inside_card = False

for i, line in enumerate(lines):
    # detecta item carta
    if "Item:" in line and "_Card" in line:
        inside_card = True

    # muda Rate somente se não for carta
    if "Rate:" in line and not inside_card:
        line = re.sub(r"Rate:\s*\d+", "Rate: 10000", line)

    result.append(line)

    # reseta depois do bloco
    if "StealProtected:" in line:
        inside_card = False

with open("db/re/mob_db_test.yml", "w", encoding="utf-8") as f:
    f.writelines(result)

