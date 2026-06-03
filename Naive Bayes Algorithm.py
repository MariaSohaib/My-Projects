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
def sub_in_SciClass():
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
def sub_in_ArtClass():
    lit=[]
    psy=[]
    urdu=[]
    fine_art=[]
    art=[]
    isl=[]
    civ=[]
    pak_std=[]
    eng=[]
    geo=[]
    acc=[]
    eco=[]
    hist=[]
    art_word=[]
    art_class=df.query("Class=='art'")
    for Doc in art_class['Doc']:
        for sub in Doc.split():
            art_word.append(sub)
            if sub=='lit':
                lit.append(sub)
            elif sub=='psy':
                psy.append(sub)
            elif sub=='eng':
                eng.append(sub)
            elif sub=='urdu':
                urdu.append(sub)
            elif sub=='fine-art':
                fine_art.append(sub)
            elif sub=='civics':
                civ.append(sub)
            elif sub=='pak-std':
                pak_std.append(sub)
            elif sub=='isl':
                isl.append(sub)
            elif sub=='art':
                art.append(sub)
            elif sub=='geo':
                geo.append(sub)
            elif sub=='acc':
                acc.append(sub)
            elif sub=='eco':
                eco.append(sub)
            elif sub=='hist':
                hist.append(sub)
    Arts=len(art_word)
    liter=len(lit)
    psyco=len(psy)
    ur=len(urdu)
    f_art=len(fine_art)
    Art=len(art)
    islam=len(isl)
    civics=len(civ)
    pk=len(pak_std)
    Eng=len(eng)
    Geo=len(geo)
    accoun=len(acc)
    econ=len(eco)
    history=len(hist)
    return Arts,liter,psyco,ur,f_art,Art,islam,civics,pk,Eng,Geo,accoun,eco,history
def sub_in_ComClass():
    com_word=[]
    stats=[]
    math=[]
    phy=[]
    acc=[]
    biz=[]
    law=[]
    eco=[]
    com_class=df.query("Class=='com'")
    for docs in com_class['Doc']:
        for sub in docs.split():
            com_word.append(sub)
            if sub=='stats':
                stats.append(sub)
            elif sub=='math':
                math.append(sub)
            elif sub=='phy':
                phy.append(sub)
            elif sub=='acc':
                acc.append(sub)
            elif sub=='biz':
                biz.append(sub)
            elif sub=='law':
                law.append(sub)
            elif sub=='eco':
                eco.append(sub)
    Commerce=len(com_word)
    Stats=len(stats)
    Math=len(math)
    Phy=len(phy)
    Acc=len(acc)
    Biz=len(biz)
    Law=len(law)
    Eco=len(eco)
    return Commerce,Stats,Math,Phy,Acc,Biz,Law,Eco
def main():
    print("hello")
if __name__=='__main__':
    main()