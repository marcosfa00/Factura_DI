### Proyecto de Generación de Facturas Simplificadas

Este proyecto en Python utiliza la biblioteca ReportLab para generar facturas simplificadas en formato PDF. A continuación, se proporciona una explicación más detallada sobre los métodos y su función en el proceso de creación de la factura.

#### 1. `PositionedTable` Class

La clase `PositionedTable` está diseñada para posicionar una tabla en el documento PDF. Sus métodos son:

- `__init__(self, table, x, y)`: Este constructor recibe una tabla (objeto de ReportLab) y las coordenadas (x, y) donde se posicionará en el lienzo del PDF.

- `draw(self)`: Este método dibuja la tabla en el lienzo PDF. Guarda el estado del lienzo, traslada la tabla a la posición indicada, ajusta su tamaño al lienzo y finalmente, restaura el estado original del lienzo para permitir la adición de más tablas.

#### 2. `Factura` Class

La clase principal `Factura` coordina la generación de la factura y contiene funciones para agregar elementos clave al documento. Veamos en detalle cada método:

- `__init__(self)`: Este constructor inicializa los estilos y elementos del documento. Luego, llama a funciones específicas para construir la factura, como `bordeIzquierdo()`, `titulo()`, `nombre_logo()`, `direccion_Facturacion()`, `tablaFacturas()`, `total()`, `lineaSeparadora()`, y `piePagina()`.

- `bordeIzquierdo()`: Este método agrega un borde izquierdo a la factura. Utiliza colores distintivos para resaltar secciones importantes.

- `titulo()`: Agrega el título "FACTURA SIMPLIFICADA" en el estilo adecuado. El texto se alinea a la derecha para mayor presentación.

- `nombre_logo()`: Incorpora el nombre de la empresa y su logo en la parte superior de la factura. Utiliza estilos y coloca la imagen junto al título.

- `direccion_Facturacion()`: Agrega una tabla con la dirección y datos del cliente. Define estilos específicos para colores, tamaños de fuente y alineaciones.

- `tablaFacturas()`: Agrega la tabla de productos con descripciones, importes, cantidades y totales. Define estilos para resaltar los encabezados y datos.

- `total()`: Agrega la sección de total con un fondo oscuro y letras blancas. Establece un estilo específico para resaltar el total.

- `lineaSeparadora()`: Agrega una línea separadora debajo del total. Utiliza una tabla con una única celda que tiene un borde inferior negro.

- `piePagina()`: Agrega un agradecimiento en la parte inferior de la factura. Utiliza un estilo específico para destacar el mensaje de agradecimiento.

#### 3. Generación del Documento

- La instancia de la clase `Factura` se crea en el bloque `__main__`.
- Los métodos de la clase son llamados en un orden específico para construir la factura.
- Finalmente, se crea un documento PDF llamado 'factura.pdf' utilizando ReportLab.

#### 4. Ejecución del Script

Para generar una factura, simplemente ejecuta el script:

```bash
python factura_generator.py
```

El script creará un archivo PDF con la factura y mostrará un mensaje indicando que la factura ha sido creada. Este proyecto es altamente personalizable y puede adaptarse fácilmente a diferentes necesidades de facturación.