import pandas as pd
df=pd.read_csv('doc.csv')
def prior():
    all_sub=df['Class'].tolist()
    num={
        'sci':0,
        'art':0,
        'com':0
    }
    for sub in all_sub:
        if sub in num:
            num[sub]+=1
    total_count=len(all_sub)
    Science=num['sci']
    Art=num['art']
    Commerce=num['com']
    return total_count, Science, Art, Commerce
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
    Science=0
    subj=['bio','math','eng','phy','chem','stat','isl','comp','env','eco']
    num={
        'bio':0,
        'math':0,
        'eng':0,
        'phy':0,
        'chem':0,
        'stat':0,
        'isl':0,
        'comp':0,
        'env':0,
        'eco':0
    }
    sci_class=df.query("Class=='sci'")
    for docs in sci_class['Doc']:
        for word in docs.split():
            Science+=1
            for sub in subj:
                if word==sub:
                    num[sub]+=1
    Biology=num['bio']
    Math=num['math']
    English=num['eng']
    Physics=num['phy']
    Chemistry=num['chem']
    Statistic=num['stat']
    Islamiyat=num['isl']
    Computer=num['comp']
    Environment=num['env']
    Economy=num['eco']
    return Science,Biology,Math,English,Physics,Chemistry,Statistic,Computer,Islamiyat,Environment,Economy
def sub_in_ArtClass():
    Arts=0
    subj=['lit','psy','urdu','fine-art','isl','civics','art','pak-std','eng','geo','acc','eco','hist']
    num={
        'lit':0,
        'psy':0,
        'urdu':0,
        'fine-art':0,
        'isl':0,
        'civics':0,
        'art':0,
        'pak-std':0,
        'eng':0,
        'geo':0,
        'acc':0,
        'eco':0,
        'hist':0
    }
    art_class=df.query("Class=='art'")
    for Doc in art_class['Doc']:
        for word in Doc.split():
            Arts+=1
            for sub in subj:
                if word==sub:
                    num[sub]+=1
    liter=num['lit']
    psyco=num['psy']
    ur=num['urdu']
    f_art=num['fine-art']
    Art=num['art']
    islam=num['isl']
    civics=num['civics']
    pak=num['pak-std']
    Eng=num['eng']
    Geo=num['geo']
    accoun=num['acc']
    econ=num['eco']
    history=num['hist']
    return Arts,liter,psyco,ur,f_art,Art,islam,civics,pak,Eng,Geo,accoun,econ,history
def sub_in_ComClass():
    Commerce=0
    subj=['stats','math','phy','acc','law','biz','eco']
    num={
        'stats':0,
        'math':0,
        'phy':0,
        'acc':0,
        'law':0,
        'biz':0,
        'eco':0
    }
    com_class=df.query("Class=='com'")
    for docs in com_class['Doc']:
        for word in docs.split():
            Commerce+=1
            for sub in subj:
                if word==sub:
                    num[sub]+=1
    Stats=num['stats']
    Math=num['math']
    Phy=num['phy']
    Acc=num['acc']
    Biz=num['biz']
    Law=num['law']
    Eco=num['eco']
    return Commerce,Stats,Math,Phy,Acc,Biz,Law,Eco
def Conditional_prob_Sci():
    sci,bio,math,eng,phy,chem,stat,comp,isl,env,eco=sub_in_SciClass()
    sub=[bio,math,eng,phy,chem,stat,comp,isl,env,eco]
    t_prob=[]
    for pro in sub:
        prob=float((pro+1)/sci)
        t_prob.append(prob)
    Science=1
    for prob in t_prob:
        Science*=prob
    return Science
def Conditional_prob_Art():
    arts,lit,psy,urdu,fine_art,art,isl,civ,pk,eng,geo,acc,eco,hist=sub_in_ArtClass()
    sub=[lit,psy,urdu,fine_art,art,isl,civ,pk,eng,geo,acc,eco,hist]
    t_prob=[]
    for pro in sub:
        prob=float((pro+1)/arts)
        t_prob.append(prob)
    Arts=1
    for prob in t_prob:
        Arts*=prob
    return Arts
def Conditional_prob_Commerce():
    Commerce,Stats,math,phy,acc,biz,law,eco=sub_in_ComClass()
    sub=[Stats,math,phy,acc,biz,law,eco]
    t_prob=[]
    for pro in sub:
        prob=float((pro+1)/Commerce)
        t_prob.append(prob)
    Comm=1
    for prob in t_prob:
        Comm*=prob
    return Comm
def main():
    x,y,z,a=prior()
    print(x,y,z,a)
if __name__=='__main__':
    main()