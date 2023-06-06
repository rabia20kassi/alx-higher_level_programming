#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: linked list to check
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1
 */
int check_cycle(listint_t *list)
{
	listint_t *node1;
	listint_t *node2;

	if (!list || !list->next)
		return (0);

	node1 = list;
	node2 = list->next;

	while (node2 != NULL && node2->next != NULL)
	{
		node1 = node1->next;
		node2 = node2->next->next;

		if (node1 == node2)
			return (1);
	}
	return (0);
}
