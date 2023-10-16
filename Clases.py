class Ticket:
    def __init__(self, codigo=0, patente="", tipo_v=0, forma_de_pago=0, pais=0, km_recorridos=0):
        self.codigo = codigo
        self.patente = patente
        self.tipoV = tipo_v
        self.forma_de_pago = forma_de_pago
        self.pais = pais
        self.km_Recorridos = km_recorridos

    def __str__(self):
        p = "{:<22}".format("Código: " + str(self.codigo))
        p += "{:<22}".format("Patente: " + self.patente)
        p += "{:<22}".format("Tipo de Vehículo: " + str(self.tipoV))
        p += "{:<22}".format("Forma de Pago: " + str(self.forma_de_pago))
        p += "{:<22}".format("Pais de cabina: " + str(self.pais))
        p += "{:<22}".format("Kilómetros recorridos: " + str(self.km_Recorridos))
        return p
