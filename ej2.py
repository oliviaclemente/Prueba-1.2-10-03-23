class datoPolinomio(object):
    def _init_(self,valor,termino):
        self.valor= valor
        self.termino= termino

class Polinomio(object):
    def _init_(self):
        self.termino_mayor= None
        self.grado= -1
        
def agregar_termino(polinomio, termino, valor):
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    if(termino > polinomio.grado):
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        while(actual.sig is not None and termino < actual.sig.info.termino):
            actual = actual.sig 
        aux.sig = actual.sig
        actual.sig = aux
    print("El polinomio es: ")
    mostrar_polinomio(polinomio)
def modificar_termino(polinomio, termino, valor):
    log.debug("El polinomio es: %s", polinomio)
    aux= polinomio.termino_mayor
    while(aux is not None and aux.info.termino != termino):
        log.debug("No es el termino buscado")
        aux= aux.sig
    log.debug("Encontre el termino buscado")
    aux.info.valor= valor
    
def obtener_valor(polinomio,termino):
    aux= polinomio.termino_mayor 
    while(aux is not None and aux.info.termino > termino):
        aux= aux.sig
    if(aux is not None and aux.info.termino == termino):
        return aux.info.valor
    else:
        return 0
    
def mostrar(polinomio):
    aux= polinomio.termino_mayor 
    pol= ''
    if(aux is not None):
        while(aux is not None):
            signo= ''
            if(aux.info.valos >= 0):
                signo += '+'
            pol += signo + str(aux.info.vaolr) + "x^" + str(aux.info.termino)
            aux= aux.sig 
    return pol
def sumar(polinomio1,polinomio2):
    paux= Polinomio()
    mayor= polinomio1 if (polinomio1.grado>polinomio1.grado) else polinomio2
    for i in range(0, mayor.grado+1):
        total= obtener_valor(polinomio1, i) + obtener_valor(polinomio2, i)
        if(total != 0):
            agregar_termino(paux,i,total)
    return paux

def multiplicar(polinomio1, polinomio2):
    paux= Polinomio()
    pol1= polinomio1.termino_mayor
    while(pol1 is not None):
        pol2= polinomio2.termino_mayor
        valor= pol1.info.valor * pol2.info.valor
        if(obtener_valor(paux, termino) != 0):
            valor += obtener_valor(paux, termino)  
            modificar_termino(paux, termino, valor)
        else:
            agregar_termino(paux, termino, valor)
        pol2= pol2.sig
    pol1= pol1.sig
    return paux

                  