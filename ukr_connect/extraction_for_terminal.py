#!/usr/bin/env python
# coding: utf-8

# In[127]:


with open('uk_connectives_cleaned-connectives_cleaned.csv') as con:
    con=list(con)
    con=[e.replace('\n','').split(',')[:9] for e in con]
    con=[e for e in con if len(e)==9]
    connectives=[e[0] for e in con[1:]]
    english=[e[1] for e in con[1:]]
    cont_discont=[e[2] for e in con[1:]]
    single_phrasal=[e[3] for e in con[1:]]
    ortho_variant=[e[4] for e in con[1:]]
    syntax=[e[5] for e in con[1:]]
    sense1=[e[6] for e in con[1:]]
    sense2=[e[7] for e in con[1:]]
    sense3=[e[8] for e in con[1:]]
    two_parted=[e for e in connectives if '...' in e and e!='']
    one_parted=[e for e in connectives if '...'  not in e and e!='' and ' ' not in e]
    two_words=[e for e in connectives if '...'  not in e and e!='' and ' ' in e]
    two_parted=[e.split('...') for e in two_parted if 'не тільки' not in e.split('...')[0]]
    print(two_parted)
    print(one_parted)
    print(two_words)


# In[33]:


with open('texts.txt','r') as text:
    text=list(text)
    text=[e.replace('\n') for e in text]


# In[152]:


import re
tokenized=[]
for e in text:
    tokenized.append(re.split('[\s.»«!?,]', e))
tokenized=[[i for i in e if i!='']for e in tokenized]
matched=[]
for t in tokenized:
    for w in range(len(t)):
        if t[w].lower() in one_parted:
            print(t[w])
            print(t[w-2:])
            matched.append(t[w])
            


# In[149]:


for e in range (len(text)):
    for w in two_words:
        if w in text[e]:
            print(w)
            print(tokenized[e])
            print('--')
            for tok in range(len(tokenized[e])):
                if w.split(' ')[0]==tokenized[e][tok].lower() and w.split(' ')[1]==tokenized[e][tok+1].lower():
                    print(tokenized[e][tok-2:tok+4])
                    matched.append(tokenized[e][tok])
            print('\n')

#for the ne tilki a i exception
#!!add але/а й/і as variants
for e in range (len(text)):
    if 'не тільки' in text[e]:
        print(text[e])
        if ' але й ' in text[e] or ' a й ' or ' але і 'in text[e] or ' а і ' in text[e]:
            print('yes')
            for tok in range(len(tokenized[e])):
                if 'не'==tokenized[e][tok].lower() and 'тільки'==tokenized[e][tok+1].lower():
                    print(tokenized[e][tok-2:tok+8])
                    find=[i for i in range(len(tokenized[e][tok:]))if tokenized[e][tok:][i]=='а' or tokenized[e][tok:][i]=='але']
                    if find!=[]:
                        print(tokenized[e][tok:tok+2],tokenized[e][find[0]+tok:find[0]+tok+2])
                        matched.append([tokenized[e][tok:tok+2],tokenized[e][find[0]+tok:find[0]+tok+2]])
            


# In[150]:


#[['ані', 'ані'], ['ні', 'ні'], ['чим', 'тим'], ['або', 'або']]
done=[]
cpt=0
for e  in tokenized:
    for w in range(len(e)):
        find=[t for t in two_parted if t[0]==e[w]]
        if find!=[]:
            if find[0][1] in e[w:]:
                find2=[e[w:][i] for i in range(len(e[w:]))if e[w:][i]==find[0][1]]
                if find2!=[] and len(find2)>1:
                    cpt=0
                    for word in e[w:]:
                        if word in done:
                            cpt+=1
                    if cpt==len(e[w:]):
                        pass
                    else:
                        matched.append(find2)
                        print(find2)
                        print(e[w:])
                        for word in e[w:]:
                            done.append(word)
                    cpt+=0
                    
                    
        


# In[151]:


print(matched)


# In[ ]:




