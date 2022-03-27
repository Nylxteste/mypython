import 'dart:io';
void main(){
  var soma = [];

  for(int x = 0; x < 2; x++){
    print('Digite o ${x + 1}º valor: ');
    String? vall = stdin.readLineSync();
    soma.add(vall);

  }
  print(int.parse(soma[0])+ int.parse(soma[1]));
  print(int.parse(soma[0])- int.parse(soma[1]));
  print(int.parse(soma[0])* int.parse(soma[1]));
  print(int.parse(soma[0]) / int.parse(soma[1]));
}