class encuesta:
    #atributos
    def __init__(self,nombre,carrera,numIdeas,ideaProy):
        self.nombre=nombre
        self.carrera=carrera
        self.numIdeas=numIdeas
        self.ideaProy=ideaProy
    
    #metodos
    def respuestas(self):
        name=[]
        carreer=[]
        librery=[]
        proyectIdeas=[]
        for i in range(0,10):
            nombre=input("ingresa tu nombre\n")
            name.append(nombre)
            carrera=input("ingresa tu carrera\n")
            carreer.append(carrera)
            librerias=input("conoces librerias de python?(si si esscribe las que conozcas separadas por un espacio, sino escribe ninguno\n")
            librery.append(librerias)
            ideasProy=input("cual idea tienes para tu proyecto?\n")
            proyectIdeas.append(ideasProy)
            print(f"la persona {name[i]} de la carrera {carreer[i]} conoce {librery[i]} librerias de python para conseguir su proyecto de: {proyectIdeas[i]}")
        print(f"librerias para cada variable:\nnombres:{name}\ncarreras:{carreer}\nlibrerias:{librery}\nideas de proyecto:{proyectIdeas}")
def main():
    encuesta.respuestas(encuesta)

if __name__=="__main__":
    main()
