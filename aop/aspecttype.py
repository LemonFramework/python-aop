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

class AspectType(type):
    """Metaclase para la construcción de aspectos. Añade el método ``pointcut``
    a la clase, de forma que permite vincular un advise a un joinpoint."""
    
    def __new__(mcs, name, bases, classdict):
        # Preparamos una función que se encarga de realizar el pointcut para
        # cualquier método ó atributo de la clase
        def pointcut(cls, joinpoint, advise_class, **kwargs):
            # Se prepara el punto donde se ejecutará el aspecto
            joinpoint_attr = getattr(cls, joinpoint)
            # Se obtienen parámetros adicionales para el aspecto
            advise_args = () if not 'args' in kwargs else tuple(kwargs['args'])
            advise_kwargs = {} if not 'kwargs' in kwargs else dict(kwargs['kwargs'])
            # Se crea el advise
            advise = advise_class(joinpoint_attr, *advise_args, **advise_kwargs)
            # Preparamos un wrapper
            def wrapper(self, *args, **kwargs):
                return advise(self, *args, **kwargs)
            setattr(cls, joinpoint, wrapper)
        # Añadimos el método ``pointcut`` a la clase
        classdict['pointcut'] = classmethod(pointcut)
        return type.__new__(mcs, name, bases, classdict)
