# importar biblioteca
import winapps

for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versão: {item.version}.')
    print(f'Data da instalação: {item.install_date}.')
    print(f'Data da Publicação: {item.publisher}.')
    print(f'Data da Publicação: {item.uninstall_string}.')
    print(f'Local da desinstalação:{item.uninstall_string}')
    print('_'*50)

# antes de subir o programa para github use o comando "pip freeze > requirements.txt"