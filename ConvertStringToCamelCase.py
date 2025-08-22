def to_camel_case(text):
    if text == "":
        return ""
    
    text = text.replace("_", "-")
    parts = text.split("-")
    royce = []

    royce.append(parts[0])  

    for word in parts[1:]:
        newWord = word[0].upper() + word[1:]
        royce.append(newWord)

    return "".join(royce)