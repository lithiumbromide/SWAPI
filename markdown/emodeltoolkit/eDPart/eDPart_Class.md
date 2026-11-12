---
title: "eDPart Class"
project: ""
interface: "eDPart"
member: ""
kind: "class"
source: "emodeltoolkit/eDPart/eDPart_Class.htm"
---

# eDPart Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains one or more bodies.

#### Header file code

```vb
class eDPart : public eDObject
{
public:

eDOutcome AddBody( const eDBody *body ); //Adds a body

eDOutcome SetTransform( const eDTransform3d &transform ); //Sets a 3D transform

};
```
