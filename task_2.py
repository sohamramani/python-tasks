while True:
        paragraph = str(input("Enter a paragraph : ")) 
        if len(paragraph) != 0 and not paragraph.isspace():
            update_or_delete = input("update or delete any word from the paragraph (u/d) : ")
            
            while True:
                if update_or_delete == "u" and len(paragraph) != 0 and not paragraph.isspace():
                    word = input("Enter the word to be updated : ")
                    new_word = input("Enter the new word : ")
                    
                    if word in paragraph:
                        upated_paragraph=paragraph.replace(word , new_word)
                        print("output : ", upated_paragraph)
                        break
                    else:
                        print("Word not found in the paragraph"+ "\n")
                    break
                
                elif update_or_delete == "d" and len(paragraph) != 0 and not paragraph.isspace():
                    del_word = input("Enter word you want to delete : ")
                    
                    if del_word in paragraph:
                        del_paragraph=paragraph.replace(del_word , "")
                        print("output : ", del_paragraph)
                        break
                    else:
                        print("Word not found in paragraph "+ "\n")
                    break
                
                else:
                    print("plese enter valid value"+ "\n")
                    break
        else:
            print("paragraph is empty"+ "\n")     

