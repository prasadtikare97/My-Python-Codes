    
def words_between(file_name):
        e_dict={}
        with open(file_name,'r') as file_read:
             for i in file_read: 
                word = i.strip()  
                e_dict[word] =True

        all_words=input("Type two words:").split()
        f_word,s_word=all_words[0], all_words[1]       
        keys = list(e_dict.keys())
        start =0
        end=len(keys)-1
        while start <=end:
            mid=(start + end )//2
            if keys[mid] < f_word:
                 start=mid+1
            elif keys[mid] > s_word:
                 end=mid-1
            else:
                 break
            
        count=0
        for read in keys[start:end+1]:
             if f_word < read < s_word:
                  count+=1
        print(f"There are {count} words between {f_word} and {s_word}")              
words_between("dict1.txt")