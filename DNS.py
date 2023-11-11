
import subprocess

comandos = [
    'ipconfig/release',
    'ipconfig/flushdns',
    'ipconfig/renew',
    'netsh int ip set dns',
    'netsh winsock reset',
    'shutdown /s'
]


for comando in comandos:
    subprocess.run(comando,
    shell=True)


    print("Comandos executados com sucesso!")
