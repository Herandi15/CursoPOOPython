class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"Nombre: {self.__nombre} Pseudónimo:{self.__pseudonimo}"

    def escribir(self):
        print(f" {self.__pseudonimo} esta escribiendo su sigueinte obra" )


class Libro:
    def __init__(self, titulo, autor, an, ed):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = an
        self.__editorial = ed

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, año):
        self.__año = año

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, editorial):
        self.__editorial = editorial

    def __str__(self):
        return f"""
        Titulo= {self.__titulo} 
        Autor= {self.__autor} 
        Año= {self.__año} 
        Editorial= {self.__editorial}
        """

    @classmethod
    def libro_planeta(cls,titulo,autor,año):
        return cls(titulo, autor,año,"Planeta")

    def leer(self, minutos):
        print(f"Leyendo {minutos} minutos")


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom


class Alumno(Persona):
    def __init__(self, nombre, edad, numero_cuenta, carrera, promedio):
        super().__init__(nombre,edad)
        self.__numero_cuenta = numero_cuenta
        self.__carrera = carrera
        self.__promedio = promedio
