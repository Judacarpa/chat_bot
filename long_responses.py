import random

R_ONE = "Bienvendio al grupo imbocar\npara ser parte de nuestra familia dejanos saber tus siguiestes datos\n  Nombre y apellido()\n  Correo()\n  Numero telefonico() "
R_ADVICE = "si estuviera en tu lugar, iria a google y buscaria eso alla"
R_TWO = "si tienes alguna demeora o facturas sin pago,\nen el siguiente correo xxxxx@xxxx podras enviarnos tu caso\npara darle manejo directo a tu incoveniente"
R_TREEH = "llama a nuestro seguro de accidentes, pero primero revisa los siguientes items\n  1.El vehiculo este registrado en systram\n  2.el carro tenga remesa y manifiesto"
R_FOUR = "El del mes y de todos los tiempos Juan David Cardona,\nbuscame en IG como @judacarpa01 ;)"

datos=[]

def unknown():
    response = ["podria decirle de otra forma? ",
                "...",
                "suena excelnte",
                "que me quieres decir?"][
        random.randrange(4)]
    return response