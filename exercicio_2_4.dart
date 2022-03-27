import 'dart:io';
void main(){
  print('Informe a distância total percorrida: ');
  String? distancia =  stdin.readLineSync();
  print('Informe o total de combustível gasto: ');
  String? gasto =  stdin.readLineSync();

  var resultado = (double.parse(gasto.toString()) * 1) / double.parse(distancia.toString());
  print('Gasto medio de $resultado litro(s) por km');


}