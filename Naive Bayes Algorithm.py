import pandas as pd
df=pd.read_csv('doc.csv')
def prior():
    total=[]
    science=[]
    arts=[]
    commerce=[]
    for class1 in df['Class']:
        total.append(class1)
    for sci_class in total:
        if sci_class=='sci':
            science.append(sci_class)
    for art_class in total:
        if art_class=='art':
            arts.append(art_class)
    for com_class in total:
        if com_class=='com':
            commerce.append(com_class)
    total_count=len(total)
    count_science=len(science)
    count_arts=len(arts)
    count_commerce=len(commerce)
    return total_count, count_science, count_arts, count_commerce
def prior_probabilities():
    tot,Sci,Art,Com=prior()
    prob_science=float(Sci/tot)
    prob_art=float(Art/tot)
    prob_com=float(Com/tot)
    return prob_science, prob_art, prob_com
def Vocab():
    t_words=[]
    sci_word=[]
    for doc in df['Doc']:
        for word in doc.split():
            t_words.append(word)
    sci_class=df.query("Class=='sci'")
    for docs in sci_class['Doc']:
        for words in docs.split():
            sci_word.append(words)
    unique_words=list(set(t_words))
    print(len(t_words), len(unique_words), len(sci_word))
def main():
    sol1,sol2,sol3=prior_probabilities()
    # print(sol1,sol2,sol3)
    Vocab()
if __name__=='__main__':
    main()