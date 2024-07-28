import PyPDF2   

# file_handle = open('Sense-and-Sensibility.pdf', 'rb') 
file_handle = open('/Users/maddyludes/Documents/GitHub/ROAR-Academy/samples/Sense-and-Sensibility.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(file_handle) 

frequency_table = dict()
for page_num in range(len(pdfReader.pages)):
    page_object = pdfReader.pages[page_num]
    page_text = page_object.extract_text()
    
    print('ttt')
    
    lines = page_text.lower()
    while '\n' in lines:
        if lines[lines.index('\n')-1] == '-':
            lines = lines.replace('\n', '', 1)
    lines = lines.replace('\n', ' ')
    words = ''.join(lines).split()

    # print(words)
    for word in words:
        if not word.isalpha():
            if word.isnumeric() or 'www' in word or 'pdf' in word:
                words.remove(word)
                continue
            if '--' in word:
                i = word.index('--')
                words.append(word[:i])
                words.append(word[i+2:])
                continue
            for char in word:
                if not char.isalnum() and not char=='-':
                    word = word[:word.index(char)] + word[word.index(char)+1:]
                    # print(word)

        if word not in frequency_table:
            frequency_table[word] = 1
        else:
            frequency_table[word] +=1
    print(frequency_table)
  
