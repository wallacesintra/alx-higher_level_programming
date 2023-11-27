#include "lists.h"

/**
 * check_cycle - Check if a singly list has a cycle in it or loop
 * @head: Pointer to head of list
 * Return: 1 (a cycle) and 0 (no cycle)
 */

int check_cycle(listint_t *head)
{
	listint_t *pre, *next;

	if (head == NULL)
		return (0);

	pre = next = head;

	while (1)
	{
		if (next->next != NULL && next->next->next != NULL)
		{
			next = next->next->next;
			pre = pre->next;
			if (pre == next)
				return (1);
		}
		else
			return (0);

	}
}