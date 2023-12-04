#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * struct listint_s - structure singly linked list
 * @n: int
 * @next: points to the next
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

listint_t *add_nodeint_end(listint_t **head, const int n);
void reverse_listint(listint_t **head);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */