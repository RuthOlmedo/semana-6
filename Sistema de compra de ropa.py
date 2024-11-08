class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Stock: {self.cantidad}")


class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        print(f"[Hombre] {self.nombre} - Talla: {self.talla} - Precio: ${self.precio} - Stock: {self.cantidad}")


class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        print(f"[Mujer] {self.nombre} - Talla: {self.talla} - Precio: ${self.precio} - Stock: {self.cantidad}")


class Inventario:
    def __init__(self):
        self.prendas = []
        self.carrito = []
        self.iniciar_inventario()

    def iniciar_inventario(self):
        # Ropa de Hombre
        self.prendas.append(RopaHombre("Camisa", 25, 50, "M"))
        self.prendas.append(RopaHombre("Pantalón", 30, 30, "L"))
        self.prendas.append(RopaHombre("Chaqueta", 55, 20, "M"))
        self.prendas.append(RopaHombre("Zapatos", 60, 25, "42"))

        # Ropa de Mujer
        self.prendas.append(RopaMujer("Falda", 28, 15, "S"))
        self.prendas.append(RopaMujer("Blusa", 22, 40, "M"))
        self.prendas.append(RopaMujer("Vestido", 45, 10, "M"))
        self.prendas.append(RopaMujer("Zapatos", 50, 20, "38"))

    def mostrar_inventario(self):
        print("\nInventario Disponible:")
        print("-" * 50)
        for i, prenda in enumerate(self.prendas, 1):
            print(f"{i}.", end=" ")
            prenda.mostrar_info()

    def agregar_al_carrito(self, numero_prenda, cantidad):
        if 1 <= numero_prenda <= len(self.prendas):
            prenda = self.prendas[numero_prenda - 1]
            if cantidad <= prenda.cantidad:
                prenda.cantidad -= cantidad
                self.carrito.append((prenda, cantidad))
                print(f"Se agregó {cantidad} de {prenda.nombre} al carrito.")
                return True
            else:
                print(f"No hay suficiente stock de {prenda.nombre}. Solo quedan {prenda.cantidad} en stock.")
        else:
            print("Número de prenda inválido.")
        return False

    def mostrar_carrito(self):
        if not self.carrito:
            print("\nEl carrito está vacío.")
            return

        print("\nCarrito de Compras:")
        print("-" * 50)
        total = 0
        for prenda, cantidad in self.carrito:
            subtotal = prenda.precio * cantidad
            print(f"{prenda.nombre} x{cantidad} = ${subtotal}")
            total += subtotal
        print(f"\nTotal a pagar: ${total}")


def menu():
    tienda = Inventario()

    while True:
        print("\nBienvenido a la Tienda de Ropa")
        print("1. Ver inventario")
        print("2. Agregar al carrito")
        print("3. Ver carrito")
        print("4. Pagar")
        print("5. Salir")

        opcion = input("\nElige una opción: ")

        if opcion == "1":
            tienda.mostrar_inventario()

        elif opcion == "2":
            tienda.mostrar_inventario()
            try:
                numero = int(input("\nNúmero de la prenda que deseas: "))
                cantidad = int(input("Cantidad que deseas: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif tienda.agregar_al_carrito(numero, cantidad):
                    print("¡Se agregó al carrito!")
                else:
                    print("No se pudo agregar al carrito.")
            except ValueError:
                print("Por favor ingresa números válidos.")

        elif opcion == "3":
            tienda.mostrar_carrito()

        elif opcion == "4":
            tienda.mostrar_carrito()
            if tienda.carrito:
                print("\n¡Gracias por tu compra!")
                tienda.carrito = []

        elif opcion == "5":
            print("\n¡Gracias por tu visita!")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    menu()
