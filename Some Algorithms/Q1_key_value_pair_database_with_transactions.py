"""
* `SET name value` – Set the variable `name` to the value `value`. For
  simplicity `value` may be an string.
* `GET name` – Print out the value of the variable `name`, or `NULL` if that
  variable is not set.
* `UNSET name` – Unset the variable `name`, making it just like that variable
  was never set.

In addition to the above data commands, your program should also support
database transactions by also implementing these commands:

* `BEGIN` – Open a new transaction block. **Transactions can be nested;** a
  `BEGIN` can be issued inside of an existing block.
* `ROLLBACK` – Undo commands issued in the current transaction, and closes it
  Returns an error if no transaction is in progress.
* `COMMIT` – Close **all** open transactions, permanently applying the changes
  made in them. Returns an error if no transaction is in progress.
"""
