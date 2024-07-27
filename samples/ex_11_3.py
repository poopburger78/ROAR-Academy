import PyPDF2      # haven't downloaded it yet

file_handle = open(‘Sense-and-Sensibility-by-Jane-Austen.pdf’, ‘rb’) 
pdfReader = PyPDF2.PdfReader(file_handle) 

frequency_table = dict()
for page_num in range(len(pdfReader.pages)):
    page_object = pdfReader.pages[page_num]
    page_text = page_object.extractText()



    stripped = page_text.split('\n').split()
    # strip numbers, chapter headers, puncuation, page numbers

    if (the word is alr there):
        frequency_table.add(word, 1)
    else:
        frequency_table[word] +=1
