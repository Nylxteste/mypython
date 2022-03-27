/*
Desenvolva um algoritmo que leia o nome de um vendedor, o seu salário fixo
e o total de vendas efetuadas por ele no mês
(em dinheiro). Sabendo que este vendedor ganha 15%
de comissão sobre suas vendas efetuadas, informar o seu nome,
 o salário fixo e salário no final do mês.
 */

import 'dart:io';
void main(){
  print('Informe o nome do vendedor: ');
  String? vendedor =  stdin.readLineSync();

  print('Informe o salário fixo de $vendedor: ');
  String? salario =  stdin.readLineSync();

  print('Informe o total de vendas efetuadas por $vendedor neste mês em dinheiro: ');
  String? vendas =  stdin.readLineSync();

  double resultado = double.parse(salario.toString()) + (double.parse(vendas.toString()) * 0.15);

  print('Nome: $vendedor | Salário Fixo: R\$$salario | Salário Final R\$${resultado.toStringAsFixed(2).replaceAll('.',',')}');
}