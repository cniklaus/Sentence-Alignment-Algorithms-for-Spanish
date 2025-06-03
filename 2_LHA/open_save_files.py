

i = 0
while i < 243:
    with open(f"Newsela/doc_level_files/docs0/{i}.txt", "r+") as file:
        text = file.read()
        #file.truncate(0)
        file.write(" ")
        file.close()
    i += 1