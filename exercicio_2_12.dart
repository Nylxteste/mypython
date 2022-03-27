/*
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês. Calcule
e mostre o total do seu salário no referido mês.
 */

import 'dart:io';
void main(){

  print('Informe o número de horas trabalhadas no mês. ');
  String? horas_trab = stdin.readLineSync();
  print('Informe o quanto você ganha por hora. ');
  String? ganho_hora = stdin.readLineSync();
  
  var resultado = double.parse(horas_trab.toString()) * double.parse(ganho_hora.toString());
  
  print('O total do seu salário este mês é R\$$resultado');
}