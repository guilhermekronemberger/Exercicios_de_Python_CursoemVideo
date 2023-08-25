from urllib import request

try:
    site = request.urlopen('https://github.com/guilhermekronemberger')

except:
    print('O site não pode ser acessado no momento.')

else:
    print('Site acessado com sucesso!')
