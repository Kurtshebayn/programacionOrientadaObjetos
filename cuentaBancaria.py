class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance_cuenta):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance_cuenta = balance_cuenta

    def __str__(self):
        return (f'Cliente {self.nombre} {self.apellido}, numero de cuenta: {self.numero_cuenta}. '
                f'Balance cuenta: ${self.balance_cuenta}')

    def depositar(self, deposito):
        self.balance_cuenta = self.balance_cuenta + deposito
        print(f'El monto ha sido depositado, su balance ahora es: {self.balance_cuenta}')

    def retirar(self, retiro):
        if retiro < self.balance_cuenta:
            self.balance_cuenta = self.balance_cuenta - retiro
            print(f'El monto ha sido retirado, su balance ahora es: {self.balance_cuenta}')
        else:
            print('El monto indicado no puede ser retirado porque supera el valor de su cuenta')


def crear_cliente(nombre, apellido, numero_cuenta, balance_cuenta):
    cliente1 = Cliente(nombre, apellido, numero_cuenta, balance_cuenta)
    print('Cliente creado con exito')
    return cliente1


def inicio():
    opc = 0
    nombre = input("ingresa un nombre: ")
    apellido = input("ingresa un apellido: ")
    numero_cuenta = input("ingresa un numero de cuenta: ")
    balance = int(input("ingresa un balance en la cuenta: "))
    cliente = crear_cliente(nombre, apellido, numero_cuenta, balance)
    print('----------------------------------------------------------')
    print('                   Datos cliente                          ')
    print(cliente)
    while opc != 3:
        print('''Elige una opcion:
            1.- Retirar dinero
            2.- Depositar dinero
            3.- Salir''')
        opc = int(input())
        if opc == 1:
            retiro = int(input(f'ingresa la cantidad a retirar: '))
            cliente.retirar(retiro)
        elif opc == 2:
            deposito = int(input(f'ingresa la cantidad a depositar: '))
            cliente.depositar(deposito)
        print(f'Su nuevo balance es {cliente.balance_cuenta}')


inicio()