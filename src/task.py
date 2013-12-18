from UserDict import DictMixin

class Task(DictMixin):
    """Contenedor de una tarea.

    Las tareas mantienen ciertas caracteristicas que permiten llevar a un
    punto espefico a alguna actividad.

    La tarea esta diseñada para actuar como un iterador de pasos a
    realizar para completar la tarea.

    Dado que se tiene un conjunto de pasos a realizar para emacs:

         {
            "install": "package-manager install emacs",
            "config": "emacs /tmp/zoek/emacs-plugins.el"
          }

    En cada iteracion retornara una labor:

        >>> for id, task in Task(emacs):
        ...     print "El paso %s realiza (%s) " % (id, task)

        El paso install realiza (package-manager install emacs)
        El paso config realiza (emacs /tmp/zoek/emacs-plugins.el)


    Attributes:
        name: Mantiene el nombre de la tara actual
        priority: Mantiene el nivel de prioridad de la tarea
        depends: Contine una conjunto de indentificadores que se deben de
            cumplir para llevar a cabo esta tarea.
        steps: Contiene una serie de pasos a ser realizados cuando la
            tarea este activa.
        description: Contiene una descripcion de la tarea.
    """
    
    def __init__(self, name, steps, priority=0, depends=[], description=""):
        self.priority = priority
        self.steps = steps
        self.name  = name
        self.depends = depends
        self.description = description

        # TODO (os.aioria@gmail.com): Adecuar los getters, setters para
        # mantener la integridad de la tarea

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

        @property
        def description(self):
            return self._description

        @description.setter
        def description(self, description):
            self._description = description

        @property
        def depends(self):
            return self._depends

        @depends.setter
        def depends(self, depends):
            self._depends = depends

        @property
        def priority(self, priority):
            self._priority = priority

        @priority.setter
        def priority(self, description):
            self._description = description


        def __getitem__(self, key):
            return self.__steps[key]

        def __setitem__(self, key, value):
            self.__steps[key] = value

        def __iter__(self):
            for id, task in self.__steps.items():
                yield id, task
                
        def __reversed__(self):
            pass

        def __contains__(self, item):
            if item in self.__steps.items() or
               item in self.__steps.values():
                return True
            return False

        def __lt__(self, task):
            if self.priority < task.priority:
                return True
            return False

        def __le__(self, task):
            if self.priority <= task.priority:
                return True
            return False


        def __gt__(self, task):
            if self.priority > task.priority:
                return True
            return False

        def __ge__(self, task):
            if self.priority >= task.priority:
                return True
            return False

        def __eq__(self, task):
            if self.priority == task.priority:
                return True
            return False

        def __ne__(self, task):
            if self.priority != task.priority:
                return True
            return False

        def keys(self):
            return self.__steps.keys()

        def values(self):
            return self.__steps.values()
