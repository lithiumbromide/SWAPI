---
title: "eDColorFloat Class"
project: ""
interface: "eDColorFloat"
member: ""
kind: "class"
source: "emodeltoolkit/eDColorFloat/eDColorFloat_Class.htm"
---

# eDColorFloat Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains a value between 0.0 and 1.0 that represents color data.

#### Header file code

```vb
class eDColorFloat
{
public:

float F; //Sets initial value

eDColorFloat( float f = -1 ) : F( f ) {}

bool IsValid() const { return 0.0 <= F && F <= 1.0; } //Ensures that the value is between 0.0 and 1.0

operator float () const { return F; } //Allows casting the eDColorFloat to a standard C++ float easier

};
```
