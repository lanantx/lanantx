cms=int(input("Ingresa tu cantidad de centimertros"))
if cms > 0:
 pulgadas=cms/2.54
 metros=cms*100
 mili=cms*10
 print(f"{cms^5}cms equivalen a {pulgadas:^5}pulgadas")
 print(f"{cms^5}cms equivalen a {metros:^5}metros")
 print(f"{cms^5}cms equivalen a {mili:^5}milimetros")
 
 
else:
    print("error")
