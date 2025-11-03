def autorisation_rentrer(code: int):
    if code == 1234:
        print('Vous pouvez rentrer')
    else:
        print('Le code est incorrect. Reessayez !')

code_utilisateur = int(input("Entrez votre code : "))

autorisation_rentrer(code_utilisateur)


