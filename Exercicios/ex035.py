s1 = float(input('PRIMEIRO segmento: '))
s2 = float(input('SEGUNDO segmento: '))
s3 = float(input('TERCEIRO segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
