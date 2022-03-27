/*
 Desenvolva um algoritmo que receba como entrada as
  medidas de um terreno e calcule e exiba sua área do terreno.
 */

import 'dart:io';
void main(){
  print('Informe a medida ALTURA do terreno: ');
  String? medida_altura =  stdin.readLineSync();
  print('Informe a medida LARGURA do terreno: ');
  String? medida_largura =  stdin.readLineSync();

  var resultado = double.parse(medida_altura.toString()) * double.parse(medida_largura.toString());
  print('A área do terreno é de $resultado m2');
}