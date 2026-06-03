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
    Computer=len(comp)
    Environment=len(env)
    Economy=len(eco)
    return Science,Biology,Math,English,Physics,Chemistry,Statistic,Computer,Islamiyat,Environment,Economy
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
    return Arts,liter,psyco,ur,f_art,Art,islam,civics,pk,Eng,Geo,accoun,econ,history
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
def Conditional_prob_Sci():
    sci,bio,math,eng,phy,chem,stat,comp,isl,env,eco=sub_in_SciClass()
    prob_bio=float((bio+1)/sci)
    prob_math=float((math+1)/sci)
    prob_eng=float((eng+1)/sci)
    prob_phy=float((phy+1)/sci)
    prob_chem=float((chem+1)/sci)
    prob_stat=float((stat+1)/sci)
    prob_comp=float((comp+1)/sci)
    prob_isl=float((isl+1)/sci)
    prob_env=float((env+1)/sci)
    prob_eco=float((eco+1)/sci)
    Science=(prob_bio*prob_chem)*(prob_comp*prob_eco)*(prob_math*prob_eng)*(prob_env*prob_phy)*(prob_isl*prob_stat)
    return Science
def Conditional_prob_Art():
    arts,lit,psy,urdu,fine_art,art,isl,civ,pk,eng,geo,acc,eco,hist=sub_in_ArtClass()
    prob_lit=float((lit+1)/arts)
    prob_psy=float((psy+1)/arts)
    prob_urdu=float((urdu+1)/arts)
    prob_fine_art=float((fine_art+1)/arts)
    prob_art=float((art+1)/arts)
    prob_isl=float((isl+1)/arts)
    prob_civ=float((civ+1)/arts)
    prob_pk=float((pk+1)/arts)
    prob_eng=float((eng+1)/arts)
    prob_geo=float((geo+1)/arts)
    prob_acc=float((acc+1)/arts)
    prob_eco=float((eco+1)/arts)
    prob_hist=float((hist+1)/arts)
    Arts=(prob_acc*prob_art)*(prob_civ*prob_eco)*(prob_eng*prob_geo)*(prob_fine_art*prob_hist)*(prob_lit*prob_urdu)*(prob_psy*prob_isl)*prob_pk
    return Arts
def Conditional_prob_Commerce():
    Commerce,Stats,math,phy,acc,biz,law,eco=sub_in_ComClass()
    prob_Stats=float((Stats+1)/Commerce)
    prob_math=float((math+1)/Commerce)
    prob_phy=float((phy+1)/Commerce)
    prob_acc=float((acc+1)/Commerce)
    prob_biz=float((biz+1)/Commerce)
    prob_law=float((law+1)/Commerce)
    prob_eco=float((eco+1)/Commerce)
    Comm=(prob_math*prob_Stats)*(prob_phy*prob_acc)*(prob_biz*prob_law)*prob_eco
    return Comm
def main():
    Science=Conditional_prob_Sci()
    Art=Conditional_prob_Art()
    Commerce=Conditional_prob_Commerce()
    prior_sci,prior_art,prior_com=prior_probabilities()
    print(Science*prior_sci,Art*prior_art,Commerce*prior_com)
if __name__=='__main__':
    main()