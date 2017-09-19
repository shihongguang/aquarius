#include <Python.h>
// gcc -fPIC c_python.c -o example.so -shared  -I/usr/include/python2.7 -I/usr/lib/python2.7/config

int foo(int a, int b)  
{  
  printf("you input %d and %d\n", a, b);  
  return a+b;  
}