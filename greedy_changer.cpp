int greedy_changer(int money) {
  //write your code here
  int result = 0;
  result += money/10;
  money =  money % 10;
  result +=  money/5;
  money =  money % 5;
  money =  money + result;
  return  money;
}

int main() {
  int  money;
  std::cin >>  money;
  std::cout << greedy_changer( money) << '\n';
}