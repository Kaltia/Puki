from package_sys import Localpackage

class Ejecutor:
    def __init__(self):
        self._manager = Localpackage()
        self._taskq = []

    def addTask(self, task):
        """Agregar tarea a la lista de ejecucion.

        De acuerdo a la prioridad de task, sera colocada dentro de una cola
        de tareas en ejecución.

        Args:
            task: Es un objeto de tipo Task, el cual sera añadido a la lista
                de ejecucicón a corde a su prioridad.        
        """
        pass

    def delTask(self, task):
        """Elimina una tara de la lista de ejecución.

        Si la tarea se desea eliminar se tendran que eliminar todas las tareas
        que dependan de la misma, ademas de si la tarea se encuentra en ejecución
        no se podra eliminar la tarea.

        Args:
            task: Es un objeto de tipo Task o un identifcador de una Task,
                que sera eliminado de la pila de ejecución.

        """
        pass

    def getStatus(self, task):
        """Obtiene el estado ejecución de task.

        El estado de task puede ser activo, dormido, pendiente, zombi,
        hecho.
        """
        pass


    def scheduler(self, genCommand):
        """Controla la ejecucion de la lista de Tareas.
        """
        pass
