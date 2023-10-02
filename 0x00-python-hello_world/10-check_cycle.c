#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	if (!list)
		return (0);

	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next; /* Move slow pointer by one steps */
		fast = fast->next->next; /* Move fast pointer by two steps */
		if (slow == fast)
			return (1);  /* Cycle detected */
	}
	free(slow);
	free(fast);
	return (0); /*No cycle found */
}
