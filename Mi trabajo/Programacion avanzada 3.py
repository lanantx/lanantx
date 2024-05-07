class Alumno:
    def __init__(self, matricula, nombre, carrera, calificaciones):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.calificaciones = calificaciones

    def imprimir_info(self):
        print("Matrícula:", self.matricula)
        print("Nombre:", self.nombre)
        print("Carrera:", self.carrera)
        print("Calificaciones:", self.calificaciones)
        print("Promedio:", self.calcular_promedio())

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


def agregar_alumno():
    matricula = input("Ingrese la matrícula del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    calificaciones = []
    while True:
        calificacion_str = input("Ingrese una calificación (o escriba 'fin' para terminar): ")
        if calificacion_str.lower() == 'fin':
            break
        calificacion = float(calificacion_str)
        calificaciones.append(calificacion)
    return Alumno(matricula, nombre, carrera, calificaciones)


def mostrar_info_alumno(alumnos):
    matricula = input("Ingrese la matrícula del alumno: ")
    encontrado = False
    for alumno in alumnos:
        if alumno.matricula == matricula:
            alumno.imprimir_info()
            encontrado = True
            break
    if not encontrado:
        print("Alumno no encontrado.")


def eliminar_alumno(alumnos):
    matricula = input("Ingrese la matrícula del alumno que desea eliminar: ")
    for i, alumno in enumerate(alumnos):
        if alumno.matricula == matricula:
            del alumnos[i]
            print("Alumno eliminado exitosamente.")
            return
    print("Alumno no encontrado.")


def mostrar_todos_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
    else:
        for alumno in alumnos:
            alumno.imprimir_info()


def main():
    alumnos = []
    while True:
        print("\nMenú:")
        print("1.- Agregar Alumno")
        print("2.- Mostrar info del alumno")
        print("3.- Eliminar alumno")
        print("4.- Mostrar todos los alumnos")
        print("5.- Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alumno = agregar_alumno()
            alumnos.append(alumno)
            print("Alumno agregado exitosamente.")
        elif opcion == '2':
            mostrar_info_alumno(alumnos)
        elif opcion == '3':
            eliminar_alumno(alumnos)
        elif opcion == '4':
            mostrar_todos_alumnos(alumnos)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()