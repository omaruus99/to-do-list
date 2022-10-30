import sys

ma_liste = []
ajout = ""
retirer = ""
choix = ""
while choix != 5 : 
    
    choix = input("Choisissez parmi les 5 options suivantes : \n 1 : Ajouter un élément à la liste \n 2 : Retirer un élément de la liste \n 3 : Afficher la liste \n 4 : Vider la liste \n 5 : Quitter \n 👉 Votre choix : ")

    if choix == "1" : 
        ajout = input("Entrer le nom d'un élement que vous voulez ajouter à la liste : ")
        ma_liste.append(ajout)
        print("L'element", ajout,"à bien été ajouter à la liste : ")
    elif choix == "2" : 
        retirer = input("Entrer le nom d'un élement que vous voulez retirer de la liste : ")
        if retirer in ma_liste : 
            ma_liste.remove(retirer)
            print("L'élement", retirer ,"a bien été retirer de la liste")
        else : 
            print("L'element ne figure pas dans la liste")    
    elif choix == "3" : 
        print(ma_liste)
    elif choix == "4" : 
        ma_liste.clear()  
    elif choix == "5" : 
        print("A bientot !")
        sys.exit()  