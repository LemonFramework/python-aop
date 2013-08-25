"""
python-aop is part of LemonFramework.

python-aop is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python-aop is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with python-aop. If not, see <http://www.gnu.org/licenses/>.


Copyright (c) 2013 Vicente Ruiz <vruiz2.0@gmail.com>
"""
from functools import wraps


class Aspect(object):
    """Clase base para la creación de un advise. Se pueden sobreescribir los
    métodos ``before``, ``after``, ``around`` y ``exception``."""
    
    def __init__(self, fn):
        self.function = fn
        wraps(fn)(self)
    
    def __getattr__(self, name):
        """Sobreescribimos este método para que la información de la función
        esté disponible."""
        if name == '__name__':
            return self.function.__name__
        elif name == '__doc__':
            return self.function.__doc__
        else:
            return super().__getattr__(name)
    
    def __call__(self, *args, **kwargs):
        """Comportamiento básico del aspecto."""
        self.before(*args, **kwargs)
        response = self.around(*args, **kwargs)
        self.after(*args, **kwargs)
        return response
    
    def execute(self, *args, **kwargs):
        """Esta función no se debe de sobreescribir. Se utiliza como apoyo para
        la función ``around``. En caso de que ocurra una excepción durante la
        ejecución del joinpoint se ejecutará el método ``exception``. Este
        método puedo relanzar la excepción tras ejecutar código o puede generar
        una respuesta para la ejecución del joinpoint."""
        response = None
            
        try:
            response = self.function(*args, **kwargs)
        except Exception as ex:
            response = self.exception(ex, *args, **kwargs)
        
        return response
    
    def before(self, *args, **kwargs):
        """Método que se ejecuta antes del joinpoint. La ejecución por defecto
        no realiza ninguna acción."""
    
    def after(self, *args, **kwargs):
        """Método que se ejecuta después del joinpoint. La ejecución por defecto
        no realiza ninguna acción."""
    
    def around(self, *args, **kwargs):
        """Método que se ejecuta alrededor del joinpoint. Permite personalizar
        el comportamiento que envuelve la función en cuestión. Si se
        sobreescribe este método, es necesario invocar manualmente al método
        ``execute`` para la ejecución del joinpoint.
        
        El comportamiento por defecto es la ejecución del joinpoint."""
        return self.execute(*args, **kwargs)
    
    def exception(self, exception, *args, **kwargs):
        """Este método sólo se ejecutará en el caso de que ocurra una excepción
        durante la ejecución del joinpoint.
        
        Se puede ejecutar algún código y lanzar una excepción ó generar una
        respuesta para el joinpoint.
        
        El comportamiento por defecto es relanzar la excepción."""
        raise exception
