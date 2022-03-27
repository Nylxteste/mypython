/*
5. Desenvolva um algoritmo que receba um valor em metros e converta para centímetros,
 depois apresente o resultado em centímetros.
 */

import 'dart:io';
void main(){
  print('Informe a quantidade de metros: ');
  String? metro =  stdin.readLineSync();
  var centimetros = double.parse(metro.toString()) * 100;
  
  print('$metro meters convert in centimeters is $centimetros centimeter');


}