# Mock interview with Adil Adilli (Google)

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

class KVPDatabase:
    def __init__(self):
        self.database = {}
        self.operations = []
        
    def set(self, name, value):
        if not self.operations:
            self.database[name] = value
        else:
            self.operations[-1].append((1, name, value))
        
    def get(self, name):
        result = "NULL"
        if self.operations:
            for operation in self.operations:
                for command, key, val in operation:
                    if key == name:
                        if command == 1:
                            result = val
                        else:
                            result = "NULL"
            return result
        else:
            return self.database[name] if name in self.database else result
    
    def unset(self, name):
        if not self.operations:
            if name in self.database:
                del self.database[name]
        else:
            self.operations[-1].append((0, name, None))
        
    def begin(self):
        self.operations.append([])
        
    def rollback(self):
        if self.operations:
            self.operations.pop()
        else:
            raise Exception("There is no transaction")
        
    def commit(self):
        if self.operations:
            for operation in self.operations:
                for command, key, val in operation:
                    if command == 1:
                        self.database[key] = val
                    else:
                        del self.database[key]
        self.operations = []
        else:
            raise Exception("There is no transaction")
        
    def test(self):
        print(self.database)
        print(self.operations)
