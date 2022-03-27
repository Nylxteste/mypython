/*
 A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) 
 prestações sem juros. Faça um algoritmo que receba um valor de
  uma compra e mostre o valor das prestações..
 */

import 'dart:io';
void main(){
  print('Informe o valor da compra: ');
  String? compra = stdin.readLineSync();
  print('O valor da compra, em 5 prestações, é de: R\$${(double.parse(compra.toString())  / 5)} por prestação');
}