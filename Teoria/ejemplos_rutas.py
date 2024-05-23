import os
import sys
from pathlib import Path

# ---

# current_dir = os.path.dirname(os.path.abspath(__file__))
# acciones_path = os.path.join(current_dir, 'acciones.py')
# acciones_3_path = os.path.join(current_dir, '..', 'acciones_3.py')

# sys.path.append(current_dir)  
# sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))  

# from acciones import Deporte, Descansar
# from acciones_3 import Deporte as Deporte_3, Descansar as Descansar_3

# Deporte.saltar("Juan")
# Deporte.nadar("Juan")
# Descansar.dormir("Juan")
# Descansar.comer("Juan")

# print()

# Deporte_3.saltar("Juan")
# Deporte_3.nadar("Juan")
# Descansar_3.dormir("Juan")
# Descansar_3.comer("Juan")

# acciones_2_path = os.path.join(current_dir, 'Ejemplo_listdir', 'acciones_2.py')
# nuevo_nombre = os.path.join(current_dir, 'Ejemplo_listdir', 'acccionesss.py')
# os.rename(acciones_2_path, nuevo_nombre)

# acciones_2_path = os.path.join(current_dir, 'Ejemplo_listdir', 'acccionesss.py')
# nuevo_nombre = os.path.join(current_dir, 'Ejemplo_listdir', 'acciones_2.py')
# os.rename(acciones_2_path, nuevo_nombre)

# ---

current_dir = Path(__file__).resolve().parent
acciones_path = current_dir / 'acciones.py'
acciones_3_path = current_dir.parent / 'acciones_3.py'

sys.path.append(str(current_dir))
sys.path.append(str(current_dir.parent))

from acciones import Deporte, Descansar
from acciones_3 import Deporte as Deporte_3, Descansar as Descansar_3

Deporte.saltar("Juan")
Deporte.nadar("Juan")
Descansar.dormir("Juan")
Descansar.comer("Juan")

print()

Deporte_3.saltar("Juan")
Deporte_3.nadar("Juan")
Descansar_3.dormir("Juan")
Descansar_3.comer("Juan")


acciones_2_path = current_dir / 'Ejemplo_listdir' / 'acciones_2.py'
nuevo_nombre = current_dir / 'Ejemplo_listdir' / 'acccionesss.py'
acciones_2_path.rename(nuevo_nombre)