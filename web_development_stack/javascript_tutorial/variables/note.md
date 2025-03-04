# Javascript Variables
## Variable Types
|_*var*_|_*let*_| _*const*_ |
|-------|-------|---------|
|  |  | - used when the value should not be changed (constant) |
|  | - have block scope | - have block scop |
|  | - must be declared before use | - must be assigned a value when declared |
|  | - cannot be redeclared in the same scope | - cannot be redeclared in the same scope |
|  |  |  |
## Differences
|  | _*Scope*_ | _*Redeclare*_ | _*Reassign*_ | _*Hosited*_ | _*Binds this*_ |
|--|-----------|----------------|--------------|-------------|----------------|
| _*var*_ | No | Yes | Yes | Yes | Yes |
| _*let*_ | Yes | No | Yes | No | No |
| _*const*_ | Yes | No | No | No | No |