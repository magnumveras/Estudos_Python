primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print('Primeiro valor = ', primeiro_valor,
          'é maior do que segundo valor = ', segundo_valor)
elif segundo_valor > primeiro_valor:
     print('Segundo valor = {valor2} '
          'é maior do que primeiro valor = {valor1}'.
          format(valor1 = primeiro_valor, valor2 = segundo_valor))
else: 
     print(f'{primeiro_valor=} é igual', 
           f'{segundo_valor=}' )