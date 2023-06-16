from cosas import *


def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)
    print("------Herencia alumno---")
    al1 = Alumno("Jose", 19, "2342342", "Ico")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("------Herencia Profe")
    profe1 = Profesor("Jesus", 30+16, 363565, "Ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("-------Herencia Ayudante profesor-------")
    ayudante = AyudanteProfesor("Adrian", 20, "25252", "Ico", 23223, "Ing. de software", 4)
    ayudante.dormir()
    ayudante.nombre ="Abraham"
    ayudante.area = "POO"

main()