from cliente import Cliente
from cliente_dao import ClienteDAO

print('*** clientes de zona fit gym')
opcion = None
while opcion != 5:
    print('''Menu:
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir
    ''')
    opcion = int(input('Escribe tu opcion (1-5):'))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de cliente ***')
        for cliente in clientes:
            print(cliente)
        print()
    elif opcion == 2:
        nombre_var = input('Escribe el nombre:')
        apellido_var = input('Escribe el apellido:')
        membresia_var = input('Escribe la membresia: ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var,
                          membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'CLientes insertados: {clientes_insertados}\n')
    elif opcion == 3:
        id_cliente_var = int(input('Escribe el id del cliente a modificar:'))
        nombre_var = input('Escribe el nombre:')
        apellido_var = input('Escribe el apellido:')
        membresia_var = input('Escribe la membresia: ')
        cliente = Cliente(id_cliente_var, nombre_var, apellido_var, membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'clientes actualizados: {clientes_actualizados}\n')
    elif opcion == 4:
        id_cliente_var = int(input('Escribe el id del cliente a eliminar:'))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {clientes_eliminados}\n')
else:
    print('Salimos de la aplicacion...')