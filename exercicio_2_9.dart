/*
Elaborar um algoritmo que efetue a apresentação do valor da conversão
em real (R$) de um valor lido em dólar (US$). O algoritmo deverá
 solicitar o valor da cotação do dólar e também a quantidade de
  dólares disponíveis com o usuário.
 */

import 'dart:io';
void main(){
  print('Informe o valor da cotação do dólar: ');
  String? dolar = stdin.readLineSync();
  print('Informe o valor em dólar disponível à conversão: ');
  String? dolar_val = stdin.readLineSync();
  var conversao = double.parse(dolar_val.toString()) * double.parse(dolar.toString());
  print(conversao);
}