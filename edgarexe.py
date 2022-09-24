
    
sillasParaCorte = 0
clientes = [1, 2]         
sillasLibres = 3-len(clientes) #3 es N
sillasOcupadas = len(clientes)

if sillasParaCorte == 0:
    sillasLibres = sillasLibres+1
    sillasOcupadas = sillasOcupadas-1

clientes.append(3)
while True:
    CantidadClientes = len(clientes)
    i = 1
    print("ha entrado el cliente", CantidadClientes)
    if sillasParaCorte > 0: #verificar si el barbero esta libre
        sillasLibres = sillasLibres+1
        sillasOcupadas = sillasOcupadas-1
        print("El cliente despierta al barbero")
        print("El barbero corta el pelo del cliente", CantidadClientes)
        print("El cliente corre satisfecho con el corte")
        del clientes[CantidadClientes-1]
    elif sillasLibres > 0: #verificar si hay espacio en la barberia
        sillasLibres = sillasLibres-1
        sillasOcupadas = sillasOcupadas+1
        print("El cliente se ha sentado a esperar")
        print("El barbero ha cortado el pelo del cliente", i)
        print("El cliente corre satisfecho con el corte")
        sillasParaCorte = sillasParaCorte-1
        while True:
            i = i+1
            CantidadClientes = len(clientes)
            if sillasOcupadas == 1:
                sillasLibres = sillasLibres+1  #verificar si hay alguien antes
                sillasOcupadas = sillasOcupadas-1
                sillasParaCorte = sillasParaCorte+1
                print("El barbero ha cortado el pelo del cliente", i)
                print("El cliente corre satisfecho con el corte")
                sillasParaCorte = sillasParaCorte-1
                del clientes[CantidadClientes-1]
                break
            else:
                sillasLibres = sillasLibres+1  #verificar si hay alguien antes
                sillasOcupadas = sillasOcupadas-1
                sillasParaCorte = sillasParaCorte+1
                print("El barbero ha cortado el pelo del cliente", i)
                print("El cliente corre satisfecho con el corte")
                sillasParaCorte = sillasParaCorte-1
                del clientes[CantidadClientes-1]
    else:
        print("El cliente se fue")
        del clientes[CantidadClientes-1]
    break