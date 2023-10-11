#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints information about a Python list
 * @p: PyObject - A pointer to the Python list object
 * This function takes a pointer to a Python list object
 * and prints various pieces
 * of information about the list, such as its size and allocated memory.
 */

void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	/* Get the size of the Python list.*/
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	/* Cast the Python object as a PyListObject to acces s*/
	/* list-specific attributes.*/
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	/* Iterate through the list and print information about each element.*/
	for (i = 0; i < size; i++)
	{
		/* Get the i-th item from the list.*/
		item = PyList_GetItem(p, i);

		/* Print the element number and the type name of the item.*/
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
