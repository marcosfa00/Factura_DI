class Factura:
    # en el contructor le pasaremos todos los datos necesarios para crear la factura
    def __init__(self,nombreArchivo,tituloFactura,nFactura,fecha,fechaEntrega,numeroCliente,codigoProducto,precioUnitario,numeroLFactura,cliente):
        self.nombreArchivo =nombreArchivo
        self.tituloFactura = tituloFactura
        self.nFactura = nFactura
        self.fecha = fecha
        self.fechaEntrega = fechaEntrega
        self.numeroCliente = numeroCliente
        self.codigoProducto = codigoProducto
        self.precioUnitario = precioUnitario
        self.numeroLFactura = numeroLFactura
        self.cliente = cliente

    def TituloFactura(self):
        logo = Image(self.nombreArchivo)
        elementsTitle = [
            ["FACTURA",]
        ]

