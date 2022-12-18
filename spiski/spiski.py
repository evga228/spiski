from math import *
#1
#maad=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa","Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#indeks=""
#while type(indeks)!=int:
#    try:
#        indeks=int(input("Indeks: "))
#    except:
#        ValueError

    
   
#indeks_list=list(str(indeks))
#print(maad[int(indeks_list[0])-1])

##3
#besp=[1,4,3,2,58,65,756,8,53,876,8,45,354,73]
#g=len(besp)
#besp.sort()
#f=besp[-1]
#chislo=f/g
#print(chislo)
#besp[-1]=chislo
#print(besp)
##4
#spisok=[1,34,5,-37,88.2,-3,17,-228,1337]
#spisok.sort(key=abs)
#print(spisok)

#spisok2=[1,34,5,-37,88.2,-3,17,-228,1337]
#spisok2.sort(key=abs)
#spisok2.reverse()
#print(spisok2)

#6
glasnie=["a","e","i","o","u","y"]
nimi=""
while type(nimi)!=int:
    try:
        nimi=str(input("Sisesta oma nimi: "))
        print("Tere,", nimi.title())
        break
        
    except:
        ValueError



#nimi=input("Mis on sinu nimi???:")
#tahed=list(nimi)
#n=len(tahed)
#print(f"{n} tahed, {tahed}")
#print("Remove kasutamine")
#t=input("Sisesta taht, mis tahad kustutada: ")
#nt=tahed.count(t)
#print(nt)
#j=0
#if nt==0:
#    print(f"{t} ei ole sellist tahe")
#else:
#    for i in range(len(tahed)):
#        if tahed[i-j]==t:
#            tahed.pop(i-j)
#            j+=1
#t=input("Mis taht on vaja otsida???")
#print(f"Taht {t} seisab {tahed.index(t)+1 positsioonil")


    #for i in tahed:
    #    if i==t: tahed.remove(t)
    #print(f"Nuud {t} ei ole sellist tahe jaanud listis, {tahed}")
