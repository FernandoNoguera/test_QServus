import pandas as pd
import operator

def calculo_datos(arch):  
    datos = pd.read_csv(arch,sep=';') 
    promedios_categoria = []
    total_respuestas = 0 

    key = 0
    vx = 0
    vw = 0
    lista_key = [] 
    lista_vx =[]
    lista_vw =[]

    for i in datos:
        total_respuestas = len(datos)
        key +=1
        lista_key.append(key)
        lista_vx.append(vx)
    
    for i in range(key):
        vw = key-i
        lista_vw.append(vw)
        
    x = (dict(zip(lista_key, lista_vx)))
    w = (dict(zip(lista_key, lista_vw)))


    def calcular_pos_categ(categ,dict_x):
        x = dict_x
        for i in datos[categ]:
            x[i] = x[i]+1
        return x


    sumatoria_categorias={}
    calculo_categoria = []
    for i in datos:
        x = calcular_pos_categ(i,x)
        for xk,xv in x.items():
            for wk,wv in w.items():
                if xk == wk:
                    calculo = xv*wv
                    if i in sumatoria_categorias: 
                        sumatoria_categorias[i]+=calculo
                    else:
                        sumatoria_categorias[i]=calculo


    numero = 0
    for k,v in sorted(sumatoria_categorias.items(), key=operator.itemgetter(1),reverse=True): 
        numero+=1
        print(numero,') ', round(v/total_respuestas,1),k)            
                

if __name__=='__main__':
    calculo_datos('datos.csv') 
    