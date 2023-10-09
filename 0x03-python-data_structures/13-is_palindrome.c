nclude "lists.h"

/**
 *  * palindrome - Recursively checks if a linked list is a palindrome.
 *   * @left: Pointer to the leftmost node.
 *    * @right: Pointer to the rightmost node.
 *     *
 *      * Return: 1 if palindrome, 0 if not.
 *       */
int palindrome(listint_t **left, listint_t *right)
{
		int response;

			// Base case: Reached the end of the list.
			// 	if (right != NULL)
			// 		{
			// 				// Recursively check if the remaining elements are a palindrome.
			// 						response = palindrome(left, right->next);
			// 								
			// 										// If the remaining elements are a palindrome and the current elements match,
			// 												// move the left pointer to the next element and continue checking.
			// 														if (response != 0)
			// 																{
			// 																			response = (right->n == (*left)->n);
			// 																						*left = (*left)->next;
			// 																									return (response);
			// 																											}
			// 																													
			// 																															return (0); // Not a palindrome.
			// 																																}
			// 																																	
			// 																																		return (1); // Reached the end, it's a palindrome.
			// 																																		}
			//
			// 																																		/**
			// 																																		 * is_palindrome - Checks if a singly linked list is a palindrome.
			// 																																		  * @head: Pointer to the head of the linked list.
			// 																																		   *
			// 																																		    * Return: 1 if palindrome, 0 if not.
			// 																																		     */
			// 																																		     int is_palindrome(listint_t **head)
			// 																																		     {
			// 																																		     	// Check if the provided head pointer is NULL.
			// 																																		     		if (head == NULL)
			// 																																		     			{
			// 																																		     					return (0);
			// 																																		     						}
			// 																																		     							
			// 																																		     								// Call the palindrome function with the head pointer and the head of the list.
			// 																																		     									return (palindrome(head, *head));
			// 																																		     									}
