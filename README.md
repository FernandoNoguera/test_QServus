# Test de selección QServus

La empresa Homeway, distribuidora de productos para el hogar, realizó una encuesta a través de la plataforma QServus. Entre las preguntas de la encuesta, se solicita hacer un ranking de los productos que la persona considera más importantes.

La pregunta es:

> ** Ordene de mayor a menor importancia los siguientes productos según sus prioridades: **
> - Armarios para ropa y vestidores,
> - Muebles de almacenaje,
> - Menaje y accesorios para cocinar,
> - Productos de cocina,
> - Sofás y sillones
> - Vajilla, cristalería y cubertería
> - Textiles, cortinas y alfombras
> - Productos para mascotas
> - Tecnología y electrónica para el hogar
> - Muebles para bebé e infantiles

Se debe crear un script en Python para procesar todas las respuestas recibidas y determinar un ranking que representa a todas esas respuestas, a lo que llamaremos ranking total.


## Ranking Total

#### Cálculo

El ranking total es calculado de la siguiente forma para cada alternativa:

ranking_total = (x_1*w_1 + x_2*w_2 + x_3*w_3 ... + x_n*w_n) / total_de_respuestas

En donde:
* x = Cantidad de respuestas en esa posición
* w = Peso de la posición

Peso de posición:
- Los pesos son aplicados en orden inverso.
- La primera posición un peso equivalente a la cantidad total de alternativas.
- La última posición tiene peso 1.

De esta forma, si la pregunta de ranking tiene 3 alternativas, los pesos serían los siguientes

```
| Posición en que es ordenada la alternativa | Peso que se utilizará en la fórmula |
| ------------------------------------------ | ------------------------------------|
|                #1                          |              3                      |
|                #2                          |              2                      |
|                #3                          |              1                      |
```

#### Ejemplo del cálculo:
La siguiente tabla muestra un resumen de las respuestas para una pregunta de ranking con 4 alternativas.

```
| Alternativa                 | resp pos #1 | resp pos #2 | resp pos #3 | resp pos #4 |
| --------------------------- | ----------- | ----------- | ----------- | ----------- |
| Despacho a domicilio        |      5      |      0      |      0      |     5       |
| Precios más bajos           |      8      |      1      |      1      |     0       |
| Disponibilidad de productos |      1      |      2      |      3      |     4       |
| Más locales                 |      2      |      7      |      0      |     1       |
```

Ahora se aplicarán los pesos que permitiran determinar el valor de cada alternativa.
```
| Alternativa           | cálc p#1 | cálc p#2 | cálc p#3 | cálc p#4 | ranking total |
| --------------------  | -------- | -------- | -------- | -------- | ------------- |
| Despacho a domicilio  | 5*4 = 20 | 0*3 = 0  | 0*2 = 0  | 5*1 = 5  |     2,5       |
| Precios más bajos     | 8*4 = 32 | 1*3 = 3  | 1*2 = 2  | 0*1 = 0  |     3,7       |
| Disp. de productos    | 1*4 = 4  | 2*3 = 6  | 3*2 = 6  | 4*1 = 4  |     2,0       |
| Más locales           | 2*4 = 8  | 7*3 = 21 | 0*2 = 0  | 1*1 = 1  |     3,0       |
```

Entonces el resultado que se entrega como ranking final es:
1. Precios más bajos (3,7)
2. Más locales (3,0)
3. Despacho a domicilio (2,5)
4. Disponibilidad de productos (2,0)


## Desarrollo solicitado

- Crear el archivo process.py, el cual recorrerá los datos proporcionados en el archivo datos.csv y realizará el cálculo de ranking total para cada alternativa.
- Este script deberá mostrar por pantalla el ranking final.
- El script debe ser desarrollado usando python 3.

#### Entrega

- Se debe envíar por correo un archivo zip con el archivo process.py y el conjunto de datos

#### Criterios a evaluar

- Obtener el resultado correcto al ejecutar ./process.py