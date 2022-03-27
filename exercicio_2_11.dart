/*
 Faça um algoritmo que receba o preço de custo de um produto e mostre
  o valor de venda. Sabe-se que o preço de custo receberá um 
  acréscimo de acordo com um percentual informado pelo usuário.
 */

import 'dart:io';
void main(){

  print('Informe o valor do produto: ');
  String? produto = stdin.readLineSync();
  print('Informe o percentual de acréscimo. Ex.: 0.10 para acréscimo de 10%. ');
  String? percentual = stdin.readLineSync();
  var conversao = double.parse(produto.toString()) + (double.parse(produto.toString()) * double.parse(percentual.toString()));
  print(conversao);
}