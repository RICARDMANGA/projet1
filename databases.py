"""# importing required libraries
import mysql.connector
 
connexion = mysql.connector.connect(
          user ="Paul",
          passwd ="Paul$123456",
          host ="localhost",                # Localhost for local connection
          dataBase ='Gestion'
        )

print(connexion)
 
# Disconnecting from the server
connexion.close()"""



def controle_saisie(nb):
    
 while True :
  try:
    nb=int(nb)
    return nb
  
  except ValueError:
    nb=input("Le chiffre que vous avez entre n/est pas valide. Veuillez essayer a nouveau : ")
  else:
    break

nombre1=input("Veuillez saisir un nombre : ")
nombre1=controle_saisie(nombre1)
print(nombre1)
nombre2=input("Veuillez saisir un autre nombre :"  )
nombre2=controle_saisie(nombre2)
print("La somme de {} et {} est {} ".format(nombre1,nombre2,nombre1+nombre2))