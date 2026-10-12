---
title: "eDObject Class"
project: ""
interface: "eDObject"
member: ""
kind: "class"
source: "emodeltoolkit/eDObject/eDObject_Class.htm"
---

# eDObject Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Base class for many classes in the toolkit.

Your client application will never allocate an eDObject directly; however, your application can call eDObject::TypeName() in derived classes.

#### Header file code

```vb
class eDObject

virtual const char *TypeName() const = 0;
};
```
