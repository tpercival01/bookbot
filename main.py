def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
    
    total = len(file_contents.split())

    temp = {}
    vals = "abcdefghijklmnopqrstuvwxyz"
    for i in file_contents.split():
        for j in [*i]:
            a = j.lower()
            if a in [*vals]:
                if a in temp:
                    temp[a] += 1
                else:
                    temp[a] = 1
    temp = dict(sorted(temp.items(), key=lambda x:x[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total} words found in the document\n")
    for i in temp:
        print(f"The '{i}' character was found {temp[i]} times")
    
    print("--- End report ---")

main()