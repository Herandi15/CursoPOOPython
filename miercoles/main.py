from cosas import Alumno
from cosas import Perro
def main():
    al1=Alumno("jose",19,"ICO")
    print(vars(al1))
    al1.__nombre ="Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("------To string")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)

    print("----PERRO-----")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza="De la calle"
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43
    print(vars(perro1))
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)
main()