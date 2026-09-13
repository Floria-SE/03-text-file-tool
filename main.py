with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

lines = text.splitlines()

clean_lines = []

for line in lines:
    line = line.strip()
    if line != "":
        clean_lines.append(line)

new_text = ""

for i, line in enumerate(clean_lines):
    if new_text == "":
        new_text = f"{i+1}. {line}"
    else:    
        new_text = f"{new_text}\n{i+1}. {line}"

print(new_text)

with open("output.txt", "w", encoding="utf-8") as file_1:
    file_1.write(new_text)