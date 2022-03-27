/*
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) O produto do dobro do primeiro com metade do segundo.
b) A soma do triplo do primeiro com o terceiro.
 */

import 'dart:io';
void main() {
  var numero = [];
  for (int x = 1; x < 4; x ++) {
    if (x > 2){
      print('Digite o $x Nº, sendo ele um Nº inteiro.');
      numero.add(stdin.readLineSync());
    }
    else{
      print('Digite o $x Nº, sendo ele um Nº Real.');
      numero.add(stdin.readLineSync());
    };
  };
  /*
  primeiro valor solicitado
  */
 double resultado_a = int.parse(numero[0]) + (double.parse(numero[1].toString()) / 2);

 /*
 segundo valor solicitado
 */
 double resultado_b = (int.parse(numero[0]) * 3) + double.parse(numero[2].toString());
 /*
 saida de info
 */
 print('O primeiro resultado é: $resultado_a');
 print('O segundo resultado é: $resultado_b');
}