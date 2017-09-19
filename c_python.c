#include <Python.h>
// gcc -fPIC c_python.c -o example.so -shared  -I/usr/include/python2.7 -I/usr/lib/python2.7/config

int fact(int n)
{
  if (n <= 1)
    return 1;
  else
    return n * fact(n - 1);
}

PyObject* wrap_fact(PyObject* self, PyObject* args)
{
  int n, result;

  if (! PyArg_ParseTuple(args, "i:fact", &n))
    return NULL;
  result = fact(n);
  return Py_BuildValue("i", result);
}

static PyMethodDef exampleMethods[] =
{
  {"fact", wrap_fact, METH_VARARGS, "Caculate N!"},
  {NULL, NULL}
};

void initexample()
{
  PyObject* m;
  m = Py_InitModule("example", exampleMethods);
}

