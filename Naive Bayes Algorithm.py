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
    for doc in df['Doc']:
        for word in doc.split():
            t_words.append(word)
    unique_words=list(set(t_words))
    return len(t_words), len(unique_words)
def ART_CLASS():
    art_word=[]
    art_class=df.query("Class=='art'")
    for Doc in art_class['Doc']:
        for Word in Doc.split():
            art_word.append(Word)
    return len(art_word),set(art_word)
def COM_CLASS():
    com_word=[]
    com_class=df.query("Class=='com'")
    for DoC in com_class['Doc']:
        for Words in DoC.split():
            com_word.append(Words)
    return len(com_word)
def Sub_in_SciClass():
    sci_word=[]
    Bio=[]
    mat=[]
    eng=[]
    phy=[]
    chem=[]
    stat=[]
    comp=[]
    isl=[]
    env=[]
    eco=[]
    sci_class=df.query("Class=='sci'")
    for docs in sci_class['Doc']:
        for sub in docs.split():
            sci_word.append(sub)
            if sub=='bio':
                Bio.append(sub)
            elif sub=='math':
                mat.append(sub)
            elif sub=='eng':
                eng.append(sub)
            elif sub=='phy':
                phy.append(sub)
            elif sub=='chem':
                chem.append(sub)
            elif sub=='stat':
                stat.append(sub)
            elif sub=='comp':
                comp.append(sub)
            elif sub=='isl':
                isl.append(sub)
            elif sub=='env':
                env.append(sub)
            elif sub=='eco':
                eco.append(sub)
    Science=len(sci_word)
    Biology=len(Bio)
    Math=len(mat)
    English=len(eng)
    Physics=len(phy)
    Chemistry=len(chem)
    Statistic=len(stat)
    Islamiyat=len(isl)
    Environment=len(env)
    Economy=len(eco)
    return Science,Biology,Math,English,Physics,Chemistry,Statistic,Islamiyat,Environment,Economy
# def sub_in_ArtClass():

def main():
    a,b=Vocab()
    # d=ART_CLASS()
    # e=COM_CLASS()
    # print(a,b,c,d,e)
    Sub_in_SciClass()
    x,y=ART_CLASS()
    print(x,y)
if __name__=='__main__':
    main()