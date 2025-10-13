# Sistema de Gestión Básica De Productos

# 1. Agregar producto
# 2. Mostrar productos
# 3. Buscar producto
# 4. Eliminar producto
# 5. Salir

titulo= " Sistema de gestión básica de productos. "

item_1 = "1. Agregar producto"
item_2 = "2. Mostrar productos"
item_3 = "3. Buscar producto"
item_4 = "4. Eliminar producto"
item_5 = "5. Salir"

codigo_tile = "Código"
descripcion_title = "Producto Descripción"
precio_title = "Precio"

opcion = 0
codigo_producto = 0
descripcion_producto = ""
precio_producto = 0


producto = [codigo_producto, descripcion_producto, precio_producto]

lista_productos = []

print(f"\n{titulo: ^80}\n")
while opcion != 5:
    print(f"\n{item_1} \n{item_2} \n{item_3} \n{item_4} \n{item_5}\n")
    
    opcion = input(f"Ingrese una opcion: ")
    if not opcion.isdigit():
        print(f"Error! Ingrese una opcion válida.") 
    else:
        opcion = int(opcion)
        match opcion:
            # Agregar productos
            case 1:
                descripcion_producto= input(f"Ingrese la descripcion del producto: ").strip()
                # Valido descripcion
                if descripcion_producto == "":
                    descripcion_valida = descripcion_producto != ""
                    while descripcion_valida == False:
                        print(f"Error! Debe ingresar una descripcion del producto.")
                        descripcion_producto= input(f"Ingrese la descripcion del producto: ").strip()
                        descripcion_valida = descripcion_producto != ""
                    
                precio_producto = input(f"Ingrese el precio del producto: ").strip()
                
                #valido precio
                if not precio_producto.isdigit():
                    precio_validado = False
                    while precio_validado == False:
                        print(f"Error! El precio del producto debe ser un número.")
                        precio_producto = input(f"Ingrese el precio del producto: ").strip()
                        precio_validado = precio_producto.isdigit()           
                
                precio_producto = int(precio_producto)        
                producto = [len(lista_productos) + 1, descripcion_producto.capitalize(), precio_producto]
                lista_productos.append(producto)
            # Mostrar productos    
            case 2:
                if (len(lista_productos)== 0):
                    print(f"No existen productos cargados.")
                else: 
                    print    (f"{codigo_tile: <1} {descripcion_title: ^90}   {precio_title: >12}")
                    for elemento in lista_productos:
                        print(f"{elemento[0]: <1} {elemento[1]: ^100} $ {elemento[2]: >10}")
            
            # Buscar producto
            case 3:
                busco_producto = ""
                if (len(lista_productos)== 0):
                    print(f"No existen productos cargados.")
                else:
                    busco_producto = input(f"Ingrese el nombre del producto: ").strip().lower()
                    busca_valida = busco_producto != ""
                    while busca_valida == False:
                        print(f"Error! Ingrese un nombre de producto válido.")
                        busco_producto = input(f"Ingrese el nombre del producto: ").strip().lower()
                        busca_valida = busco_producto != ""
                print(f"\nEl producto buscado es: {busco_producto}")
                total_encontrados = 0
                productos_encontrados = []
                for elemento in lista_productos:
                    if busco_producto.lower() in elemento[1].lower():
                        productos_encontrados.append(elemento)
                        total_encontrados +=1
                        
                if total_encontrados > 0:
                    print    (f"{codigo_tile: <1} {descripcion_title: ^90}   {precio_title: >12}")
                    for elemento in productos_encontrados:
                        print(f"{elemento[0]: <1} {elemento[1]: ^100} $ {elemento[2]: >10}")
                else:
                    print (f"Producto inexistente.")
            
            # Elimino producto
            case 4:
                busco_codigo_producto = 0
                codigo_validado = False
                if (len(lista_productos)== 0):
                    print(f"No existen productos cargados.")
                else:
                    print    (f"{codigo_tile: <1} {descripcion_title: ^90}   {precio_title: >12}")
                    for elemento in lista_productos:
                        print(f"{elemento[0]: <1} {elemento[1]: ^100} $ {elemento[2]: >10}")
                        
                    busco_codigo_producto = input(f"Ingrese el codigo del producto a eliminar: ").strip()
                
                    # Valido codigo
                    if not busco_codigo_producto.isdigit():
                        codigo_validado = False
                    else:
                         if 0 < int(busco_codigo_producto) <= len(lista_productos):
                             codigo_validado = True
                    while codigo_validado == False:
                        print(f"Error! El codigo del producto debe ser un número mayor a 0 y menor a {len(lista_productos) + 1}.")
                        busco_codigo_producto = input(f"Ingrese el codigo del producto a eliminar: ").strip()
                        codigo_validado = busco_codigo_producto.isdigit() and 0 < int(busco_codigo_producto) <= len(lista_productos)
       
                    busco_codigo_producto = int(busco_codigo_producto)
                    print(f"\nproducto a eliminar: \n")
                    print    (f"{codigo_tile: <1} {descripcion_title: ^90}   {precio_title: >12}")
                    producto_delete = lista_productos[busco_codigo_producto-1]
                    print(f"{producto_delete[0]: <1} {producto_delete[1]: ^100} $ {producto_delete[2]: >10}") 
                    
                    # validacion final S/N
                    
                    print(f"Desea eliminar el producto {producto_delete[1]} ") 
                    valido_confirmacion = input(f"confirme S/N: ")
                    while not valido_confirmacion.lower() == "s" and not valido_confirmacion.lower() == "n":
                        valido_confirmacion = input(f"Error! Ingrese S/N: ")
                        
                    if valido_confirmacion.lower() == "s":
                        lista_productos.pop(busco_codigo_producto-1)
                        print(f"\n Producto eliminado correctamente.")
                    else:
                        print(f"\n Eliminacion cancelada.")
                           
            case _:
                if  not 0 < opcion <= 5:
                    print(f"\n Error! Ingrese una opción válida") 
                else:
                    print(f"gracias by")    
                
                
    

        
    
    