def main():
    book_path = "books/frankenstein.txt"
    report_list = []

    with open(book_path) as f:
        file_contents = f.read()

    char_dictionnary = count_char(file_contents)

    print(f'--- Begin report of {book_path} ---')
    print(count_words(file_contents), 'words found in the document \n')

    for key, value in char_dictionnary.items():
        report_list.append({'name': key, 'num': value})

    report_list.sort(reverse=True, key=sort_on)

    for i in report_list:
        if i['name'].isalpha():
            print(f'The {i['name']} character was found {i['num']} times')
    print('--- End of report ---')
    

def sort_on(dict):
    return dict['num']

def count_words(file_contents):
    words = file_contents.split()
    return len(words)
    
def count_char(text):
    char_dictionnary = {}
    text = text.lower()
    for char in text:
        if char not in char_dictionnary:
            char_dictionnary.update({char: 1})
        else:
            count = char_dictionnary[char]
            count += 1
            char_dictionnary.update({char: count})
    return char_dictionnary

main()