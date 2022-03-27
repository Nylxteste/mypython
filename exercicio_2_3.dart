import 'dart:io';
void main(){
  var soma = [];
  double resultado = 0;
  for(int x = 0; x < 4; x++){
    print('Digite o ${x + 1}º valor de nota: ');
    String? vall = stdin.readLineSync();
    soma.add(vall);
  }
  resultado = (double.parse(soma[0]) + double.parse(soma[1]) + double.parse(soma[2]) + double.parse(soma[3])) / 4;
  print('A média é ${resultado.toStringAsFixed(2)}.');
}