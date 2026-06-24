def get_book_text(filepath: str):
    with open(filepath) as file:
        content = file.read()
        return content
def get_word_list(content: str) -> list:
    str_list = content.split()
    return str_list
def get_dict(contents: str) -> dict[str,int]:
    contents=contents.lower()
    diction = {}
    for char in contents:
        diction[char]=0
    for char in contents:
        diction[char]+=1
    return diction
def sort_on(cont: tuple[str,int]) -> int:
    return cont[1]
def chars_dict_to_sorted_list(diction: dict[str,int]) -> list[tuple[str,int]]:
    new_list=[]
    for key in diction:
        new_list.append((key,diction[key]))
    new_list=sorted(new_list,reverse=True,key=sort_on)
    return new_list
