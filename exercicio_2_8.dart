/*
 Ler dois valores para as variáveis A e B, e efetuar as trocas
  dos valores de forma que a variável A passe a possuir o valor
   da variável B e a variável B passe a possuir o valor da variável A.
    Apresentar os valores trocados.
 */

import 'dart:io';
void main(){
  print('Informe A: ');
  String? a =  stdin.readLineSync();
  print('Informe B: ');
  String? b =  stdin.readLineSync();

  print('Atualmente: A = $a e B = $b');

  String? aux = b;
  b = a;
  a = aux;

  print('Após a mudança: A = $a e B = $b');
}