// importing dart:io file
import 'dart:io';
int x = 1;
int valor = 0;
void main()
{
  for (int x = 1; x <= 2; x++ ) {
    print("Digite o $xº número: ");
    String? teste = stdin.readLineSync();
    valor += int.parse(teste.toString());
  }
print(valor);

}