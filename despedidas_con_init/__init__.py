"""Este fichero se ejecuta al escribir 'import despedidas_con_init'.

Aqui se decide que queda a la vista del que importa el paquete.
"""

# Este print no lo lleva ningun paquete de verdad. Esta puesto solo para que
# veas en que momento se ejecuta este fichero.
print("(se ha ejecutado el __init__.py)")

# El punto significa "esta misma carpeta".

from . import formal        # trae el MODULO  -> despedidas_con_init.formal.adios("Ana")
from .corta import adios    # trae la FUNCION -> despedidas_con_init.adios("Ana")